import sys
import argparse

from jetson_inference import imageNet
from jetson_utils import videoSource, videoOutput, cudaFont, Log

font = cudaFont()
parser = argparse.ArgumentParser()
parser.add_argument("input", type=str, default="/dev/video0", nargs='?', help="URI of the input stream")
parser.add_argument("output", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="models/fruitsv3/resnet18.onnx", help="path to the model to use")
parser.add_argument("--labels", type=str, default="models/fruitsv3/labels.txt", help="path to the labels file")
parser.add_argument("--input_blob", type=str, default="input_0", help="name of the input blob")
parser.add_argument("--output_blob", type=str, default="output_0", help="name of the output blob")
opt = parser.parse_args()

# Load the custom network
net = imageNet(model=opt.network, labels=opt.labels, input_blob=opt.input_blob, output_blob=opt.output_blob)

input = videoSource(opt.input, argv=sys.argv)
output = videoOutput(opt.output, argv=sys.argv)

while True:
    # capture the next image
    img = input.Capture()

    if img is None: # timeout
        continue  

    # classify the image and get the topK predictions
    # if you only want the top class, you can simply run:
    #   class_id, confidence = net.Classify(img)
    predictions = net.Classify(img, topK=3)

    # draw predicted class labels
    for n, (classID, confidence) in enumerate(predictions):
        classLabel = net.GetClassLabel(classID)
        confidence *= 100.0

        print(f"imagenet:  {confidence:05.2f}% class #{classID} ({classLabel})")

        font.OverlayText(img, text=f"{confidence:05.2f}% {classLabel}", 
                         x=5, y=5 + n * (font.GetSize() + 5),
                         color=font.White, background=font.Gray40)
                         
    # render the image
    output.Render(img)

    # update the title bar
    output.SetStatus("{:s} | Network {:.0f} FPS".format(net.GetNetworkName(), net.GetNetworkFPS()))

    # print out performance info
    net.PrintProfilerTimes()

    # exit on input/output EOS
    if not input.IsStreaming() or not output.IsStreaming():
        break