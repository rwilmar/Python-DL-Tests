import argparse
import cv2
import numpy as np

def get_args():
    
    parser = argparse.ArgumentParser("Handle an input stream")
    # -- Create the descriptions for the commands
    i_desc = "The location of the input file"

    # -- Create the arguments
    parser.add_argument("-i", help=i_desc)
    args = parser.parse_args()

    args.isImage=False
    if args.i == "CAM":
        args.i=0
    elif args.i.endswith('.jpg') or args.i.endswith('.png'):
        args.isImage=True

    return args


def capture_stream(args):
    ### Handle image, video or webcam
    cap = cv2.VideoCapture(args.i)
    cap.open(args.i)
    ### Get and open video capture
    width=100
    height=100
    fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
    out = cv2.VideoWriter('out.mp4', fourcc, 30, (width,height))
    while cap.isOpened():
        # Read the next frame
        flag, frame = cap.read()
        if not flag:
            break
        key_pressed = cv2.waitKey(60)
    ###  Re-sizing the frame to 100x100
        resized = cv2.resize(frame, (width, height), interpolation = cv2.INTER_AREA)
    ###  Add Canny Edge Detection to the frame, 
    ###       stack... to make a 3-channel image
        edges = cv2.Canny(resized,100,200)
        edges = np.dstack((edges, edges, edges))
    ### Write out the frame, depending on image or video
        out.write(edges)
    
    # Break if escape key pressed
        if key_pressed == 27:
            break
    out.release()
    cap.release()
    cv2.destroyAllWindows()
    print("process finished")


def main():
    args = get_args()
    capture_stream(args)


if __name__ == "__main__":
    main()
