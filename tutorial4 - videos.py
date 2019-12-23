import cv2

cap = cv2.VideoCapture(0)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(str(width) + " " + str(height))

while cap.isOpened():

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Video', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):    # use cv2.waitKey(1) for videos and cv2.waitKey(0) for images
        break

cap.release()
cv2.destroyAllWindows()
