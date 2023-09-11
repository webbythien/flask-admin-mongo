from adminlte.views import BaseAdminViewMongo
from wtforms.fields import HiddenField
from flask_admin.actions import action
from flask_admin.model.template import EndpointLinkRowAction
from models.bannedMessage import BannedMessages 
from bson.objectid import ObjectId
from flask import flash,get_flashed_messages
from utils.redis import append_struct_to_array
import traceback
import json



class BannedMessageView(BaseAdminViewMongo):
    column_editable_list = None
    column_searchable_list = ['room_id','message','address','name']
    column_exclude_list = None
    column_details_exclude_list = None
    column_filters = ['create_at']
    can_export = True
    can_view_details = False
    can_create = False
    can_edit = False
    can_delete = True
    edit_modal = False
    create_modal = False
    details_modal = False
    form_overrides = dict(create_at=HiddenField)
    column_labels = {
    'create_at': 'Created At',
    }
    form_args = {
    'create_at': {
        'label': 'Created At',
        }
    }

    @action('unban', 'Unban', 'Are you sure you want to unban selected messages?')
    def action_unban(self, ids):
        try:
            query = BannedMessages.objects(_id__in=ids)
            for unbanMessage in query:
                unbanMessageJson = {
                    "id": str(unbanMessage._id),
                    "room_id": unbanMessage.room_id,
                    "create_at":unbanMessage.create_at,
                    "message": unbanMessage.message,
                    "address": unbanMessage.address
                }
                json_data = json.dumps(unbanMessageJson)

                append_struct_to_array(unbanMessage.room_id,json_data)
                query.delete()
            pass
        except Exception as e:
            traceback.print_exc()

            messages = get_flashed_messages(with_categories=True)
            flash(f'An error occurred: {str(e)}', 'error')
    def get_query(self):
        # Customize the query to filter rows where status is True
        return super(BannedMessageView, self).get_query().order_by('-create_at')    
