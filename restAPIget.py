#!/usr/bin/env python3

import requests
import json

def get_api_data():
	from __main__ import baseUrl		# import variable from calling script
	from __main__ import apiUrl			# import variable from calling script
	apiResponse = requests.get(baseUrl + apiUrl)
	test_status_code(apiResponse)
	return

def test_status_code(apiResponse):
	if apiResponse.status_code == 200:
		print_json_data(apiResponse)
	elif apiResponse.status_code == 400:
		print("API reuest failed with response code " + str(apiResponse.status_code) + " (bad api request sent to endpoint server)")
	elif apiResponse.status_code == 401:
		print("API reuest failed with response code " + str(apiResponse.status_code) + " (endpoint server authentication error)")
	elif apiResponse.status_code == 403:
		print("API reuest failed with response code " + str(apiResponse.status_code) + " (access to endpoint resource is forbidden)")
	elif apiResponse.status_code == 404:
		print("API reuest failed with response code " + str(apiResponse.status_code) + " (resource not found on endpoint server)")
	return

def print_json_data(apiResponse):
	parsedJSON = json.loads(apiResponse.content)
	print(json.dumps(parsedJSON, indent=2, sort_keys=True))
	return

get_api_data()
