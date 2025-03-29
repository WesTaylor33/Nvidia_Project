Fruit Classifier

 This is a retrained model of resnet18 that can identify select fruits and vegetables. 

<img width="1281" alt="Screenshot 2025-03-29 at 8 42 21 PM" src="https://github.com/user-attachments/assets/b43ab518-20af-4ca5-a5c0-12a0b096b504" />
Image of the trained model classifying an Apple.

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

<img width="1043" alt="Screenshot 2025-03-29 at 8 37 41 PM" src="https://github.com/user-attachments/assets/112c4fe6-bb55-4e7a-97d1-4f2d829f955c" />

Uses Imagenet and resnet18.

<img width="429" alt="Screenshot 2025-03-29 at 8 39 00 PM" src="https://github.com/user-attachments/assets/04d53bd3-d1d8-4966-bb2c-68aa7cd81480" />
When using live video feed, percentages will be displayed at the top as shown here.


## Running this project

1. Clone the project
2. Install Jetson-Inference and Jetson-Util
3. Cd into the project folder
4. To run my program run: python3 classify.py /dev/video0 webrtc://@:8554/my_output
<img width="1063" alt="Screenshot 2025-03-29 at 8 40 44 PM" src="https://github.com/user-attachments/assets/c697e8bf-8dac-4ebd-97df-752c976d41fb" />

Link to video (https://youtu.be/XTGlZWSlSQ0)
