from flask_admin import AdminIndexView
from flask_admin import expose, AdminIndexView
from flask import redirect

class MyView(AdminIndexView):

    def is_visible(self):
        # This view won't appear in the menu structure
        return False

    @expose('/')
    def index(self):
        return redirect("/admin/livestream")