from pathlib import Path
import json

def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
def get_new_username(path):
    username = input("你的名字是？")
    contents = json.dumps(username)
    path.write_text(contents)
    return username
def greet_user():
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        new = input(f"请问你的用户名是否叫{username},如果不是,请输入q: ")
        if new == "q":
            username = get_new_username(path)
        print(f"欢迎回来:{username}")
    else:
        username = get_new_username(path)
        print(f"当你回来的时候程序记住了你的名字叫{username}")

greet_user()