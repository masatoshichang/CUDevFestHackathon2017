from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    test_data = [('2013', 15), ('2014', 5), ('2015', 10), ('2016', 30), ('2017', 80)]
    return render_template('line_chart_template.html', data_list=test_data)
