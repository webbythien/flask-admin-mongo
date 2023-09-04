from adminlte.views import BaseAdminViewMongo
from wtforms.fields import HiddenField, FileField,StringField


class LivestreamView(BaseAdminViewMongo):
    column_editable_list = ['title', 'desc','view','status']
    column_searchable_list = ['title', 'desc','id']
    column_exclude_list = ['image']
    column_details_exclude_list = None
    column_filters = ['view','created']
    can_export = True
    can_view_details = False
    can_create = True
    can_edit = True
    can_delete = True
    edit_modal = True
    create_modal = True
    details_modal = False
    form_overrides = dict(background=HiddenField,image=FileField)
    form_args = {
    'desc': {
        'label': 'Description',
    }
    }
    def get_query(self):
        # Customize the query to filter rows where status is True
        return super(LivestreamView, self).get_query().filter(status='live')
    