from wmata_api import app
import json
import unittest

class WMATATest(unittest.TestCase):
    # ensure both endpoints return a 200 HTTP code
    def test_http_success(self):
        escalator_response = app.test_client().get('/incidents/escalators').status_code
        # assert that the response code of 'incidents/escalators returns a 200 code
        self.assertEqual(escalator_response,200)

        elevator_response = app.test_client().get('/incidents/elevators').status_code
        # assert that the response code of 'incidents/elevators returns a 200 code
        self.assertEqual(elevator_response,200)

################################################################################

    # ensure all returned incidents have the 4 required fields
    def test_required_fields(self):
        required_fields = ["StationCode", "StationName", "UnitType", "UnitName"]
        required_fields_sorted = required_fields.sort()

        response = app.test_client().get('/incidents/escalators')
        json_response = json.loads(response.data.decode())

        # for each incident in the JSON response assert that each of the required fields
        # are present in the response

        for incident in json_response:
            fields = list(incident.keys()).sort()
            check_flag = required_fields_sorted == fields
            self.assertEqual(check_flag, True)


################################################################################

    # ensure all entries returned by the /escalators endpoint have a UnitType of "ESCALATOR"
    def test_escalators(self):
        response = app.test_client().get('/incidents/escalators')
        json_response = json.loads(response.data.decode())


        # for each incident in the JSON response, assert that the 'UnitType' is "ESCALATOR"

        for incident in json_response:
            check_flag = incident["UnitType"] == "ESCALATOR"
            self.assertEqual(check_flag, True)

################################################################################

    # ensure all entries returned by the /elevators endpoint have a UnitType of "ELEVATOR"
    def test_elevators(self):
        response = app.test_client().get('/incidents/elevators')
        json_response = json.loads(response.data.decode())

        # for each incident in the JSON response, assert that the 'UnitType' is "ELEVATOR"

        for incident in json_response:
            check_flag = incident["UnitType"] == "ELEVATOR"
            self.assertEqual(check_flag, True)

################################################################################

if __name__ == "__main__":
    unittest.main()