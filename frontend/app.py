from flask import Flask, render_template, request, redirect
from datetime import datetime
import random

app = Flask(__name__)

alerts = []

signal_states = ["red", "yellow", "green"]

junctions = [
    {"name": "Silk Board", "lat": 12.9166, "lng": 77.6230, "signal": "green"},
    {"name": "Marathahalli Bridge", "lat": 12.9567, "lng": 77.7010, "signal": "yellow"},
    {"name": "Madiwala Checkpost", "lat": 12.9244, "lng": 77.6174, "signal": "red"},
    {"name": "KR Puram", "lat": 13.0007, "lng": 77.6956, "signal": "green"},
    {"name": "Hebbal Flyover", "lat": 13.0358, "lng": 77.5970, "signal": "yellow"},
    {"name": "Whitefield Hope Farm", "lat": 12.9698, "lng": 77.7500, "signal": "red"},
    {"name": "Electronic City Junction", "lat": 12.8406, "lng": 77.6770, "signal": "green"},
    {"name": "Majestic Signal", "lat": 12.9780, "lng": 77.5720, "signal": "yellow"},

    # Hyderabad
    {"name": "Gachibowli", "lat": 17.4399, "lng": 78.3529, "signal": "red"},
    {"name": "Hitech City", "lat": 17.4510, "lng": 78.3800, "signal": "green"},
    {"name": "Kukatpally JNTU", "lat": 17.4931, "lng": 78.3916, "signal": "yellow"},
    {"name": "Secunderabad Parade Ground", "lat": 17.4393, "lng": 78.4983, "signal": "red"},
    {"name": "LB Nagar Circle", "lat": 17.3470, "lng": 78.5570, "signal": "green"},
    {"name": "Mehdipatnam Signal", "lat": 17.3843, "lng": 78.4327, "signal": "yellow"},
    {"name": "Banjara Hills Road No. 12", "lat": 17.4146, "lng": 78.4342, "signal": "green"},
    {"name": "Charminar Signal", "lat": 17.3616, "lng": 78.4747, "signal": "red"},

    # Delhi
    {"name": "Connaught Place", "lat": 28.6304, "lng": 77.2177, "signal": "green"},
    {"name": "AIIMS Flyover", "lat": 28.5667, "lng": 77.2100, "signal": "yellow"},
    {"name": "India Gate Circle", "lat": 28.6090, "lng": 77.2295, "signal": "red"},
    {"name": "Dwarka Mor", "lat": 28.6270, "lng": 77.0720, "signal": "green"},
    {"name": "Lajpat Nagar", "lat": 28.5673, "lng": 77.2439, "signal": "yellow"},
    {"name": "Saket Mall Junction", "lat": 28.5285, "lng": 77.2193, "signal": "green"},
    {"name": "Kashmere Gate", "lat": 28.6679, "lng": 77.2274, "signal": "red"},
    {"name": "Rajouri Garden Circle", "lat": 28.6433, "lng": 77.1130, "signal": "yellow"},

    # Mumbai
    {"name": "Powai", "lat": 19.1189, "lng": 72.9096, "signal": "red"},
    {"name": "Bandra Kurla Complex", "lat": 19.0621, "lng": 72.8674, "signal": "green"},
    {"name": "Andheri Signal", "lat": 19.1197, "lng": 72.8468, "signal": "yellow"},
    {"name": "Sion Circle", "lat": 19.0450, "lng": 72.8641, "signal": "red"},
    {"name": "Dadar TT Circle", "lat": 19.0176, "lng": 72.8430, "signal": "green"},
    {"name": "Marine Drive", "lat": 18.9430, "lng": 72.8238, "signal": "yellow"},
    {"name": "Thane Teen Hath Naka", "lat": 19.1990, "lng": 72.9720, "signal": "green"},
    {"name": "Vashi Toll Plaza", "lat": 19.0748, "lng": 72.9970, "signal": "red"}
]


@app.route("/")
def dashboard():
    return render_template("dashboard.html", junctions=junctions, alerts=alerts)


@app.route("/alerts")
def alerts_page():
    return render_template("alerts.html", alerts=alerts)


@app.route("/create-alert")
def create_alert():
    return render_template("create_alert.html", junctions=junctions)


@app.route("/trigger-alert", methods=["POST"])
def trigger_alert():
    junction = request.form["junction"]
    alert_type = request.form["alert_type"]

    alerts.append({
        "junction": junction,
        "alert_type": alert_type,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    return redirect("/alerts")


if __name__ == "__main__":
    app.run(debug=True)
