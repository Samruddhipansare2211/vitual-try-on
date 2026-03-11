from flask import Flask, request, render_template, jsonify
from PIL import Image
import cv2
import numpy as np
import mediapipe as mp
from io import BytesIO
import base64

app = Flask(__name__)

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

uploaded_cloths = []

def remove_white_background(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
    b,g,r = cv2.split(img)
    rgba = cv2.merge([b,g,r,mask])
    return rgba

def apply_cloth(model_img, cloth_img):
    h, w, _ = model_img.shape
    rgb = cv2.cvtColor(model_img, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb)
    if not results.pose_landmarks:
        return model_img
    lm = results.pose_landmarks.landmark
    l_shoulder = (int(lm[11].x*w), int(lm[11].y*h))
    r_shoulder = (int(lm[12].x*w), int(lm[12].y*h))
    l_hip = (int(lm[23].x*w), int(lm[23].y*h))
    cloth_width = abs(r_shoulder[0]-l_shoulder[0]) + 180
    cloth_height = abs(l_hip[1]-l_shoulder[1]) + 200
    cloth_resized = cv2.resize(cloth_img, (cloth_width, cloth_height))
    x_offset = int((l_shoulder[0]+r_shoulder[0])/2 - cloth_width/2)
    y_offset = l_shoulder[1] - 60
    result = model_img.copy()
    ch,cw = cloth_resized.shape[:2]
    if x_offset < 0: x_offset=0
    if y_offset < 0: y_offset=0
    if x_offset+cw>w: cw=w-x_offset
    if y_offset+ch>h: ch=h-y_offset
    cloth_resized = cloth_resized[0:ch,0:cw]
    alpha = cloth_resized[:,:,3]/255.0
    cloth_rgb = cloth_resized[:,:,:3]
    roi = result[y_offset:y_offset+ch, x_offset:x_offset+cw]
    for c in range(3):
        roi[:,:,c] = alpha*cloth_rgb[:,:,c] + (1-alpha)*roi[:,:,c]
    result[y_offset:y_offset+ch, x_offset:x_offset+cw] = roi
    return result

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/preds', methods=['POST'])
def submit():
    global uploaded_cloths
    uploaded_cloths = []
    cloth_files = request.files.getlist('cloth')
    model_file = request.files['model']

    model_bytes = np.frombuffer(model_file.read(), np.uint8)
    model_img = cv2.imdecode(model_bytes, cv2.IMREAD_COLOR)

    op_list = []
    for cloth in cloth_files:
        cloth_bytes = np.frombuffer(cloth.read(), np.uint8)
        cloth_img = cv2.imdecode(cloth_bytes, cv2.IMREAD_COLOR)
        cloth_img = remove_white_background(cloth_img)
        uploaded_cloths.append(cloth_img)

        result = apply_cloth(model_img, cloth_img)
        result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(result_rgb)
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        op_list.append(base64.b64encode(buffer.getvalue()).decode())

    return render_template("index.html", op_list=op_list)

@app.route('/camera_tryon', methods=['POST'])
def camera_tryon():
    global uploaded_cloths
    if len(uploaded_cloths) == 0:
        return jsonify({"error":"Upload cloth first"})
    index = int(request.json.get("index",0)) % len(uploaded_cloths)

    data = request.json["image"]
    img_bytes = base64.b64decode(data.split(",")[1])
    np_arr = np.frombuffer(img_bytes, np.uint8)
    model_img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    result = apply_cloth(model_img, uploaded_cloths[index])
    result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(result_rgb)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_base64 = base64.b64encode(buffer.getvalue()).decode()
    return jsonify({"image": img_base64})

if __name__=="__main__":
    app.run(debug=True)