#!/usr/bin/python3
"""exports data in the JSON format"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    request_ses = requests.Session()

    empid = argv[1]
    idurl = ('https://jsonplaceholder.typicode.com/users/{}/todos'
             .format(empid))
    name_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(empid)

    the_employee = request_ses.get(idurl)
    employee_name = request_ses.get(name_url)

    json_request = the_employee.json()
    usr = employee_name.json()['username']

    total_tasks = []
    updatedUsr = {}

    for all_emps in json_request:
        total_tasks.append(
            {
                "task": all_emps.get('title'),
                "completed": all_emps.get('completed'),
                "username": usr,
            })
    updatedUsr[empid] = total_tasks

    jsonFile = empid + ".json"
    with open(jsonFile, 'w') as f:
        json.dump(updatedUsr, f)
