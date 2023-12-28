# Defect Detection Robot for PCB's

## Purpose
- Quickly detect defects on PCB
- Create large map with all defects labeled on PCB
- Take individual zoomed in pictures of defects using secondary microscope camera
- Do this for multiple PCB's without the need for a human to place PCB's
- Work for more than one type of PCB

## Plan
- Center stepper motors, move to 0 position for x,y,z axis
- Autofocus the z-axis so that ESP32-CAM will be in focus
- Use ESP32 to quickly take a few large images of PCB
- Send this data to RaspberryPi using MQTT protocol
- Use UNET to find defects in PCB
- (Extra: Distribute work among multiple PC's using Celery/RabbitMQ)
- Create map with labeled defects
- Use Aruco markers to tract where defects are located
- Autofocus z-axis so microscope camera will be in focus
- Using position of Aruco markers, track defects using microscope
- Send images of defects to RaspberryPi using MQTT protocol
- Display map and zoomed in defects using a website

## Feature Details
### Auto Adjust Feature
- Detect if image is blurry 
- Use LaPlacian filter, find variance in edges
- Adjust z-axis of robot to focus camera

### Center Motors
- https://www.youtube.com/watch?v=YsLykxnHApg
- https://www.youtube.com/watch?v=QRCvC5xhJCw