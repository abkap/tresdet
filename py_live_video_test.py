# %%
import tensorflow as tf 
import matplotlib.pyplot as plt 
import cv2 
import numpy as np 
import os 
import time 

# %%
VIDEO_LINK = 'elephant-attack.mp4'
# class_names = ['bird', 'elephant', 'person', 'wild_boar']
class_names = ['bird', 'elephant', 'person', 'undetected', 'wild_boar']

img_height , img_width , color_mode = 180,180,"grayscale"
# model = tf.keras.models.load_model('./trained_models/model-0.8748-(h-det).h5')
# model = tf.keras.models.load_model("./m(e-15)-0.821-(h-det,ud).h5")
model = tf.keras.models.load_model("./m(e-15)-0.821-(h-det,ud).h5")

# %%
def detect_animal(frame) : 
    # print(frame.shape)
    img_array = np.array(frame)
    img_array = cv2.resize(img_array,(img_width,img_height))
    img_array = cv2.cvtColor(img_array,cv2.COLOR_BGR2GRAY)
    img_array = tf.expand_dims(img_array, 0)
    # print(img_array.shape)

    predictions = model.predict(img_array)
    score = predictions[0]
    prediction_animal = class_names[score.argmax()]
    prediction_percent = np.max(score)
    # print(prediction_animal , prediction_percent)
    return prediction_animal,prediction_percent

# %%
video = cv2.VideoCapture(VIDEO_LINK)
fps = int(video.get(cv2.CAP_PROP_FPS))
frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
print(round(frames/fps))
print(fps)
fcount = 1
seconds = 0 
while True : 
    ret,frame  = video.read()
    if ret :
        cv2.imshow('frame', frame)
        if fcount % fps == 0 :  # for each  seconds 
            animal , confidence = detect_animal(frame)
            print(animal,confidence)
            print(seconds)
            seconds += 1
        
      

        if cv2.waitKey(fps) == ord('q') : 
            break

        
        fcount += 1
        # print(seconds)
    
    else : 
        break 



