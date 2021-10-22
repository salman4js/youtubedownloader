from flask import Flask, Blueprint, render_template, request, flash
import os
from pytube import YouTube
route = Blueprint('route', __name__)

@route.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form.get('name')
        homedir = os.path.expanduser('~')
        dir = "D:\gfg\\" + '/Downloads'
        YouTube(url).streams.get_highest_resolution().download(dir)
        flash("Your Video is successfully downloaded", category = "success")
    return render_template('home.html')
