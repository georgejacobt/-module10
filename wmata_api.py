import json
import requests
from flask import Flask

# API endpoint URL's and access keys
WMATA_API_KEY = "b5388b0a60be4f4989b649c643517041"
INCIDENTS_URL = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
headers = {"api_key": WMATA_API_KEY, 'Accept': '*/*'}

################################################################################

app = Flask(__name__)

# get incidents by machine type (elevators/escalators)
# field is called "unit_type" in WMATA API response
@app.route("/incidents/<unit_type>", methods=["GET"])
def get_incidents(unit_type):
  # create an empty list called 'incidents'
  incidents_list = []
  keys_to_include = ["StationCode", "StationName" , "UnitType", "UnitName"]
  filtered_dict = {}

  # use 'requests' to do a GET request to the WMATA Incidents API
  # retrieve the JSON from the response
  response = requests.get(INCIDENTS_URL, headers=headers)
  incidents = response.json()
  elevator_incidents = incidents['ElevatorIncidents']

  # iterate through the JSON response and retrieve all incidents matching 'unit_type'
  # for each incident, create a dictionary containing the 4 fields from the Module 7 API definition
  #   -StationCode, StationName, UnitType, UnitName
  # add each incident dictionary object to the 'incidents' list

  # return the list of incident dictionaries using json.dumps()

  if (unit_type == "escalators"):
     for elevator_incident in elevator_incidents:
        if elevator_incident.get("UnitType") == "ESCALATOR":
           filtered_dict = {key: elevator_incident[key] for key in keys_to_include if key in elevator_incident}
           incidents_list.append(filtered_dict)   
     return(json.dumps(incidents_list))
  
  elif (unit_type == "elevators"):
     for elevator_incident in elevator_incidents:
        if elevator_incident.get("UnitType") == "ELEVATOR":
           filtered_dict = {key: elevator_incident[key] for key in keys_to_include if key in elevator_incident}
           incidents_list.append(filtered_dict)      
     return(json.dumps(incidents_list))


if __name__ == '__main__':
    app.run(debug=True)
