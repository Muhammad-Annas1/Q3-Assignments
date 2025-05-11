import bcrypt
import json
import os

USER_FILE = "users.json"

class UserManager:
    @staticmethod
    def load_users():
        if os.path.exists(USER_FILE):
            with open(USER_FILE, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return {}
        return {}

    @staticmethod
    def save_users(users):
        with open(USER_FILE, 'w') as f:
            json.dump(users, f)

    @staticmethod
    def register_user(username, password):
        users = UserManager.load_users()
        if username in users:
            return False
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        users[username] = hashed_pw
        UserManager.save_users(users)
        return True

    @staticmethod
    def login_user(username, password):
        users = UserManager.load_users()
        if username in users:
            return bcrypt.checkpw(password.encode(), users[username].encode())
        return False

    @staticmethod
    def reset_password(username, new_password):
        users = UserManager.load_users()
        if username in users:
            hashed_pw = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
            users[username] = hashed_pw
            UserManager.save_users(users)
            return True
        return False
