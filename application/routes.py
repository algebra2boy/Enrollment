from copy import deepcopy
from application import app, db
from flask import Response, render_template, request,json, redirect, flash, url_for, session # use to render html file and pass data 
from application.forms import LoginForm, RegisterForm 
from application.model import User, Course, Enrollment
from data.aggregation_pipeline import pipeline

# retrieve the all the classes from the MongoDB
# sort by courseID from smallest to biggest using the + sign 
# courseData = Course.objects.all()
courseData = Course.objects.order_by("courseID")

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True)

@app.route("/courses/")
@app.route("/courses/<term>")
def courses(term = None):
    if term == None:
        term = "Spring 2023"
    # pass data from python to the html view
    return render_template("courses.html", courseData=courseData, course = True, term = term)

@app.route("/register", methods = ["GET", "POST"])
def register():
    # user is already registered, no need to go to resgister page
    if session.get('username'):
        return redirect(url_for('index'))

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
    # if the user is logged in already, no need to let the user to login in again, instead redirect the user to the home page again
    if session.get('username'):
        return redirect(url_for('index'))

    form = LoginForm()

    # if submit button is being pressed
    if form.validate_on_submit():

        # validate user's email and passsword
        email = form.email.data
        password = form.password.data
        # retrieve the first object in the User array 
        user = User.objects(email=email).first()

        if user and user.get_hash_password(password):
            flash(f"{user.first_name} have successfully logged in!!", "success")

            # share information across the site
            session['user_id'] = user.user_id
            session['username'] = user.first_name
            
            return redirect('/index')
        else: 
            flash("Your email is not found in the database", "danger")
    return render_template("login.html", login=True, login_form = form, title = "Login")

@app.route("/logout")
def logout():
    # deleting the session variable
    session['user_id'] = False
    session.pop("username", None)
    return redirect(url_for('index'))


@app.route("/enrollment", methods = ["GET", "POST"])
def enrollment():
    # the user has not logged in yet
    if not session.get('username'):
        return redirect(url_for('index'))

    # print(request.args)
    # request.args.get('courseID') -> use this if we only using GET
    courseID = request.form.get('courseID')
    course_title = request.form.get('title')
    term = request.form.get('term')
    user_id = session.get('user_id')

    single_course_data = {"id": courseID,
                            "title": course_title,
                            "term": term}
    # coming from the course page
    if courseID:
        if Enrollment.objects(user_id=user_id, courseID=courseID):
            flash(f"You are already registered in {course_title}!", "danger")
            return redirect(url_for('courses'))
        else: 
            # add the collection entry to MongoDB
            Enrollment(user_id=user_id, courseID=courseID).save()
            flash(f"You are enrolled in {courseID}!", "success")

    deep_copy_pipeline = deepcopy(pipeline)
    deep_copy_pipeline[4]["$match"]["user_id"] = user_id

    classes = list(User.objects.aggregate(*deep_copy_pipeline))

    return render_template("enrollment.html", 
                            enrollment=True,
                            course_data = single_course_data,
                            title = "Enrollment",
                            classes = classes)

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
