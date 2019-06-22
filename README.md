# BagFile2Video-and-Rectification
This repository contains a script to convert Bag file to Video(in .avi) and another script to rectify a video from a distorted video  taken by stereo camera.
## Steps to obtain the video from bag file.
1) Run the script cvtBag2Vid.py like a python script.
```
python  cvtBag2Vid.py
```
2) Play the bagfile.

```
rosbag  play file.py
```
3) You will find your file by the name of output.avi in your pwd.
(Don't forget to change the name of the ros topic in the file)
