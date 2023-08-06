from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [
    { 'Id':1, 'Title': 'Data Analyst', 'Location': 'Chennai', 'Experience': '0-1yr' },
    { 'Id':2, 'Title': 'Data Scientist', 'Location': 'Bangalore', 'Experience': '5-8yrs' }
]
@app.route('/')
def careers_home():
    return render_template('home.html', jobs=JOBS)
@app.route('/api/jobs')
def job_list():
    return jsonify(JOBS)
if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)