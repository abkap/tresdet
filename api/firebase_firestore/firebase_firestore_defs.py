import firebase_admin
from firebase_admin import credentials,firestore

class FirebaseEssentials : 
    def __init__(self) -> None:
        cred = credentials.Certificate("tresdet-firebase-adminsdk.json")
        firebase_admin.initialize_app(cred, {
        'storageBucket' : "tresdet-478dd.appspot.com"
})

class FirebaseFirestore(FirebaseEssentials) : 
    def __init__(self) -> None:
        super().__init__()
        #other 
        self.db = firestore.client() 

    def write_data(self,data : dict) :
        self.db.collection('users').add(data)


firebase_instance = FirebaseFirestore() 
