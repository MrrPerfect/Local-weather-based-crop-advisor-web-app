from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    soil_type = request.form['soil_type']
    location = request.form['location']

    # You can process the selected soil_type and location here

    return f"Soil Type: {soil_type}, Location: {location}"


if __name__ == '__main__':
    app.run(debug=True)
