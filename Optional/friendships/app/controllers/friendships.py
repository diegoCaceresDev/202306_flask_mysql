#Config
from app import app
from flask import render_template, redirect, request, flash

#Models
from app.models.friendships import User


@app.route("/friendships/")
def friendships():
    
    friendships = User.get_all_friendships()
    users = User.get_all_users()
    
    return render_template("friendships/friendships.html", friendships=friendships, users = users)

@app.route("/add_user/", methods=["POST"])
def add_user():
    
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name']
    }
    
    User.add_user(data)
    
    return redirect('/friendships/')

@app.route("/create_friendship/", methods=["POST"])
def create_friendship():
    
    data = {
        "user_id": int(request.form['user_id']),
        "friend_id": int(request.form['friend_id'])
    }
    
    User.create_friendship(data)
    
    return redirect('/friendships/')