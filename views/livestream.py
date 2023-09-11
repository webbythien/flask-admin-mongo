from adminlte.views import BaseAdminViewMongo
from wtforms.fields import HiddenField, FileField,StringField


class LivestreamView(BaseAdminViewMongo):
    column_editable_list = ['title', 'desc','view','status','name_galxe','link_galxe']
    column_searchable_list = ['title', 'desc','id']
    column_exclude_list = ['image','image_galxe']
    column_details_exclude_list = None
    column_filters = ['view','created']
    can_export = True
    can_view_details = False
    can_create = True
    can_edit = True
    can_delete = True
    edit_modal = True
    create_modal = True
    detaodal = False
    form_overrides = dict(background=HiddenField,image=FileField,image_galxe=FileField,image_galxe_url = HiddenField)
    column_labels = {
        'title': 'Title',
        'desc': 'Description',
        'view': 'View',  # Rename the 'view' column to 'View'
        'status': 'Status',
        'name_galxe': 'Name Galxe',
        'link_galxe': 'Link Galxe',
        'image_galxe_url':'Image Galxe'
    }
    form_args = {
    'desc': {
        'label': 'Description',
        },
    'name_galxe':{
        'label': 'Name Galxe',
    },
    'link_galxe':{
        'label': 'Link Galxe ',
    }
    }
    def get_query(self):
        # Customize the query to filter rows where status is True
        return super(LivestreamView, self).get_query().filter(status='live')
    