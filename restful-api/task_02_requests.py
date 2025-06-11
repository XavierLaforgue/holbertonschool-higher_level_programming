#!/usr/bin/python3
"""
Module Name: task_02_requests.

Contains functions to fetch and prints posts from an http server.
"""
import requests
import csv


def fetch_and_print_posts():
    """Fetch list of posts from httpserver and print them."""
    response = requests.get("https://jsonplaceholder.typicode.com/"
                            "posts")
    print(f"Status Code: {response.status_code}")
    if response.status_code >= 200 and response.status_code < 300:
        posts = response.json()
        [print(post["title"]) for post in posts]


def fetch_and_save_posts():
    """Fetch list of posts, save chose fields in csv file."""
    response = requests.get("http://jsonplaceholder.typicode.com/"
                            "posts")
    if response.status_code < 200 and response.status_code >= 300:
        return
    posts = response.json()
    [posts.pop("userId") for posts in posts]
    with open("posts.csv", "w", encoding="utf-8") as f:
        fieldnames = ["id", "title", "body"]
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for post in posts:
            writer.writerow(post)


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
