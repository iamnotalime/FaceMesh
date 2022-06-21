import cv2
import mediapipe as mp
import time

#First of all, we have to initialize the value of the fps first before going ahead to the next
cap = cv2.VideoCapture('Image/1.mp4')
pTime = 0
mpFaceMesh = mp.solutions.face_mesh
mpDraw = mp.solutions.drawing_utils
faceMesh = mpFaceMesh.FaceMesh(max_num_faces = 2)
drawSpec = mpDraw.DrawingSpec(thickness=2, circle_radius=5)

while True:
    success, img = cap.read()  
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACE_CONNECTIONS, drawSpec, drawSpec)

            for id,lm in enumerate(faceLms.landmark):
                # print(lm)
                ih, iw, ic = img.shape
                x, y = int(lm.x*iw), int(lm.y*ih)
                print(id,x,y)

    
    
    
    
    cTime = time.time()
    fps = 1 / (cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS:{int(fps)}', (20,70), cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 3)
    cv2.imshow("image", img)
    cv2.waitKey(1)
    