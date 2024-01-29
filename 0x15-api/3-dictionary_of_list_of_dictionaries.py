#!/usr/bin/python3
"""Exports data in the JSON format"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    import json
    import requests
    import sys

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    doAll = {}

    for user in users:
        task_list = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                task_Dict = {"username": user.get('username'),
                             "task": task.get('title'),
                             "completed": task.get('completed')}
                task_list.append(task_Dict)
        doAll[user.get('id')] = task_list

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(doAll, f)
