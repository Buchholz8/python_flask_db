from flask import Flask
import dbhelpers
import json

app = Flask(__name__)

@app.get('/cars')
def get_cars():
    results = dbhelpers.run_procedures('CALL get_cars()', [])
    car_json = json.dumps(results, default=str)
    return car_json

app.run(debug=True)