## Simple ToDo list application

This is a simple "ToDoList" project. It can be helpful to manage Your daytime.

## Installing / Getting started

A quick introduction of the minimal setup you need to get a ToDoList up &
running.

```shell
git clone https://github.com/arturiermolenko/to_do_list
cd to_do_list
python3 -m venv venv 
source venv/bin/activate
pip install -r requirements.txt
touch .env
python manage.py migrate
python manage.py runserver
```
Instead of "touch .env" use, please, command "echo > .env" for Windows.
Fill .env file in according to .env.sample


## Features:
- create Tasks with it's content, creation date and tags
- add a deadline time
- making task "Complete" or not will helps to see, what is done and what You still need to do
- create Your own tags
