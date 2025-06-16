from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load job applications
def load_jobs():
    try:
        with open("jobs.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save job applications
def save_jobs(jobs):
    with open("jobs.json", "w") as file:
        json.dump(jobs, file, indent=4)

@app.route("/jobs", methods=["GET"])
def get_jobs():
    return jsonify(load_jobs())

@app.route("/jobs/<int:job_id>", methods=["GET"])
def get_job(job_id):
    jobs = load_jobs()
    for job in jobs:
        if job["id"] == job_id:
            return jsonify(job)
    return {"message": "Job not found"}, 404

@app.route("/jobs", methods=["POST"])
def add_job():
    jobs = load_jobs()
    new_job = request.json
    new_job["id"] = len(jobs) + 1
    jobs.append(new_job)
    save_jobs(jobs)
    return jsonify(new_job), 201

@app.route("/jobs/<int:job_id>", methods=["DELETE"])
def delete_job(job_id):
    jobs = load_jobs()
    jobs = [job for job in jobs if job["id"] != job_id]
    save_jobs(jobs)
    return {"message": "Job deleted"}

if __name__ == "__main__":
    app.run(debug=True)
