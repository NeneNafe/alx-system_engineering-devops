#!/usr/bin/python3
"""a Python script that thats uses a REST API, for a given employee ID
returns information about his/her TODO list progress"""

import json
from sys import argv

import requests

if __name__ == "__main__":

    request_ses = requests.Session()

    empid = argv[1]
    idurl = ('https://jsonplaceholder.typicode.com/users/{}/todos'
             .format(empid))
    name_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(empid)

    the_employee = request_ses.get(idurl)
    employee_name = request_ses.get(name_url)

    json_request = the_employee.json()
    name_of_emp = employee_name.json()['name']

    total_num_tasks = 0

    for tasks in json_request:
        if tasks['completed']:
            total_num_tasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name_of_emp, total_num_tasks, len(json_request)))

    for tasks in json_request:
        if tasks['completed']:
            print("\t " + tasks.get('title'))
