# Object Scope 🔍
A lightweight web application that allows users to perform real-time and file-based object detection using YOLOv10 via a Flask-powered web interface.

---

 🚀 Features
- Real-time object detection using webcam.
- Upload image/video files for YOLOv10-based detection.
- Built using Flask for a simple yet efficient backend.
- Integrated with YOLOv10 for accurate object detection.
- Displays results with bounding boxes and class labels.

 🧠 Tech Stack
- Python 3.8+
- Flask
- OpenCV
- YOLOv10 (Ultralytics)
- HTML/CSS + Bootstrap (Frontend)

 🛠️ Installation & Setup

1. Clone the repository
bash
git clone https://github.com/Hydra404coder/Object_Scope.git

cd Object_Scope
Create and activate a Python virtual environment
python -m venv venv

# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt

🤖 YOLOv10 Setup
1. Clone the YOLOv10 repository
 git clone https://github.com/WongKinYiu/yolov10.git
cd yolov10

🧪 Run Flask App
# Activate virtual environment if not already:
# source venv/bin/activate

python app.py

Object_Scope/
├── app.py               > Flask app
├── yolov10_infer.py     > YOLOv10 inference logic
├── templates/
│   └── index.html       > Main frontend
├── static/
│   └── styles.css       > CSS styles
├── uploads/             > Uploaded images/videos
├── results/             > Output with detection
└── models/
    └── yolov10n.pt      > YOLOv10 model weights


