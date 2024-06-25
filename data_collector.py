import cv2
import os
import time 
import uuid


IMAGE_PATH="collected_image"

labels=["Hello","Yes","No",'Thanks',"Please"]

number_of_images=5

for label in labels:
    img_path=os.path.join(IMAGE_PATH,label)

    os.makedirs(img_path)


    #open_camera
    cap=cv2.VideoCapture(0)

    print(f'collecting image for {label}')

    time.sleep(5)

    for imgnum in range(number_of_images):
        ref, frame =cap.read()

        imagename=os.path.join(IMAGE_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename,frame)
        cv2.imshow('frame',frame)
        time.sleep(4)


        if cv2.waitKey(1) & 0xFF==ord('q'):
            break

    
    cap.release()