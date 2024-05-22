#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to JSON format.
Record all the tasks owned by an wmployee.
"""

import json
import requests
import sys


if __name__ == "__main__":

    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Get the user_ID from the command-line argument
    user_id = sys.argv[1]

    # Fetch user information using the provided employee ID
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    # Fetch the todo list for the employee using the provided user_ID
    params = {"userId": user_id}
    todos = requests.get(url + "todos", params).json()

    # Create a dictionary containing the user and todo list information
    data_to_export = {
        user_id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            }
            for t in todos
        ]
    }

    # Write the data to a JSON file with the user_id as the filename
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
