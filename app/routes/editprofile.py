from app import *

app.config['UPLOAD_FOLDER'] = '../static/img/'
app.config['SECRET_KEY'] = 'supersecretkey'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/editprofile', methods=['GET','POST'])
def editprofile():

    username = session["username"]
    id_x = db_x.find_one({'username':username})
    fname = id_x["profile_pic"]

    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        file.filename = id_x["username"]
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        fname=file.filename
        db_x.update_one({'_id':id_x['_id']}, {"$set" : {"profile_pic" :fname}})
        return render_template('editprofile.html', form=form,fname=fname)
    
    if request.method=='POST':
        fullname = request.form["fullname"]
        email = request.form["email"]
        mobilenum = request.form["mobilenum"]

        db_x.update_one({'_id':id_x['_id']}, {"$set" : {"fullname" :fullname}})
        db_x.update_one({'_id':id_x['_id']}, {"$set" : {"email" :email}})
        db_x.update_one({'_id':id_x['_id']}, {"$set" : {"mobilenum" :mobilenum}})
    return render_template("editprofile.html",form=form,fname=fname)