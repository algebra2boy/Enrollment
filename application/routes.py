from application import app, db
from flask import Response, render_template, request,json # use to render html file and pass data 

courseData = [{"courseID":"1111","title":"PHP 111","description":"Intro to PHP","credits":"3","term":"Fall, Spring"}, 
                 {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":"4","term":"Spring"}, 
                 {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":"3","term":"Fall"}, 
                 {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":"3","term":"Fall, Spring"}, 
                 {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":"4","term":"Fall"}]

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

@app.route("/register")
def register():
    return render_template("register.html", register=True)

@app.route("/login")
def login():
    return render_template("login.html", login=True)

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


class User(db.Document):
    user_id     = db.IntField(unique=True)
    first_name  = db.StringField(max_length = 50)
    last_name   = db.StringField(max_length = 50)
    email       = db.StringField(max_length = 30)
    password    = db.StringField(max_length = 30)


@app.route("/user")
def user():
    # manually creating users
    User(user_id = 1, first_name = "Yongye", last_name = "Tan",
                email = "yongye0997@gmail.com", password = "qwer1234").save()
    
    User(user_id = 2, first_name = "Tina", last_name = "Zou",
                email = "tzou@gmail.com", password = "qwer2345").save()
    
    users = User.objects.all()
    return render_template("user.html", users=users)
