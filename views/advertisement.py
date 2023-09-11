from adminlte.views import BaseAdminViewMongo
from wtforms.fields import HiddenField, FileField


class AdvertisementView(BaseAdminViewMongo):
    column_editable_list = ['link']
    column_searchable_list = ['link']
    column_exclude_list = ['image']
    column_details_exclude_list = None
    column_filters = None
    can_export = True
    can_view_details = False
    can_create = True   
    can_edit = True
    can_delete = True
    edit_modal = True
    create_modal = True
    detaodal = False
    form_overrides = dict(image_url=HiddenField,created=HiddenField,image=FileField)
    def get_query(self):
        # Customize the query to filter rows where status is True
        return super(AdvertisementView, self).get_query().order_by('-created')
    