import cv2
import datetime

cap = cv2.VideoCapture(0)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(str(width) + " " + str(height))

while cap.isOpened():

    ret, frame = cap.read()

    if ret:

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(width) + 'Height: ' + str(height)
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, datet, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # use cv2.waitKey(1) for videos and cv2.waitKey(0) for images
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()