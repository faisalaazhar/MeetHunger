from app import *

app.config['UPLOAD_FOLDER'] = '../static/img/'
app.config['SECRET_KEY'] = 'supersecretkey'


class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")


@app.route('/addblog', methods=['GET', 'POST'])
def addblog():
    blogg = dict()
    blog_pic = randint(00000000, 99999999)
    fname = ""
    if "username" in session:
        form = UploadFileForm()
        if form.validate_on_submit():
            file = form.file.data  # First grab the file
            file.filename = str(blog_pic)+".jpg"
            file.save(os.path.join(os.path.abspath(os.path.dirname(
                __file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))  # Then save the file
            fname = file.filename
            blogg["blog_pic"] = fname
            return render_template("addblog.html", form=form, fname=fname)
        if request.method == 'POST':
            title = request.form["title"]
            des = request.form["descrp"]
            blogg["title"] = title
            blogg["des"] = des
            blogg["blog_pic"] = str(blog_pic)+".jpg"
            blogg["username"] = session["username"]
            db_blog.insert_one(blogg)
            return redirect(url_for("blog"))
    else:
        return redirect(url_for("login"))
    return render_template("addblog.html", form=form)


@app.route('/blog', methods=['GET', 'POST'])
def blog():
    title = []
    des = []
    blog_pic = []
    cnt = 0
    username = []
    for z in db_blog.find():
        title.append(z["title"])
        des.append(z["des"])
        blog_pic.append(z["blog_pic"])
        username.append(z["username"])
        cnt += 1
        # x["blog_pic"]=z["blog_pic"]
    return render_template("blog.html", cnt=cnt, title=title, des=des, blog_pic=blog_pic, username=username)


@app.route('/showblog/<string:s>', methods=['GET', 'POST'])
def showSingleblog(s):
    x = db_blog.find_one({"blog_pic": s})
    return render_template("singleBlog.html", **locals())
