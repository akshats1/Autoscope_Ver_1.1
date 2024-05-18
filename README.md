# Autoscope_Ver_1.1
Autoscope Software version 1.1 is ready 

```bash 
1-> css need to Update 
2-> video capture Module work is (DONE) Both starting and stopping(Refinement Needed)
3-> Motor control with user(Module is Done) But only integration with main UI is left
4-> resolution (4056X3040) image is capturing But Lag is there 
```
```bash 
Packages we need to Install:
See requirements.txt for details
```
```bash 
OS: Rasbian Bullseye
Hardware:Raspberry pi 4 ,Ardino
```
### Installation of Package getting system ready:
```bash 
git clone https://github.com/
cd wherever you have clone the repository
pip install -r requirements.txt





```
### How to run Flask Application
After installing the packages :run the following command
```bash 
python3 app_update.py
run localhost:// on your browser
```
### Folder Structure for Autoscope_ver_1.1
```
├── app.py
├── app_update.py
├── camera_update_new.py
├── camera_update_new_resolution.py
├── LICENSE
├── README.md
├── requirements.txt
├── screenshots
│   ├── 2024-05-17-181259_800x480_scrot.png
│   └── captured_image_2024-05-16_18-19-58.jpg
├── static
│   ├── scripts.js
│   ├── style2.css
│   ├── style.css
│   └── style_old.css
└── templates
    ├── index.html
    ├── index_old.html
    └── start.html
```

### screenshots
![alt text](screenshots/2024-05-17-181259_800x480_scrot.png)

captured image of plant cell
![alt text](screenshots/captured_image_2024-05-16_18-19-58.jpg)