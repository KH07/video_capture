import cv2

def main():

    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)

    # Create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 24.0, (640, 480))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break

        vidout = cv2.resize(frame, (640, 480))
        out.write(vidout)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
