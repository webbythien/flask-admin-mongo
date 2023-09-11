from . import dbMongo
import datetime
from bson import ObjectId

class BannedMessages(dbMongo.Document):
    _id = dbMongo.ObjectIdField(primary_key=True,default=ObjectId)
    create_at= dbMongo.IntField(required=True,default=int(datetime.datetime.now().timestamp()))
    room_id= dbMongo.StringField(required=True)
    message = dbMongo.StringField(required=True)
    address = dbMongo.StringField(required=True)
    name=dbMongo.StringField()
    meta = {
        "collection": "banned_message",# Replace with your desired collection name
    }
    
    