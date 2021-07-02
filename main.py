from flask import Flask, render_template, request
from random import choice
from model import chicken_prices_before, chicken_prices_after

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_wings = int(request.form["wings"])
        days = request.form['weekday']
        price_message_before = chicken_prices_before(num_wings, days)
        price_message_after = chicken_prices_after(num_wings, days)
        difference = round((float(price_message_after)-float(price_message_before)),2)
        print (difference)
        return render_template('results.html', price_message_before=price_message_before, price_message_after=price_message_after, num_wings = num_wings, difference = difference)
    else:
        return render_template('index.html')



app.run(host='0.0.0.0', port=8080)

