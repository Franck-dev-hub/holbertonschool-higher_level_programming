#!/usr/bin/python3
import requests
import csv

"""
task_02_requests.py
Consuming and processing data from an API using Python
"""


def fetch_and_print_posts():
    """
    fetch_and_print_posts - Fetch and print posts
    Return: Void
    """
    req = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(req.status_code))
    if req.status_code == 200:
        data = req.json()
        for i in data:
            print(i["title"])


def fetch_and_save_posts():
    """
    fetch_and_save_posts - Fetch and print posts
    Return: Void
    """
    req = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(req.status_code))
    if req.status_code == 200:
        data = req.json()
        result = []
        for i in range(len(data)):
            result.append({
                "id": data[i]["id"],
                "title": data[i]["title"],
                "body": data[i]["body"]
                })
        with open("posts.csv", 'w', newline='', encoding="utf-8") as file:
            names = ["id", "title", "body"]
            reader = csv.DictWriter(file, fieldnames=names)
            reader.writeheader()
            reader.writerows(result)
