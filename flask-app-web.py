from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)
JOBS = [
    { 'Id':1, 'Title': 'Data Analyst', 'Location': 'Chennai', 'Salary': '50000' },
    { 'Id':2, 'Title': 'Data Scientist', 'Location': 'Bangalore', 'Salary': '60000' }
]
#def job_list_db():


@app.route('/')
def careers_home():
    return render_template('home.html', jobs=job_list_db())
@app.route('/api/jobs')
def job_list():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)