from adminlte.views import BaseAdminViewMongo
from wtforms.fields import HiddenField


class BannedWordView(BaseAdminViewMongo):
    column_editable_list = ['word']
    column_searchable_list = ['word']
    column_exclude_list = None
    column_details_exclude_list = None
    column_filters = None
    can_export = True
    can_view_details = False
    can_create = True
    can_edit = True
    can_delete = True
    edit_modal = True
    create_modal = True
    details_modal = False