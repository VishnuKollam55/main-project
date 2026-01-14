from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <html>
    <head>
        <title>Integrated Pollution Monitoring System</title>
    </head>
    <body style="font-family:Arial;">
        <h1>Integrated Pollution Monitoring and Control System</h1>
        <hr>

        <h2>Air Pollution Module</h2>
        <p>Model Used: Random Forest Regression</p>
        <p>Output: AQI Prediction</p>

        <h2>Water Pollution Module</h2>
        <p>Model Used: Random Forest Regression</p>
        <p>Output: Water Quality Index (WQI)</p>

        <h2>Noise Pollution Module</h2>
        <p>Model Used: Random Forest Classification</p>
        <p>Output: Noise Level (Low / Medium / High)</p>

        <hr>
        <p><b>Status:</b> System running successfully</p>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
