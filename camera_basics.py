import cv2

camera = cv2.VideoCapture(0) #stores camera connect. 0 is usually default. My webcam unfortunately does not work




print(camera.isOpened()) #returns True if camera opened false otherwise
while True:
    success, frame = camera.read() #(bool, captured image)

    if not success:
        print("Could not capture frame.")
        break
    frame = cv2.flip(frame, 1)

    height, width = frame.shape[:2]
    left = width//4
    right = width *3 // 4
    top = height // 6
    bottom = height *5//6

    cv2.rectangle(frame, (left, top), (right, bottom), (0,0,255),3)  #creates a green border (point1, point 2, color, thickness)
    cv2.circle(frame, (width//2, height//2), 5, (0, 255, 0), -1) #tiny circle
    cv2.putText(frame, "put your hand here",  (left, top - 15),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),1, cv2.LINE_AA)

 #creates a green border (point1, point 2, color, thickness)
    cv2.imshow("My camera", frame)
    key = cv2.waitKey(1)

    if key == ord("q"):
        break




camera.release() #closes connects and frees webcam
cv2.destroyAllWindows() #closes window