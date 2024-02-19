#!/usr/bin/python3
"""Script that uses JSONPlaceholder API to get information about an employee"""
import requests
from sys import argv

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
    else:
        # Convert the command-line argument to an integer (employee_id)
        employee_id = int(argv[1])

        # Fetching employee information from JSONPlaceholder API
        user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        t = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

        user_respons = requests.get(user_url)
        tasks_respons = requests.get(t)

        # Check if the API requests were successful
        if user_respons.status_code != 200 or tasks_respons.status_code != 200:
            print(f"Error: Unable to fetch data for employee {employee_id}")
        else:
            # Extract JSON data from the API responses
            user_data = user_respons.json()
            tasks_data = tasks_respons.json()

            # Extract relevant information about the employee and tasks
            employee_name = user_data['name']
            total_tasks = len(tasks_data)
            done_tasks = sum(task['completed'] for task in tasks_data)

            # Display the employee's name and task completion status
            print(
                f"Employee {employee_name} is done with tasks "
                f"({done_tasks}/{total_tasks}):"
            )

            # Display the titles of completed tasks
            for task in tasks_data:
                if task['completed']:
                    print(f"\t{task['title']}")
