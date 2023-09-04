from flask_security import RoleMixin, UserMixin
from flask_mongoengine import MongoEngine 
from flask_login import current_user
from flask_security.utils import hash_password
from flask_security.utils import encrypt_password

admin_dbMongo = MongoEngine()

class RoleMongo(admin_dbMongo.Document,RoleMixin):
    name = admin_dbMongo.StringField(max_length=80, unique=True)
    description = admin_dbMongo.StringField(max_length=255)
    meta = {
        "collection": "roles" 
    }
    def __str__(self):
        return self.name

class UserMongo(admin_dbMongo.Document,UserMixin):
    first_name = admin_dbMongo.StringField(max_length=255)
    last_name = admin_dbMongo.StringField(max_length=255)
    email = admin_dbMongo.StringField(max_length=255, unique=True, required=True)
    password = admin_dbMongo.StringField(max_length=255, required=True)
    active = admin_dbMongo.BooleanField(default=True)
    roles = admin_dbMongo.ListField(admin_dbMongo.ReferenceField(RoleMongo), default=[])
    meta = {
        "collection": "users" 
    }
    def __str__(self):
        return f"{self.first_name} {self.last_name} <{self.email}>"
    
    def pre_save(self):
        """Perform checks or modifications before saving."""
        # You can add your custom checks or modifications here before saving
        self.password=encrypt_password(self.password)
        pass

    def save(self, *args, **kwargs):
        self.pre_save()  # Call the pre_save function before saving
        super().save(*args, **kwargs)
    @property
    def is_active(self):
        return self.active
    
    def get_id(self):
        return str(self.id)
    
    def is_authenticated(self):
        return current_user.is_authenticated
    def has_role(self, role_name):
        """Check if the user has a specific role."""
        return any(role.name == role_name for role in self.roles)
    