from flask import Flask, render_template

app = Flask(__name__)
JOBS = [
    {'Id':1, 'Title': 'Data Analyst', 'Location': 'Chennai', 'Salary': Rs: 20L },
    {'Id':2, 'Title': 'Data Scientist', 'Location': 'Bangalore', 'Salary': Rs: 25L }
    ]
@app.route('/')
def careers_home():
    return render_template('home.html', jobs=JOBS)

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)