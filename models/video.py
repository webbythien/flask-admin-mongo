from . import dbMongo
import datetime
from bson import ObjectId



class Video(dbMongo.Document):
    title = dbMongo.StringField(required=True, max_length=255)
    desc = dbMongo.StringField(required=True)
    background = dbMongo.StringField(required=True)
    view = dbMongo.IntField(default=0)
    id= dbMongo.StringField(required=True,unique=True)
    status = dbMongo.StringField(default='off',required=True,choices=[('live', 'live'), ('off', 'off')])
    host = dbMongo.StringField(required=True,default='Lido')
    created= dbMongo.IntField(required=True,default=int(datetime.datetime.now().timestamp()))
    _id = dbMongo.ObjectIdField(primary_key=True,default=ObjectId)  # Trường _id
    meta = {
        "collection": "videos",# Replace with your desired collection name
         "id_field": "_id" 
    }
    
    