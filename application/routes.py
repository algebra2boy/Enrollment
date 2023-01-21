from application import app, db
from flask import Response, render_template, request,json, redirect, flash, url_for # use to render html file and pass data 
from application.forms import LoginForm, RegisterForm 
from application.model import User, Course, Enrollment

courseData = [{"courseID":"1111","title":"CS 453","description":"Networks","credits":"3","term":"Fall, Spring"}, 
                 {"courseID":"2222","title":"CS 589","description":"Machine Learning","credits":"3","term":"Spring"}, 
                 {"courseID":"3333","title":"CS 326","description":"Web Design","credits":"4","term":"Fall"}, 
                 {"courseID":"4444","title":"Math 545","description":"Linear Algebra for Applied Mathematics","credits":"3","term":"Fall, Spring"}, 
                 {"courseID":"5555","title":"Music 150","description":"Lively Arts","credits":"4","term":"Fall"}]

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True)

@app.route("/courses/")
@app.route("/courses/<term>")
def courses(term = "Spring 2020"):
    # pass data from python to the html view
    return render_template("courses.html", courseData=courseData, course = True, term = term)

@app.route("/register", methods = ["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user_id  = User.objects.count() # find the total count of user
        user_id  += 1   

        email       = form.email.data
        password    = form.password.data
        first_name  = form.first_name.data
        last_name   = form.last_name.data
        print(user_id, email, password, first_name, last_name)
        # setting up a user with hashed password and then save it 
        user = User(user_id=user_id, email=email, first_name=first_name, last_name=last_name)
        user.set_hash_password(password=password)
        user.save()
        flash(f"{first_name} is successfully registered", "success")
        return redirect('/index')

    return render_template("register.html", register=True, register_form = form, title = "New User Registration")

@app.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()

    # if submit button is being pressed
    if form.validate_on_submit():

        # validate user's email and passsword
        email = form.email.data
        password = form.password.data
        # retrieve the first object in the User array 
        user = User.objects(email=email).first()

        if user and user.password == password:
            flash(f"{user.first_name} have successfully logged in!!", "success")
            return redirect('/index')
        else: 
            flash("Your email is not found in the database", "danger")
    return render_template("login.html", login=True, login_form = form, title = "Login")

@app.route("/enrollment", methods = ["GET", "POST"])
def enrollment():
    # print(request.args)
    # request.args.get('courseID') -> use this if we only using GET
    courseID = request.form.get('courseID')
    title = request.form.get('title')
    term = request.form.get('term')

    course_data = {"id": courseID,
                            "title": title,
                            "term": term}

    return render_template("enrollment.html", 
                            enrollment=True,
                            course_data = course_data)

@app.route("/api/")
@app.route("/api/<id>")
def api(id=None):
    if id == None:
        json_data = courseData
    else: 
        json_data = {"error": "course does not exist"}
        for course in courseData:
            if course['courseID'] == id:
                json_data = course
                break
            
    # can use contentype as sell
    return Response(json.dumps(json_data),
                    mimetype="application/json")



@app.route("/user")
def user():
    # manually creating users
    # User(user_id = 1, first_name = "Yongye", last_name = "Tan",
    #             email = "yongye0997@gmail.com", password = "qwer1234").save()
    
    # User(user_id = 2, first_name = "Tina", last_name = "Zou",
    #             email = "tzou@gmail.com", password = "qwer2345").save()
    
    users = User.objects.all()
    return render_template("user.html", users=users)
