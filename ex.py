j=5
print ("hola", j)

cap = cv2.VideoCapture(args.i)
    cap.open(args.i)

    while cap.isOpened():
        # Read the next frame
        flag, frame = cap.read()
        if not flag:
            break
        key_pressed = cv2.waitKey(60)

        # Break if escape key pressed
        if key_pressed == 27:
            break

        # Release the out writer, capture, and destroy any OpenCV windows
    out.release()
    cap.release()
    cv2.destroyAllWindows()