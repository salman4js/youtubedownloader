from flask import Flask, Blueprint, render_template, request, flash
import os
from pytube import YouTube
route = Blueprint('route', __name__)

@route.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        pythonlink = "https://www.pythonanywhere.com/user/azeemdownloader/files/home/azeemdownloader/D%3A%5Cgfg%5C/Downloads"

        url = request.form.get('name')
        homedir = os.path.expanduser('~')
        dir = "D:\gfg\\" + '/Downloads'
        video_name = YouTube(url)
        videoname = video_name.title
        YouTube(url).streams.get_highest_resolution().download(dir)
        path=get.download(link, 'videoname')
        print(videoname)
        flash("Your Video is successfully downloaded", category = "success")
    return render_template('home.html')
