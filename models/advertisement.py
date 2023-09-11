from . import dbMongo
import datetime
from bson import ObjectId
from utils.upload_s3 import upload_image_url
from flask import flash,get_flashed_messages

class Advertisement(dbMongo.Document):
    _id = dbMongo.ObjectIdField(primary_key=True,default=ObjectId)
    image = dbMongo.StringField()
    image_url = dbMongo.StringField()
    link = dbMongo.StringField(required=True)
    created= dbMongo.IntField(required=True,default=int(datetime.datetime.now().timestamp()))
    meta = {
        "collection": "advertisement",# Replace with your desired collection name
         "id_field": "_id" 
    }

    def save(self, *args, **kwargs):
        try:
            liveObjChekc = Advertisement.objects(_id = self._id).first()
            if liveObjChekc is None:
                if self.image.filename =='':
                    raise ValueError("Image is required")
                #func save and get image from s3
                url = upload_image_url(self.image,str(self._id))
                # self.image =None
                self.image_url = url
                self._fields['image'].required = False
                self._data.pop('image', None)
                self.image = None
                super(Advertisement, self).save(*args, **kwargs)
            else:
                if self.image.filename !='':
                    url = upload_image_url(self.image,str(self._id))
                    self.image_url = url
                self.image = None
                self._data.pop('image', None)
                super(Advertisement, self).save(*args, **kwargs)

        except Exception as e:
            messages = get_flashed_messages(with_categories=True)
            for category, _ in messages:
                flash('', category)
            flash(f'An error occurred: {str(e)}', 'error')
            return str(e)