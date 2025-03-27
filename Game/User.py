class User:
    def __init__(self):
        self.users: list[str] = []
        self.curr_user: str = None
    
    def set_user(self, user):
        self.curr_user = user
    
    def get_user(self):
        return self.curr_user
    
    def get_history(self):
        # read from file
        # return history
        pass

    def add_user(self, user):
        self.users.append(user)

    def print_all_users(self):
        print("\nAll users:")
        for user in self.users:
            print(user)
