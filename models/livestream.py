from . import dbMongo
import datetime
from bson import ObjectId
from utils.upload_s3 import upload_file,get_file
from flask import flash,get_flashed_messages
class Livestream(dbMongo.Document):
    title = dbMongo.StringField(required=True, max_length=255)
    desc = dbMongo.StringField(required=True)
    background = dbMongo.StringField()
    view = dbMongo.IntField(default=0)
    id= dbMongo.StringField(required=True,unique=True)
    status = dbMongo.StringField(default='live',required=True,choices=[('live', 'live'), ('off', 'off')])
    host = dbMongo.StringField(required=True,default='Lido')
    created= dbMongo.IntField(required=True,default=int(datetime.datetime.now().timestamp()))
    _id = dbMongo.ObjectIdField(primary_key=True,default=ObjectId)  # Trường _id
    image = dbMongo.StringField()
    meta = {
        "collection": "videos",# Replace with your desired collection name
         "id_field": "_id" 
    }

    def save(self, *args, **kwargs):
        try:
            liveObjChekc = Livestream.objects(_id = self._id).first()
            if liveObjChekc is None:
                if self.image.filename =='':
                    raise ValueError("Image is required")
                #func save and get image from s3
                new_filename = upload_file(self.image, self.id)
                url = get_file(new_filename,3600)

                # self.image =None
                self.background = url
                self._fields['image'].required = False
                self._data.pop('image', None)
                self.image = None
                # --------------------------------------------------------

                if self._id is None:
                    super(Livestream, self).save(*args, **kwargs)
                    return
                else:
                    liveTempObj = Livestream.objects(status='live').first()
                    Livestream.objects(status='live').update(status='off')
                    try:
                        super(Livestream, self).save(*args, **kwargs)
                    except Exception as e:
                        Livestream.objects(_id = liveTempObj._id).update(status='live')
                        flash(f'An error occurred: {str(e)}', 'error')
            else:
                if self.image.filename !='':
                    new_filename = upload_file(self.image, self.id)
                    url = get_file(new_filename,3600)
                self._data.pop('image', None)
                super(Livestream, self).save(*args, **kwargs)

        except Exception as e:
            messages = get_flashed_messages(with_categories=True)
            for category, _ in messages:
                flash('', category)
            flash(f'An error occurred: {str(e)}', 'error')
            return str(e)
            