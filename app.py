import os

from bson.objectid import ObjectId
from flask import Flask, redirect, render_template, request, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB setup
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.events_db


@app.route("/")
def index():
    events = list(db.events.find())
    settings = db.settings.find_one()
    return render_template("index.html", events=events, settings=settings)


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        title = request.form["title"]
        time = request.form.get("time").split(",")
        location = request.form["location"]

        db.events.insert_one({"title": title, "time": time, "location": location})
        return redirect(url_for("admin"))
    events = list(db.events.find())
    return render_template("admin.html", events=events)


@app.route("/delete/<event_id>", methods=["POST"])
def delete(event_id):
    db.events.delete_one({"_id": ObjectId(event_id)})
    return redirect(url_for("admin"))


@app.route("/settings", methods=["GET", "POST"])
def settings():
    if request.method == "POST":
        font = request.form["font"]
        color = request.form["color"]
        header = request.form["header"]
        spacing = request.form["spacing"]
        separator = request.form["separator"]
        max_size = request.form["max_size"]
        db.settings.update_one(
            {},
            {
                "$set": {
                    "font": font,
                    "color": color,
                    "header": header,
                    "spacing": spacing,
                    "separator": separator,
                    "max_size": max_size,
                }
            },
            upsert=True,
        )
        return redirect(url_for("settings"))
    settings = db.settings.find_one()
    return render_template("settings.html", settings=settings)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
