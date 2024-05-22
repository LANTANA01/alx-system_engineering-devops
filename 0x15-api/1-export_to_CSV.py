#!/usr/bin/python3
"""Exports todo list information for a given employee_ID into CSV format."""

import csv
import requests
import sys


if __name__ == "__main__":

    # Define the base URL for the JSON API
    url = "https://jsonplaceholder.typicode.com/"
    
    # Get the user ID from the command-line
    user_id = sys.argv[1]

    # Fetch user information from the API
    user = requests.get(url + "users/{}".format(user_id)).json()

    # Extract the username from the user data
    username = user.get("username")

    # Fetch Todo list
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Use list comprehension to iterate over the todo list items
    # Write each item's details (user ID, username, completion status,
    #   and title) as a row in the CSV file
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
