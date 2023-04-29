import firebase_admin
from firebase_admin import credentials,storage
from PIL import Image
import io

class FirebaseEssentials : 
    def __init__(self) -> None:
        cred = credentials.Certificate("tresdet-firebase-adminsdk.json")
        firebase_admin.initialize_app(cred, {
        'storageBucket' : "tresdet-478dd.appspot.com"
})


class FirebaseStorage(FirebaseEssentials) :
    def __init__(self) -> None:
        super().__init__()
        self.bucket = storage.bucket()

    
    def save_image(self):
        IMAGE_URL = 'data/photo.jpg'
        blob = self.bucket.blob(IMAGE_URL)
        try:
            content = blob.download_as_string()
            print(type(content))
            img_stream = io.BytesIO(content)
            img = Image.open(img_stream)
            img.save("captured.jpg")
            print(img.size)
            return "image saved successfully"
        except Exception as e: 
            print("error in downlaoding  \n\n",e)
            pass
    def get_image_for_pil(self, url : str) -> Image :
        # IMAGE_URL = 'data/photo.jpg'
        blob = self.bucket.blob(url)
        try:
            content = blob.download_as_string()
            print(type(content))
            img_stream = io.BytesIO(content)
            img = Image.open(img_stream)
            print(img.size)
            return img
        except Exception as e : 
             print(e)
             return None
    
    # To download image as file
    # Only for developement purpose 
    def download_image(self,url : str) -> None : 
        blobs = self.bucket.list_blobs()
        print(blobs , type(blobs))
        for i,blob in enumerate(blobs) : 
            blob.download_to_filename(f'downloaded/{i}.jpg')
            print(blob.name)
        # blobs.download_to_file('downloaded/')
        print('finished')