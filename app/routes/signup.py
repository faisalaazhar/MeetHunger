from app import *

@app.route('/signup',methods=['GET','POST'])
def signup():
    message = ''

    if request.method=='POST':
        username = request.form["username"]
        fullname = request.form["fullname"]
        mobilenum = request.form["mobilenum"]
        email = request.form["email"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        
        if " " in username:
            message = 'Username should not have any space'
            return message  

        user_found = db_x.find_one({"username": username})
        email_found = db_x.find_one({"email": email})
        if user_found:
            message = 'There already is a user by that name'
            return message
            #return render_template('index.html', message=message)
        elif email_found:
            message = 'This email already exists in database'
            return message
            #return render_template('index.html', message=message)
        elif password1 != password2:
            message = 'Passwords should match!'
            return message
            #return render_template('index.html', message=message)
        else:
            hashed = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())
            session["username"] = username
            session["fullname"] = fullname
            session["mobilenum"] = mobilenum
            session["email"] = email
            session["password"] = hashed
            return redirect(url_for("verify"))

    return render_template("signup.html")