from flask import *;
from pymongo import MongoClient

client=MongoClient("mongodb://127.0.0.1:27017")

#creating a database
db=client['PMS']

#creating a collection
horror_data=db.HORROR
login_data=db.USERS
action_data=db.ACTION
news_data=db.NEWS
pomplet_data=db.POMPLET


app=Flask(__name__)
@app.route('/')
def home():
    return render_template('bgimage.html')

@app.route('/register')
def registration():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/writer')
def contentwriter():
    return render_template('writer.html')

@app.route('/news')
def newspaper():
    return render_template('news.html')

@app.route('/pomplet')
def pomplet():
    return render_template('pomplet.html')

@app.route('/twitter')
def twitter():
    return render_template('tweet.html')

@app.route('/instagram')
def instagram():
    return render_template('igram.html')

@app.route('/fb')
def facebook():
    return render_template('fb.html')

@app.route("/horror")
def horror():
    return render_template('imagelist.html')

@app.route("/action")
def action():
    return render_template('action.html')

@app.route("/sucessh",methods=['GET', 'POST'])
def onSubmit():
    name=request.form.get("Name")
    email=request.form.get("Email")
    msg=request.form.get("Message")

    a={"Name": name,"Email": email, "Message":msg}
    horror_data.insert_one(a)
    return render_template('writer.html')

@app.route("/sucessnews",methods=['GET', 'POST'])
def onNews():
    name=request.form.get("name")
    email=request.form.get("email")
    pg=request.form.get("pgno")
    side=request.form.get("side")

    a={"Name": name,"Email": email, "PageNo":pg,"Side":side}
    news_data.insert_one(a)
    return render_template('bgimage.html')

@app.route("/sucesspomp",methods=['GET', 'POST'])
def onPomplet():
    name = request.form.get("name")
    email = request.form.get("email")
    pg = request.form.get("pgno")
    side = request.form.get("side")

    a = {"Name": name, "Email": email, "No of pages": pg, "Side": side}
    pomplet_data.insert_one(a)
    return render_template('bgimage.html')

@app.route("/logins",methods=['GET', 'POST'])
def onLogin():
    name=request.form.get("name")
    email=request.form.get("email")
    pwd=request.form.get("pass")

    a={"Name": name,"Email": email, "Password":pwd}
    login_data.insert_one(a)
    return render_template('bgimage.html')


@app.route("/sucessaction",methods=['GET', 'POST'])
def onAction():
    name=request.form.get("Name")
    email=request.form.get("Email")
    msg=request.form.get("Message")

    a={"Name": name,"Email": email, "Message":msg}
    action_data.insert_one(a)
    return render_template('writer.html')

@app.route("/data")
def dataa():
    data=horror_data.find()
    return render_template('index2.html',lst=data)

if __name__=='__main__':
    app.run()