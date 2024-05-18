from flask import Flask, render_template, Response,jsonify
import time
import io
import threading
import PIL.Image
from camera_update_new import Camera 
#from camera_update_new_resolution import Camera # Import your Camera class
import atexit
from datetime import datetime

app = Flask(__name__)
# adding save directory
save_dir="/home/pi/Pictures/Saved_videos/"
camera = Camera(save_dir=save_dir)

@app.route('/')
# 16 May 
def start_page():
    #return render_template('index.html')
    #return render_template('index.html')
    return render_template('start.html')
@app.route('/index')
def index_page():
    return render_template('/index.html')

def generate_frames():
    while True:
        frame = camera.get_frame()  # Get a frame from the camera
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        time.sleep(0.5)  # Adjust sleep time as needed

@app.route('/video_record')
def video_record():
    filename=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+'.mp4'
    # for recording the live video
    camera.start_recording(filename)
    return 'video recording started'

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/capture')
def capture():
    camera.capture_image()  # Capture an image
    #return 'Image captured!'
    return 'Image Captured'

@app.route('/stop_record')
def stop_capture():
    camera.stop_recording()  # Stop video recording
    return 'Video recording stopped!'
def cleanup():
    camera.close()# After Picamera stop preview close the camera

if __name__ == "__main__":
    atexit.register(cleanup)# for releasing the resources of picamera
    app.run(debug=True,use_reloader=False)

