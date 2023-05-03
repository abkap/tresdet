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
    
   