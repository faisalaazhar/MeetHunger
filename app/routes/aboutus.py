from app import *

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")