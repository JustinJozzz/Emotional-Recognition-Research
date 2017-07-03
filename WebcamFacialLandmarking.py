import dlib
import cv2
from imutils.video import WebcamVideoStream

video_capture = WebcamVideoStream(src=0).start() #start webcam on a new thread
detector = dlib.get_frontal_face_detector() #Face detector
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") #get pre trained model

while True:
    frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    clahe_image = clahe.apply(gray)

    detections = detector(clahe_image, 1) 

    for k,d in enumerate(detections): 
        
        shape = predictor(clahe_image, d) #Get coordinates
        for i in range(1,68): 
            cv2.circle(frame, (shape.part(i).x, shape.part(i).y), 1, (0,0,255), thickness=2) #draw a red circle for each point

    cv2.imshow("image", frame) 

    if cv2.waitKey(1) & 0xFF == 27: #Exit if esc
        break