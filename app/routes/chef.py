from pydoc import describe
from app import *


@app.route('/joinaschef', methods=['GET', 'POST'])
def joinaschef():
    if "username" in session:
        if request.method == 'POST':
            city = request.form["city"]
            skill = request.form["skills"]
            location = request.form["location"]
            workex = request.form["workex"]
            description = request.form["description"]

            chef = dict()
            chef["username"] = session["username"]
            chef["city"] = city
            chef["skill"] = skill
            chef["location"] = location
            chef["workex"] = workex
            chef["description"] = description
            db_chef.insert_one(chef)
            return redirect("/findachef/"+session["username"])
        return render_template("joinaschef.html")
    else:
        return redirect(url_for("login"))


@app.route('/findachef/<string:s>', methods=['GET', 'POST'])
def findchefbycity(s):
    x = db_x.find_one({"username": s})
    y = db_chef.find_one({"username": s})
    return render_template("contact_chef.html", x=x, y=y)


@app.route('/findachef', methods=['GET', 'POST'])
def findachef():
    if "username" in session:
        if request.method == 'POST':
            city = request.form["city"]
            name = []
            skill = []
            location = []
            description = []
            cnt = 0
            for x in db_chef.find({'city': city}):
                name.append(x["username"])
                skill.append(x["skill"])
                location.append(x["location"])
                description.append(x["description"])
                cnt = cnt+1
            return render_template("findchefbycity.html", city=city, name=name, skill=skill, location=location, description=description, cnt=cnt)
        name = []
        skill = []
        location = []
        description = []
        city = []
        cnt = 0
        for x in db_chef.find():
            name.append(x["username"])
            skill.append(x["skill"])
            location.append(x["location"])
            description.append(x["description"])
            city.append(x["city"])
            cnt = cnt+1
        return render_template("chefs.html", city=city, name=name, skill=skill, location=location, description=description, cnt=cnt)
    else:
        return redirect(url_for("login"))
