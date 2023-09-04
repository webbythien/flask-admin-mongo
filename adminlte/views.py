from flask import url_for, redirect, request, abort
from flask_admin import menu
from flask_login import current_user


class FaLink(menu.MenuLink):

    def __init__(self, name, url = None, endpoint = None, category = None, class_name = None, icon_type = "fa",
                 icon_value = None, target = None):
        super(FaLink, self).__init__(name, url, endpoint, category, class_name, icon_type, icon_value, target)


#########-----------------------------------------

from flask_admin.contrib.mongoengine import ModelView as MongoModelView

class FaLinkMongo(menu.MenuLink):

    def __init__(self, name, url=None, endpoint=None, category=None, class_name=None, icon_type="fa",
                 icon_value=None, target=None):
        super(FaLink, self).__init__(name, url, endpoint, category, class_name, icon_type, icon_value, target)
        

class FaModelViewMongo(MongoModelView):

    def __init__(self, model, name=None, category=None, endpoint=None, url=None, static_folder=None,
                 menu_class_name=None, menu_icon_type="fa", menu_icon_value=None):
        super(FaModelViewMongo, self).__init__(model, name, category, endpoint, url, static_folder, menu_class_name,
                                          menu_icon_type, menu_icon_value)
        

class BaseAdminViewMongo(FaModelViewMongo):
    required_role = 'admin'
    can_export = True
    can_view_details = True
    can_create = True
    can_edit = True
    can_delete = True
    edit_modal = True
    create_modal = True
    details_modal = True

    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False

        if current_user.has_role(self.required_role):
            return True

        return False

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            if current_user.is_authenticated:
                abort(403)
            else:
                return redirect(url_for('security.login', next = request.url))


class AdminsViewMongo(BaseAdminViewMongo):
    required_role = 'superadmin'
    column_editable_list = ['email', 'first_name', 'last_name']
    # column_searchable_list = ['roles', 'email', 'first_name', 'last_name']
    column_searchable_list = ['email', 'first_name', 'last_name']
    column_exclude_list = ['password']
    column_details_exclude_list = ['password']
    column_filters = ['email', 'first_name', 'last_name']
    can_export = True
    can_view_details = True
    can_create = True
    can_edit = True
    can_delete = True
    edit_modal = True
    create_modal = True
    details_modal = True