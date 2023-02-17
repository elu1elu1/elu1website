from flask import Flask, render_template, jsonify
app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Scientist',
    'location': 'Shanghai, China',
  },
  {
    'id': 2,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': '$ 140,000'
  },
{
    'id': 3,
    'title': 'Backend Engineer',
    'location': 'Remote',
    'salary': '$ 160,000'
  },
{
    'id': 4,
    'title': 'Data Analyst',
    'location': 'Boston, MA USA',
    'salary': '$ 140,000'
  },
]

@app.route("/")

def consulting_service():
  return render_template('home.html',
                        jobs=JOBS,
                        company_name='Data-Lu'
                        )

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

  
  
