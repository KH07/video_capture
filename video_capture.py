import time
import cv2

def main():

    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)

    width = int(cap.get(3))
    height = int(cap.get(4))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    recording = False

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            cv2.imshow('frame', frame)

        key = cv2.waitKey(1) & 0xFF

        # Press 'R' to start recording
        if key == ord('r') and recording is False:
            # Create a VideoWriter object
            filename = time.strftime("%Y%m%d-%H%M%S") + '.avi'
            out = cv2.VideoWriter(filename, fourcc, 24.0, (width, height))
            recording = True

        if recording:
            out.write(frame)

        # Press 'S' to stop recording
        if key == ord('s'):
            recording = False
            out.release()
            continue

        # Press 'Q' to quit the program
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
