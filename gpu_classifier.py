# %%
import tensorflow as tf 
from tensorflow import keras 
import numpy as np 
import matplotlib.pyplot as plt 
import cv2
from os import path 

# %%
datasets_folder = "/mnt/e/dataset/main_project/datasets"
elephant_dataset = path.join(datasets_folder,"elephant")
wild_board_dataset = path.join(datasets_folder,"wild_boar")
bird_dataset = path.join(datasets_folder,"bird")

print(elephant_dataset)
print(wild_board_dataset)
print(bird_dataset)

batch_size = 32
img_height = 180
img_width = 180

# %%
color_mode = "grayscale"
train_ds = keras.utils.image_dataset_from_directory(
    datasets_folder,
    validation_split=0.2,
    subset="training",
    seed=123,
    color_mode=color_mode,
    image_size=(img_height,img_width),
    batch_size=batch_size
)

# %%

val_ds = keras.utils.image_dataset_from_directory(
    datasets_folder,
    validation_split=0.2,
    subset="validation",
    seed=123,
    color_mode=color_mode,
    image_size=(img_height,img_width),
    batch_size=batch_size
)

# %%
class_names = train_ds.class_names 
print(class_names)
class_len = len(class_names)

plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
  for i in range(9):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(images[i].numpy().astype("uint8"))
    plt.title(class_names[labels[i]])
    plt.axis("off")






# %%
AUTOTUNE = tf.data.AUTOTUNE 
train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

# %%
model = keras.models.Sequential([
    keras.layers.Rescaling(1./255, input_shape=(img_height,img_width,1)),
    keras.layers.Conv2D(16,3, activation="relu"),
    keras.layers.MaxPooling2D(),
    keras.layers.Conv2D(32,3, activation="relu"),
    keras.layers.MaxPooling2D(),
    keras.layers.Conv2D(64,3, activation="relu"),
    keras.layers.MaxPooling2D(),
    keras.layers.Flatten(),
    keras.layers.Dense(128,activation='relu'),
    keras.layers.Dense(class_len)

])

model.compile(optimizer="adam",loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=['accuracy'])

model.summary()

# %%
epochs =  10
history = model.fit(train_ds,validation_data=val_ds,epochs=epochs , verbose=1)

# %%
acc = history.history['val_accuracy']
print(acc)
final_acc = acc[len(acc) - 1]

model.save(f"model-witgpu-{round(final_acc,4)}-(h-det).h5")

# %%
img = tf.keras.utils.load_img(
    "test/h1.png",
    target_size = (img_height,img_width),
    color_mode = color_mode 
)


img_array = tf.keras.utils.img_to_array(img)

img_array = tf.expand_dims(img_array, 0) # Create a batch
predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(f"animal : {class_names[0]} | accuracy :  {round(np.array(score)[0] * 100,2)}")
print(f"animal : {class_names[1]} | accuracy :  {round(np.array(score)[1] * 100,2)}")
print(f"animal : {class_names[2]} | accuracy :  {round(np.array(score)[2] * 100,2)}")
if len(class_names) > 3 :
    print(f"animal : {class_names[3]} | accuracy :  {round(np.array(score)[3] * 100,2)}")
plt.imshow(img)


# %%





