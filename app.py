from flask import Flask, render_template, request, Response, send_file, url_for
import cv2
import os
from yolov10_utils import detect_objects
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

camera = cv2.VideoCapture(0)

@app.route('/')
def index():
    return render_template('index.html')

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        frame = detect_objects(frame)
        _, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    ext = filename.split('.')[-1].lower()

    if ext in ['jpg', 'jpeg', 'png']:
        # Process image
        img = cv2.imread(filepath)
        img = detect_objects(img)
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], f"processed_{filename}")
        cv2.imwrite(output_path, img)

        return render_template('index.html', image_file=output_path)

    else:
        # Process video
        cap = cv2.VideoCapture(filepath)
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], f"processed_{filename}")
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = None

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame = detect_objects(frame)
            if out is None:
                out = cv2.VideoWriter(output_path, fourcc, cap.get(cv2.CAP_PROP_FPS), (frame.shape[1], frame.shape[0]))
            out.write(frame)

        cap.release()
        if out:
            out.release()

        return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
