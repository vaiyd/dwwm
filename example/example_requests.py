# -*- coding: utf-8 -*-

#pip install requests
import requests

def get():
    res = requests.get(url="http://127.0.0.1:5001/")
    dict_res = res.json()
    print(dict_res)

def post():
    res = requests.post(url="http://127.0.0.1:5001/tasks",
                        json={"title":"title7", "description":"dc7"})
    dict_res = res.json()
    print(dict_res)

def put():
    res = requests.put(url="http://127.0.0.1:5001/tasks/5",
                        json={"completed":True,
                              "description":"description5"})
    dict_res = res.json()
    print(dict_res)

def delete():
    res = requests.delete(url="http://127.0.0.1:5001/tasks/5")
    dict_res = res.json()
    print(dict_res)

def main():
    post()

if __name__ == '__main__':
    main()