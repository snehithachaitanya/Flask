from flask import *;
from pymongo import MongoClient

client=MongoClient("mongodb://127.0.0.1:27017")#points to mongo compas

#creating a database
db=client['PMS']

#creating a collection
horror_details=db.HORROR

app=Flask(__name__)

@app.route("/")
def sample10():
    return render_template("imagelist.html")

@app.route("/sucess",methods=['GET', 'POST'])
def onSubmit():
    name=request.form.get("Name")
    email=request.form.get("Email")
    msg=request.form.get("Message")

    a={"Name": name,"Email": email, "Message":msg}
    horror_details.insert_one(a)
    return "insertion sucessful"

@app.route("/data")
def dataa():
    data=horror_details.find()
    return render_template('index2.html',lst=data)

# running the app file
if __name__ == "__main__":
    app.run()