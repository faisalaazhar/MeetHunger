from app import *

@app.route('/login', methods=['GET','POST'])
def login():
    
    if request.method=='POST':
        username = request.form["username"]
        password = request.form["password"]

        name_found = db_x.find_one({'username':username})
        if name_found:
            name = name_found['username']
            passcheck = name_found['password']

            if bcrypt.checkpw(password.encode('utf-8'), passcheck):
                session["username"] = name
                return redirect(url_for("home"))
            else:
                if "username" in session:
                    return name+"123"
                return "Wrong Password"
        else:
            return "username not found"
    return render_template("login.html")