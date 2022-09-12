from app import *

otp = randint(000000,999999)

@app.route('/verify', methods=['GET','POST'])
def verify():
    msg_otp = ""
    username = session["username"]
    fullname = session["fullname"] 
    mobilenum = session["mobilenum"] 
    email = session["email"] 
    hashed = session["password"]
    role = "user"
    profile_pic = "https://bootdey.com/img/Content/avatar/avatar7.png"

    msg = Message('Verify Email-OTP',sender='meet.hunger479@gmail.com',recipients=[email])
    msg.body = str(otp)
    mail.send(msg)

    if request.method=='POST':
        userotp = request.form["otp"]

        if otp==int(userotp):
            msg_otp = "OTP Verified Successfully!"
        
            user_input = {'username': username, 'fullname': fullname, 'mobilenum': mobilenum, 'email': email, 'password': hashed, 'role': role, 'profile_pic': role}
            db_x.insert_one(user_input)
            session.pop("username", None)
            session.pop("fullname", None)
            session.pop("mobilenum", None)
            session.pop("email", None)
            session.pop("password", None)
            return redirect(url_for("login"))
        else:
            return "Wrong OTP"

    
    return render_template("otp.html")