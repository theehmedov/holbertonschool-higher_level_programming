#!/usr/bin/python3
"""Fetch posts from JSONPlaceholder and print or save them"""
import requests
import csv

URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    """Fetch posts and print their titles"""
    response = requests.get(URL)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """Fetch posts and save them to a CSV file"""
    response = requests.get(URL)
    if response.status_code == 200:
        posts = response.json()
        # Strukturlaşdırılmış məlumat: list of dictionaries
        data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

        # CSV faylına yazmaq
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
