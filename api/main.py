from fastapi import FastAPI 
from pydantic import BaseModel 
import tensorflow as tf 
import numpy as np 
from PIL import Image
import io
import base64
import json

from firebase_storage.firebase_storage_defs import FirebaseStorage

#predefined 
model = tf.keras.models.load_model('./m-esp32(u-1,e-35)-0.8437-(h-det,ud)(added-bird-datas).h5')

#initializations 
firebase_storage = FirebaseStorage()

def get_animal_name(img_location : str , model) : 
    class_names = ['bird', 'elephant', 'person', 'undetected', 'wild_boar']
    img_height , img_width , color_mode = 180,180,"grayscale"
    
    try : 
        
        img = firebase_storage.get_image_for_pil(url=img_location).convert('L')
        img = img.rotate(270)
        img = img.resize((img_height,img_width))
        img_array = np.array(img)
  
        img_array = tf.expand_dims(img_array, 0) # Create 
        predictions = model.predict(img_array)
        score = predictions[0]

        print(predictions[0])

        print(f"animal : {class_names[0]} | accuracy :  {round(np.array(score)[0] * 100,2)}")
        print(f"animal : {class_names[1]} | accuracy :  {round(np.array(score)[1] * 100,2)}")
        print(f"animal : {class_names[2]} | accuracy :  {round(np.array(score)[2] * 100,2)}")
        if len(class_names) > 3 :
            print(f"animal : {class_names[3]} | accuracy :  {round(np.array(score)[3] * 100,2)}")
        if len(class_names) > 4 :
            print(f"animal : {class_names[4]} | accuracy :  {round(np.array(score)[4] * 100,2)}")
        # plt.imshow(img)
        animal_detected_index  = np.argmax(score)
        animal_detected_score = np.max(score)
        animal_detected = class_names[animal_detected_index]
        print("animal detected is " , animal_detected , " with socre " , animal_detected_score)

        return {
            "AnimalName" : animal_detected, 
            "Accuracy": animal_detected_score, 
            "response" : "siren"
        }
    except Exception as e : 
        print(e)
        return {
            "status" : "Error occured",
            "exception" : str(e)
        }




app = FastAPI()
class Item(BaseModel) : 
    FarmFeildId : int
    CameraId : int
    CaptureCount : int  
    ImageLocation : str

@app.get("/") 
def root() : 
    return {
        "Company" : "TresDet" , 
        "Status" : "working perfectly"
    }


@app.post("/detect") 
def detect_image(cam_data : Item): 
    result = get_animal_name(cam_data.ImageLocation, model)
    print(type(result))
    result = json.dumps(str(result))
    return result

    

