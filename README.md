Fruit Classifier

 This is a retrained model of resnet18 that can identify select fruits and vegetables. 

![add image descrition here](direct image link here)

## The Algorithm

This uses a while loop to process each image, and within each image it is passed through a retrained version of the model that identifies which fruit or vegetable it is.
Possible classes:
- Apple
- Banana
- Cabbage
- Carrot
- Cherry
- Cucumber
- Eggplant
- Grapes
- Kiwi
- Mango
- Orange
- Pear
- Strawberry
- Zucchini

## Running this project

1. Clone the project
2. Install Jetson-Inference and Jetson-Util
3. Cd into the project folder
4. To run my program run: python3 classify.py /dev/video0 webrtc://@:8554/my_output

[View a video explanation here](video link)
