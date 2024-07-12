import cv2

def view_webcam(ip_address):
    # Create a VideoCapture object with the IP address
    stream_url = f"http://{ip_address}/video"
    cap = cv2.VideoCapture(stream_url)

    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return

    try:
        # Display the video stream
        while True:
            # Read the frame from the video stream
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame.")
                break

            # Display the frame
            cv2.imshow('IP Camera Stream', frame)

            # Press 'q' to quit the loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        # Release the VideoCapture object and close display window
        cap.release()
        cv2.destroyAllWindows()

# Replace '192.168.1.2:8080' with your IP camera's IP address and port
ip_address = '192.168.0.20:8080'
view_webcam(ip_address)

