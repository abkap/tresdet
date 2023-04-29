import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials




cred = credentials.Certificate("tresdet-firebase-adminsdk.json")
firebase_admin.initialize_app(cred, {
    'storageBucket' : "tresdet-478dd.appspot.com"
})

#firestore initilization
db = firestore.client()



# dealing with data 
coll_ref = db.collection(u'users')

# writing to db
def write_db():
    doc_ref = coll_ref.document(u'farmfield1').set({
        "animal" : "elephant" , 
        "time":"10.15AM 12/05/2024",
        "response"  : 'siren sound'
    })


# reading from db 
def print_db() : 
    docs = coll_ref.stream() 
    for doc in docs : 
        print(doc.to_dict())
