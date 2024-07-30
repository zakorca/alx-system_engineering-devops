#!/usr/bin/python3
""" export data in the CSV format """
import csv
import requests
import sys


if __name__ == "__main__":
    url_user = "https://jsonplaceholder.typicode.com/users/"
    url_todos = "https://jsonplaceholder.typicode.com/todos"
    user = requests.get(url_user + "{}".format(sys.argv[1])).json()
    todos = requests.get(url_todos, params={"userId": sys.argv[1]}).json()

    user_id = sys.argv[1]
    username = user.get("username")

    with open("{}.csv".format(user_id), "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, username,
                             task.get("completed"), task.get("title")])
