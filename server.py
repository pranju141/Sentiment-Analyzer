from flask import Flask,render_template,request,session,redirect,flash
import math
from textblob import TextBlob

app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')




@app.route('/emotion', methods=['POST'])
def emotion():
    sentence = request.form['emotion']
    polarity = TextBlob(sentence).polarity
    subjectivity = TextBlob(sentence).subjectivity
    polarity*=100
    print(polarity)
    subjectivity*=100

    return render_template('emotion.html',p=math.floor(polarity), s=math.floor(subjectivity))
 

app.run(debug=True)
