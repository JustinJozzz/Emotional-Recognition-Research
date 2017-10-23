import dlib
import cv2
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
import numpy as np
import math

emotions = ["Anger", "Disgust", "Fear", "Happiness", "Neutral", "Sadness", "Surprise"]
video_capture = cv2.VideoCapture(0) #start webcam on a new thread
video_capture.set(3, 562);
video_capture.set(4, 762);
detector = dlib.get_frontal_face_detector() #Face detector
#emotionSVM = SVC(kernel='linear', probability=True, tol=1e-3)
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") #get pre trained model
emotionRF = joblib.load("EmotionRF.pkl")

data = {} 

def make_detections(image):
    detections = detector(image, 1)
    for k,d in enumerate(detections):
        shape = predictor(image, d) 
        for i in range(1,68): 
            cv2.circle(frame, (shape.part(i).x, shape.part(i).y), 1, (0,0,255), thickness=2) #draw a red circle for each point
        xlist = []
        ylist = []
        for i in range(1,68): 
            xlist.append(float(shape.part(i).x))
            ylist.append(float(shape.part(i).y))
            
        xmean = np.mean(xlist)
        ymean = np.mean(ylist)
        xcentral = [(x-xmean) for x in xlist]
        ycentral = [(y-ymean) for y in ylist]

        landmarks_vectorised = []
        for x, y, w, z in zip(xcentral, ycentral, xlist, ylist):
            landmarks_vectorised.append(w)
            landmarks_vectorised.append(z)
            meannp = np.asarray((ymean,xmean))
            coornp = np.asarray((z,w))
            dist = np.linalg.norm(coornp-meannp)
            landmarks_vectorised.append(dist)
            landmarks_vectorised.append(int(math.atan((y-ymean)/(x-xmean))*360/math.pi))

        data['landmarks_vectorised'] = landmarks_vectorised
    if len(detections) >= 1: 
        training_data = []
        training_data.append(data['landmarks_vectorised'])
        npar_train = np.array(training_data)
        rawProbs = emotionRF.predict_proba(npar_train)
        rawProbs = rawProbs.flatten().tolist()

        for i, x in enumerate(rawProbs):
            cv2.putText(frame, emotions[i]+": "+str(round(x*100, 2)) + "%", (0, (i+1)*20), cv2.FONT_HERSHEY_SIMPLEX, .5, 255 if not x == max(rawProbs) else (0,128,0))
    

while True:
    #frame = cv2.imread('./dataset/Happiness/IMG_0776.jpg')
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    clahe_image = clahe.apply(gray)

    make_detections(clahe_image)

    cv2.imshow("image", frame) 

    if cv2.waitKey(1) & 0xFF == 27: #Exit if esc
        break