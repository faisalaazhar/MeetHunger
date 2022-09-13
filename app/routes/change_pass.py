from app import *


@app.route('/change_pass', methods=['GET', 'POST'])
def change_pass():

    if request.method == 'POST':

        password = request.form["password"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]

        if password1 != password2:
            return "both new password should be same"

        username = session["username"]
        id_x = db_x.find_one({'username': username})
        passcheck = id_x['password']

        if bcrypt.checkpw(password.encode('utf-8'), passcheck):
            hashed = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())
            db_x.update_one({'_id': id_x['_id']}, {
                            "$set": {"password": hashed}})
            return redirect("/login")
        else:
            return "old password don't match"

    return render_template("change_pass.html")
