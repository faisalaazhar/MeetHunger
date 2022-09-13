from app import *


@app.route('/', methods=['GET', 'POST'])
def home():
    chef = 0
    user = 0
    for x in db_chef.find():
        chef = chef+1
    for x in db_x.find():
        user = user+1
    return render_template("home.html", chef=chef, user=user)
