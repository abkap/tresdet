# importing libraries
import cv2
import numpy as np
count = 1 
# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture("./elephant-attack.mp4")
SAVE_DIR = './intruding_elephant'
# Check if camera opened successfully
if (cap.isOpened()== False):
    print("Error opening video file")
  
# Read until video is completed
while(cap.isOpened()):
      
# Capture frame-by-frame
    ret, frame = cap.read()
    #writing to folder 
    cv2.imwrite(f'{SAVE_DIR}/e-{count}.jpg',frame)
    if ret == True:
    # Display the resulting frame
        cv2.imshow('Frame', frame)
          
    # Press Q on keyboard to exit
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
  
# Break the loop
    else:
        break
    count += 1
  
# When everything done, release
# the video capture object
cap.release()
  
# Closes all the frames
cv2.destroyAllWindows()