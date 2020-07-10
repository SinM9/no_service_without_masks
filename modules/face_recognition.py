import cv2
import face_recognition

video_capture = cv2.VideoCapture("/dev/video0")

face_locations = []

while True:
    ret, frame = video_capture.read()

    # Find all the faces in the current frame of video
    face_locations = face_recognition.face_locations(frame)

    # Display the results
    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
