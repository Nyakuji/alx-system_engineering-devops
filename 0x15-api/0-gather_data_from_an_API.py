#!/usr/bin/python3
"""Script that uses JSONPlaceholder API to get information about employee"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(argv[1])

        # Fetching employee information
        user_url = (
            f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        )
        tasks_url = (
            f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        )

        user_response = requests.get(user_url)
        tasks_response = requests.get(tasks_url)

        if (
            user_response.status_code != 200
            or tasks_response.status_code != 200
        ):
            print(f"Error: Unable to fetch data for employee {employee_id}")
        else:
            user_data = user_response.json()
            tasks_data = tasks_response.json()

            employee_name = user_data['name']
            total_tasks = len(tasks_data)
            done_tasks = sum(task['completed'] for task in tasks_data)

            print(
                f"Employee {employee_name} is done with tasks "
                f"({done_tasks}/{total_tasks}):"
            )

            for task in tasks_data:
                if task['completed']:
                    print(f"\t{task['title']}")
