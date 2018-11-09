# Pyqt_trackingPlayer

## Introduction
This project is for the tracking player
the player is divided into two part:
1. play the tracker with choosing the camera and starting frame
2. play the tracker with specified ID

## Development Environment
- Python 3.5 + tensorflow + pyqt5

## Command Line
- if change the ui ```pyuic5 vis.ui > vis.py```
- if change the qt rescource (qrc) ```Pyrcc5 resource.qrc -o resource_rc.py```
- to run the project ```python showui.py```

## Step to play the tracking video
1. choose the camera
2. choose the start frame
3. choose the end frame
4. click the ok button
5. click the start button to play the video
6. click the stop button to stop the video

## Version Update Information
- 2018/11/8: upload the total python file
- 2018/11/9: Now, we can change the camera number when we play part 2 and the ID go to another camera
