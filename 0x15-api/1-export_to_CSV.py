#!/usr/bin/python3
""" a script that exports data in the CSV format"""

import csv
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
    usr = employee_name.json()['name']

    total_num_tasks = 0

    for tasks in json_request:
        if tasks['completed']:
            total_num_tasks += 1

    CSVfile = empid + '.csv'

    with open(CSVfile, "w", newline='') as csvfile:
        write = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in json_request:
            write.writerow([empid, usr, i.get('completed'), i.get('title')])
