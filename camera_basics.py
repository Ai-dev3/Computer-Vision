import cv2

camera = cv2.VideoCapture(0) #stores camera connect. 0 is usually default

print(camera.isOpened()) #returns True if camera opened false otherwise

success, frame = camera.read() #(bool, captured image)
print("Frame captured:", success)

if success: #checks if we recieved the image
    print("Frame shape:", frame.shape) #dimensions
    cv2.imshow("My camera", frame) #display
    cv2.waitKey(0) #wait for key press

camera.release() #closes connects and frees webcam
cv2.destroyAllWindows() #closes window