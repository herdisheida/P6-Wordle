from pathlib import Path
import json


# EYDA nota ekki klasa fyrir user
class User:
    RESULT_FOLDER = Path("results")

    def __init__(self):
        self.users: list[str] = []
        self.curr_user: str = None
    
    def set_curr_user(self, user):
        self.curr_user = user
    
    def get_user(self):
        return self.curr_user
    
    def get_history(self):
        filename = f"{self.curr_user}_results.txt"
        file_path = self.RESULT_FOLDER / filename

        
        with open(file_path, mode="r", encoding="utf-8") as file:
            history = json.load(file)
            print(history)


    def add_user(self, user):
        self.users.append(user)

    def print_all_users(self):
        print("\nAll users:")
        for user in self.users:
            print(user)


user = User()
user.add_user("mima")
user.add_user("mimi")
user.set_curr_user("mima")
user.get_history()
