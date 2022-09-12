from app import *

@app.route('/requestChef', methods=['GET','POST'])
def requestChef():
    if request.method=='POST':
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        date = request.form["date"]
        time = request.form["time"]
        skills = request.form["skills"]
        message = request.form["message"]
        skills.split(",")
        for x in db_chef.find():
            z = x["skill"]
            z.split(",")
            for i in z:
                for k in db_x.find({"username":x["username"]}):
                    mailll = k["email"]
                for j in skills:
                    if i==j:
                        msg = Message('want to be hired? ',sender='meet.hunger479@gmail.com',recipients=[mailll])
                        msg.body = "Your Skills macthes with "+name+" requirement Contact with "+email
                        mail.send(msg)
    return render_template("requestChef.html")
