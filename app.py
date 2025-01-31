from flask import Flask, render_template, request, jsonify, redirect
import requests
from datetime import datetime

app = Flask(__name__)

# API endpoint for fetching pincode details
API_URL = "https://api.postalpincode.in/pincode/"

# In-memory log storage
request_logs = []

# Custom API Endpoint
@app.route("/api/pincode/<string:pincode>", methods=["GET"])
def custom_api(pincode):
    response = requests.get(API_URL + pincode)
    if response.status_code == 200:
        data = response.json()
        if data and data[0]["Status"] == "Success":
            return jsonify({
                "status": "success",
                "pincode": pincode,
                "details": data[0]["PostOffice"]
            })
        else:
            return jsonify({
                "status": "error",
                "message": "No details found for this pincode."
            }), 404
    else:
        return jsonify({
            "status": "error",
            "message": "Failed to fetch data from the API."
        }), 500

# Homepage
@app.route("/", methods=["GET", "POST"])
def index():
    pincode_details = None
    if request.method == "POST":
        pincode = request.form.get("pincode")
        if pincode:
            # Log the request
            log_entry = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "pincode": pincode,
                "status": "Initiated"
            }
            request_logs.append(log_entry)

            # Call the API to fetch pincode details
            response = requests.get(API_URL + pincode)
            if response.status_code == 200:
                data = response.json()
                if data and data[0]["Status"] == "Success":
                    pincode_details = data[0]["PostOffice"]
                    log_entry["status"] = "Success"
                else:
                    pincode_details = "No details found for this pincode."
                    log_entry["status"] = "No data found"
            else:
                pincode_details = "Failed to fetch data from the API."
                log_entry["status"] = "API Error"
    
    return render_template("index.html", pincode_details=pincode_details)

# Logs Page
@app.route("/logs")
def logs():
    return render_template("logs.html", logs=request_logs)

# API Documentation Page
@app.route("/api-docs")
def api_docs():
    return render_template("api_docs.html")

# About Page
@app.route("/about")
def about():
    return render_template("about.html")

# Contact Us Page
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        # Here you can add code to save the message or send an email
        return render_template("contact.html", success=True)
    return render_template("contact.html", success=False)

# Clear Logs
@app.route("/clear-logs", methods=["POST"])
def clear_logs():
    global request_logs
    request_logs = []  # Clear the logs
    return redirect("/logs")  # Redirect back to the logs page

if __name__ == "__main__":
    app.run(debug=True)