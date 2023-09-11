from . import dbMongo
import datetime
from flask import flash,get_flashed_messages
from utils.redis import append_struct_to_array
from bson import ObjectId



class BannedWord(dbMongo.Document):
    _id = dbMongo.ObjectIdField(primary_key=True,default=ObjectId)
    word = dbMongo.StringField(required=True, max_length=255,unique=True)
    meta = {
        "collection": "banned_words",# Replace with your desired collection name
    }
    
    def save(self, *args, **kwargs):
        try:
            append_struct_to_array("banned_words",str(self.word))
            super(BannedWord, self).save(*args, **kwargs)
        except Exception as e:
            messages = get_flashed_messages(with_categories=True)
            for category, _ in messages:
                flash('', category)
            flash(f'An error occurred: {str(e)}', 'error')
            return str(e)
 