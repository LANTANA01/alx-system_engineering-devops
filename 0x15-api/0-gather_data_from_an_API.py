!#/usr/bin/python3
"""Returns to-do list information for a given employee_ID"""

import requests
import sys

if __name__ == '__main__':

    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]

    #Fetch user info and todos
    users_response = requests.get(url + "users/{}".format(employee_id))
    user = (users_response).json()
    params = {"userId": employee_id}
    todo_response = requests.get(url + "todos", params)
    todos = todo_response.json()
    completed = []

    # Filter completed tasks and count them
    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{})".format(user.get("name"),len(completed),len(todos)))

    for complete in completed:
        print("\t {}".format(complete))
