import cv2

def access_ip_camera(ip_address):
    # Open a connection to the IP camera
    cap = cv2.VideoCapture(ip_address)

    if not cap.isOpened():
        print("Error: Could not open video stream from IP address.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture image.")
            break

        # Display the resulting frame
        cv2.imshow('IP Camera Stream', frame)

        # Press 'q' to exit the video stream
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Replace 'http://<ip_address>:<port>/video' with the actual IP address and port
    ip_address = 'http://192.168.1.101:8080/video'
    access_ip_camera(ip_address)

