from app import *

@app.route('/contactus',methods=['GET','POST'])
def contactus():
    if request.method=='POST':
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        user_input = {'name': name, 'email': email, 'subject': subject, 'message': message}
        db_contact.insert_one(user_input)
    return render_template("contactus.html")