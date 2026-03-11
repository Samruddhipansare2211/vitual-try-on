
# 👗 Virtual Try-On for Clothing Using Augmented Reality and AI

<p align="center">
<img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python"/>
<img src="https://img.shields.io/badge/Flask-Web_Framework-orange?style=for-the-badge&logo=flask"/>
<img src="https://img.shields.io/badge/OpenCV-Image_Processing-red?style=for-the-badge&logo=opencv"/>
<img src="https://img.shields.io/badge/MediaPipe-Pose_Detection-green?style=for-the-badge"/>

</p>

---

## 🌟 Project Overview

Online shopping for apparel often leads to uncertainty because customers cannot try clothes before purchasing. This results in **high return rates** and **poor customer satisfaction**.

Our solution: a **Virtual Try-On System** that allows users to:

* Upload full-body photos or use a webcam.
* Select and switch between multiple outfits seamlessly.
* See **realistic AI-powered previews** in real-time.
* Enjoy an intuitive and visually appealing interface.

---

## 🎯 Key Features

| Feature                     | Description                                                 |
| --------------------------- | ----------------------------------------------------------- |
| **AI Body Detection**       | Detects user body landmarks for precise clothing alignment. |
| **Multiple Outfit Support** | Upload and switch between multiple clothes instantly.       |
| **Camera Try-On**           | Real-time virtual try-on using webcam feed.                 |
| **Instant Results**         | Processed results displayed immediately.                    |
| **Seamless Switching**      | Change outfits without page refresh.                        |

---

## 🏗️ Architecture

```mermaid
flowchart LR
    User --> WebApp[Flask Application]
    WebApp --> AI[Pose Detection & Cloth Overlay]
    AI --> Assets[Cloth & Model Images]
    WebApp --> Browser[Display Try-On Result]
```

---

## 🔁 Application Flow

```mermaid
sequenceDiagram
    participant User
    participant Browser
    participant FlaskApp
    participant AI

    User->>Browser: Upload Image / Start Camera
    Browser->>FlaskApp: Send Image
    FlaskApp->>AI: Apply Cloth Overlay
    AI-->>FlaskApp: Return Processed Image
    FlaskApp-->>Browser: Display Try-On Result
```

---

## 📂 Project Structure

```
Virtual-Try-On-Application/
│
├── assets/
│   ├── cloth/             # Cloth images for upload
│   └── image/             # Example model images / camera captures
│
├── client-side/
│   ├── templates/
│   │   └── index.html     # Frontend template
│   ├── app.py             # Flask backend
│   └── requirements.txt   # Python dependencies
│
├── cloth_mask.py          # Cloth masking module
├── dataset.py             # Dataset processing module
├── remove_bg.py           # Background removal module
└── .vscode/
    └── settings.json      # Optional VS Code settings
```

---

## 🛠️ Setup Instructions

### 1️⃣ Open Project in VS Code

Open the **Virtual-Try-On-Application** folder in VS Code.

---

### 2️⃣ Create Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```
---

### 3️⃣ Install Dependencies

```bash
pip install -r requirement.txt
```

**Key Packages:**

* Flask – Web framework
* numpy – Array operations
* OpenCV (`opencv-python`) – Image processing
* MediaPipe – Pose detection
* Pillow – Image manipulation

---

### 4️⃣ Run the Application

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 🖼️ Screenshots & Demo

| Upload Try-On                                     | Camera Try-On                                     |
| ------------------------------------------------- | ------------------------------------------------- |
| ![Upload Result](Project Screenshot\Screenshot_upload.png) | ![Camera Result](Project Screenshot\Screenshot_camera.png) |

🎥 **Demo Video:** [assets/demo_video.mp4](assets/demo_video.mp4)

---

## ⚡ How to Use

### Upload Try-On

1. Click **Choose File** to select a cloth image (`assets/cloth/`) and a model image (`assets/image/`).
2. Click **Try Outfit** to see the virtual try-on result.

### Camera Try-On

1. Click **Start Camera** to enable webcam.
2. Click **Capture** to apply the selected cloth.
3. Switch outfits using **Next/Previous** buttons seamlessly.

---

## 💡 Future Improvements

* Real-time AR overlay without manual capture.
* Mobile-friendly, fully responsive design.
* Enhanced lighting and shading for realistic rendering.
* Integration with e-commerce platforms for instant purchase.

---

## 👩‍💻 Author

**Samruddhi Pansare – Software Engineer | AI & Computer Vision Enthusiast**

<p align="center">
<a href="https://www.linkedin.com/in/samruddhi-pansare-b34371328" target="_blank">
<img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>
&nbsp;&nbsp;
<a href="https://github.com/Samruddhipansare2211" target="_blank">
<img alt="GitHub" src="https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github&logoColor=white"/>
</a>
</p>

**Highlights:**

* ✅ Passionate about **AI-powered applications** and real-time computer vision.
* ✅ **Python, Flask, OpenCV, MediaPipe, Tailwind CSS** – core technical expertise.
* ✅ Focused on building **innovative, practical software solutions**.

---

