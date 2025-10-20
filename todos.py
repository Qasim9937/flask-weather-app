from dotenv import load_dotenv
from datetime import datetime 
from datetime import timezone

todos = []

def add_todo(todo):
    if todo not in todos:
        todos.append([todo, datetime.now()])
    return todos



if __name__ == '__main__':
    print(type(todos))