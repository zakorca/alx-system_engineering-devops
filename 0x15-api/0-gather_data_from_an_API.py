#!/usr/bin/python3
""" returns information about his/her TODO list progress using REST API """
import requests
import sys


if __name__ == "__main__":
    url_user = "https://jsonplaceholder.typicode.com/users/"
    url_todos = "https://jsonplaceholder.typicode.com/todos"
    user = requests.get(url_user + "{}".format(sys.argv[1])).json()
    todos = requests.get(url_todos, params={"userId": sys.argv[1]}).json()
    count = 0
    total_task_todos = len(todos)

    user_name = user.get("name")
    for task in todos:
        if task.get("completed"):
            count += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, count, total_task_todos))
    for task in todos:
        if task.get("completed"):
            print("\t {}".format(task.get("title")))
