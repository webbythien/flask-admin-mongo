from adminlte.views import BaseAdminViewMongo


class VideoView(BaseAdminViewMongo):
    column_editable_list = None
    column_searchable_list = ['title', 'desc','id']
    column_exclude_list = ['host']
    column_details_exclude_list = None
    column_filters = ['view','created']
    can_export = True
    can_view_details = False
    can_create = False
    can_edit = False
    can_delete = True
    edit_modal = False
    create_modal = False
    details_modal = False
    column_labels = {
        'title': 'Title',
        'desc': 'Description',
        'view': 'View',  # Rename the 'view' column to 'View'
        'status': 'Status',
        'name_galxe': 'Name Galxe',
        'link_galxe': 'Link Galxe',
        'image_galxe_url':'Image Galxe'
    }
    def get_query(self):
        # Customize the query to filter rows where status is True
        return super(VideoView, self).get_query().filter(status='off').order_by('-created')