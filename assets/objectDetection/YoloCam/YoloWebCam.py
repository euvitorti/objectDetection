import math
import cv2
import cvzone
from ultralytics import YOLO

# Initialize camera object
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set the width of the captured video to 1280 pixels
cap.set(4, 720)   # Set the height of the captured video to 720 pixels

# Load YOLO model with specified weights
model = YOLO("../Yolo-Weights/yolov8l.pt")

while True:
    success, img = cap.read()  # Capture a frame from the camera
    if not success:  # If frame is not captured successfully, skip the iteration
        continue

    results = model(img, stream=True)  # Perform object detection on the captured frame
    for r in results:
        boxes = r.boxes  # Get bounding boxes from the results
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]  # Extract coordinates of the bounding box

            # Convert coordinates to integers
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1  # Calculate width and height of the bounding box
            cvzone.cornerRect(img, (x1, y1, w, h))  # Draw a corner rectangle on the image

            conf = math.ceil((box.conf[0] * 100)) / 100  # Calculate confidence level and round it to two decimal places
            cls = int(box.cls[0])  # Get the class index of the detected object
            class_name = model.names[cls]  # Get the class name using the class index

            # Put text on the image with the class name and confidence level
            cvzone.putTextRect(img, f'{class_name} {conf}', (max(0, x1), max(35, y1)), scale=3, thickness=3)

    cv2.imshow("Image", img)  # Display the image
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Break the loop if 'q' key is pressed
        break

# Release the camera and destroy all OpenCV windows
cap.release()
cv2.destroyAllWindows()
