from flask import Flask, url_for, redirect, flash,jsonify, request
from flask_migrate import Migrate
from flask_security import Security
from flask_admin import helpers as admin_helpers
from adminlte.admin import AdminLte,admin_db_store
from flask_admin import menu
from flask_security.utils import encrypt_password
from views.livestream import LivestreamView
from views.myview import MyView
from models.livestream import Livestream
from models.video import Video
from views.video import VideoView
from flask import Flask, url_for, redirect, request
from flask_migrate import Migrate
from flask_security import Security, login_required, current_user
from flask_security.utils import verify_password, encrypt_password
from flask_admin import helpers as admin_helpers
from adminlte.admin import AdminLte, admin_db_store
from models import dbMongo
import pytube

app = Flask(__name__)
app.config.from_pyfile('config.py')


dbMongo.init_app(app)

migrate = Migrate(app, dbMongo)
admin_migrate = Migrate(app, dbMongo)

@app.get("/")
def index():
    # print(encrypt_password("admin"))
    return redirect("/admin/livestream")

security = Security(app, admin_db_store)
admin = AdminLte(app, skin = 'green', name = 'LidoAdmin', index_view= MyView(), short_name = "<b>L</b>D", long_name = "<b>Lido</b>Admin")

admin.set_category_icon(name = 'Livestream', icon_value ='fa-video-camera')

admin.add_view(LivestreamView(Livestream, name = "Streaming", category="Livestream", menu_icon_value = 'fa-eye'))
admin.add_view(VideoView(Video, name = "Video", category="Livestream", menu_icon_value = 'fa-youtube-play'))



@security.context_processor
def security_context_processor():
    print(encrypt_password('admin'))
    return dict(
        admin_base_template = admin.base_template,
        admin_view = admin.index_view,
        h = admin_helpers,
        get_url = url_for
    )

@app.route('/change_password', methods=['POST'])
@login_required
def change_password():
    if request.method == 'POST':
        current_password = request.form.get('password')
        new_password = request.form.get('new_password')
        if verify_password(current_password, current_user.password):
            # Update the user's password in MongoEngine
            current_user.password = new_password
            current_user.save()
            flash('Password changed successfully', 'success')
        else:
            flash('Current password is incorrect', 'error')
    return redirect(url_for("index"))

#api for yotube link
@app.route('/get_video_info', methods=['POST'])  # Chuyển sang phương thức POST
def get_video_info():
    data = request.get_json()  # Lấy dữ liệu từ phần thân (body) của yêu cầu
    video_url = data.get('url')  # Lấy URL từ dữ liệu JSON

    try:
        yt = pytube.YouTube(video_url)
        video_info = {
            'title': yt.title,
            'views': yt.views,
            'thumbnail': yt.thumbnail_url,
            "description":yt.description,
            "author":yt.author,
        }
        print(yt.description)
        return jsonify(video_info), 200
    except Exception as e:
        error_message = str(e)
        return jsonify({'error': error_message}), 400
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5009)
    
