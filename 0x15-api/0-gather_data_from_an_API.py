#!/usr/bin/python3
''' gather data from an API '''
import requests
from sys import argv

if __name__ == '__main__':
    # get employee response
    endpoint = 'https://jsonplaceholder.typicode.com'
    user_res = requests.get(endpoint + '/users/' + argv[1]).json()

    # get total number of tasks
    todos = requests.get(endpoint + '/todos?userId=' + argv[1]).json()

    # get number completed tasks and their titles
    titles_done = [todo['title'] for todo in todos if todo['completed']]

    print('Employee {} is done with tasks({}/{}):'
          .format(user_res['name'], len(titles_done), len(todos)))

    [print('\t {}'.format(title)) for title in titles_done]
