from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/inquiryoption')
def inquiry_option():
    return render_template('inquiryoption.html')

@app.route('/inquiryform-a')
def inquiryform_a(): 
    return render_template('inquiryform-a.html')

@app.route('/inquiryform-t')
def inquiryform_t():
    return render_template('inquiryform-t.html')


if __name__ == '__main__':
    app.run(debug=True)
