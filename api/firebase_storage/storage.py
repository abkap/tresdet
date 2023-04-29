#storage initialization
from tkinter import Image
import numpy as np
import tensorflow as tf
from firebase_storage_defs import FirebaseStorage

    

# get_image()
firebase_storage = FirebaseStorage() 
img = firebase_storage.get_image_for_pil(url='dataset/1548774397/photo4.jpg')

# print(img)


model = tf.keras.models.load_model('m(e-15)-0.821-(h-det,ud).h5')
def get_animal_name(img : Image , model) : 
    class_names = ['bird', 'elephant', 'person', 'undetected', 'wild_boar']
    img_height , img_width , color_mode = 180,180,"grayscale"
    
    try : 
        img = img.convert('L')
        # img = img.rotate(270)
        # img.save("rotated.jpg")
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
    
    

result = get_animal_name(img,model)
print(result)

