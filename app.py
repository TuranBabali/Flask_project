# imports
from flask import Flask, render_template, request, redirect
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#my_app
app = Flask(__name__,template_folder='templates',static_folder='static',static_url_path='/static')

Scss(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)
 
#Data Class
class  Mytask(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100),nullable= False)
    complete = db.Column(db.Integer)
    created = db.Column(db.DateTime, default =datetime.utcnow)

    def __repr__(self) -> str:
        return f"Task {self.id}"

 
# Home Page
@app.route("/",methods= ['GET','POST'])
def index():
    #Add a task
    if request.method == 'POST':
        current_task= request.form['content']
        new_task= Mytask(content=current_task)
        
        
        return render_template('index.html')
 

if __name__ in  "__main__":
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)
 