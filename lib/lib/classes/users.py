


class User:
    def __init__(self, name, email, quickie, longterm, drinks, id = None):
        self.name = name
        self.email = email
        self.quickie = quickie
        self.longterm = longterm
        self.drinks = drinks
        self.id = id

    def __repr__(self):
        return f"<User {self.name} {self.email} {self.quickie} {self.longterm} {self.drinks} {self.id}>"
    

    @classmethod
    def create_table(cls):
        create_users_sql = """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY, 
            name TEXT, 
            email TEXT, 
            quickie TEXT, 
            longterm TEXT, 
            drinks TEXT"""
        CURSOR.execute(create_users_sql)