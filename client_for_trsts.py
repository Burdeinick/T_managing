import requests


def get_users():
    """ For testing geting all users"""
    url = r'http://127.0.0.1:5000/api/v1/user/list'
    headers = {"UserName": "Kop", "UserSecret": "4567"}
    requests.post(url, headers=headers)

def board_create():
    """For board create"""
    url = r'http://127.0.0.1:5000/api/v1/board/create'
    headers = {"UserName": "Kop", "UserSecret": "456"}
    data = {
            "title": "Доска разработчика",
            "columns": [
                        "ToDo",
                        "InProgress",
                        "Done"
                        ]
            }
    requests.post(url, json=data, headers=headers)







def board_delete():
    """ For board delete"""
    url = r'http://127.0.0.1:5000/api/v1/board/delete'
    headers = {"UserName": "Kop", "UserSecret": "4567"}
    data = {"title": "Доска разработчика"}
    requests.post(url, json=data, headers=headers)

def board_list():
    """ Get all boards """
    url = r'http://127.0.0.1:5000/api/v1/board/list'
    headers = {"UserName": "Kop", "UserSecret": "456"}
    requests.post(url, headers=headers)   


def card_create():
    """ Create a card """
    url = r'http://127.0.0.1:5000/api/v1/card/create'
    headers = {"UserName": "Bob", "UserSecret": "123"}
    data = {
            "title": "Доска выаыва",
            "board": "Доска разработчика",
            "status": "Noooo",
            "description": "Необходимо проверить",
            "assignee": "Username",
            "estimation": "7h"
            }
    requests.post(url, json=data, headers=headers) 

def card_update():
    """ For update a card"""
    url = r'http://127.0.0.1:5000/api/v1/card/update'
    headers = {"UserName": "Kop", "UserSecret": "456"}
    data = {
            "title": "Развернуть PostgreSQL",
            "board": "Доска разработчика",
            "status": "hjgjgh",
            "description": "Новое описание",
            "assignee": "assigneeeeeeee",
            "estimation": "estwewewewe"
            }
    requests.post(url, json=data, headers=headers) 

def card_delete():
    """ For delete a card"""
    url = r'http://127.0.0.1:5000/api/v1/card/delete'
    headers = {"UserName": "Bob", "UserSecret": "123"}
    data = {
            "title": "Развернуть PostgreSQL",
            "board": "Доска разработчика"
            }

    requests.post(url, json=data, headers=headers) 














def colum_info():
    """ Get info about a task"""
    url = r'http://127.0.0.1:5000/api/v1/report/cards_by_column'
    headers = {"UserName": "Bob", "UserSecret": "123"}
    data = {
            "board": "Доска разработчика",
            "column": "Noooo",
            "assignee": "Username"
            }
    requests.post(url, json=data, headers=headers) 

# get_users()
# board_create()
# board_delete()
# board_list()
# card_create()
# card_update()
# card_delete()
colum_info()
