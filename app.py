from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/inquiryoption')
def inquiry_option():
    return render_template('inquiryoption.html')


if __name__ == '__main__':
    app.run(debug=True)

