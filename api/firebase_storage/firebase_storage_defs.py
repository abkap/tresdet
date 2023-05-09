
from firebase_admin import storage
from PIL import Image
import io
import firebase_admin 
from firebase_admin import credentials

class FirebaseEssentials : 
    def __init__(self) -> None:
        if not firebase_admin._apps :
            cred = credentials.Certificate("tresdet-firebase-adminsdk.json")
            firebase_admin.initialize_app(cred, {
            'storageBucket' : "tresdet-478dd.appspot.com"
})


class FirebaseStorage(FirebaseEssentials) :
    def __init__(self) -> None:
        super().__init__()
        self.bucket = storage.bucket()

    def get_image_for_pil(self, url : str) -> tuple[bool, str] : 
        # IMAGE_URL = 'data/photo.jpg'
        blob = self.bucket.blob(url)
        blob.make_public() 
        print(blob.public_url)
        try:
            content = blob.download_as_string()
            print(type(content))
            img_stream = io.BytesIO(content)
            img = Image.open(img_stream)
            print(img.size)
            return img , blob.public_url 
        except Exception as e : 
             print(e)
             return None , None
    
   