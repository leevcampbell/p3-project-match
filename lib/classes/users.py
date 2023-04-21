from lib import CURSOR, CONN




class User:
    def __init__(self, name, email, quickie, long_term, drinks, id = None):
        self.name = name
        self.email = email
        self.quickie = quickie
        self.long_term = long_term
        self.drinks = drinks
        self.id = id

    def __repr__(self):
        return f"<User name: {self.name} email: {self.email} quickie: {self.quickie} long_term: {self.long_term} drinks: {self.drinks} >"
    

    
    def update(self):
        sql = """UPDATE users SET 
            name = ?, 
            email = ?, 
            quickie = ?, 
            long_term = ?, 
            drinks = ? 
            WHERE id = ?"""
        CURSOR.execute(sql, [self.name, self.email, self.quickie, self.long_term, self.drinks, self.id])
        CONN.commit()

        
    
    def create(self):
        sql = """INSERT INTO users (
            name,
            email,
            quickie,
            long_term,
            drinks
        ) VALUES (?, ?, ?, ?, ?)"""
        CURSOR.execute(sql, [self.name, self.email, self.quickie, self.long_term, self.drinks])
        self.id = CURSOR.execute("SELECT * FROM users ORDER BY id DESC LIMIT 1").fetchone()[0]
        CONN.commit()

    def save(self):
        if self.id:
            self.update()
        else:
            self.create()

    def delete(self):
        sql = "DELETE FROM users WHERE id = ?"
        CURSOR.execute(sql, [self.id])
        CONN.commit()

    @classmethod
    def create_table(cls):
        create_users_sql = """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY, 
            name TEXT, 
            email TEXT, 
            quickie TEXT, 
            long_term TEXT, 
            drinks TEXT
            )""" 
        CURSOR.execute(create_users_sql)

    @classmethod
    def query_all(cls):
        sql = ("SELECT * FROM users")
        users = CURSOR.execute(sql).fetchall()
        users_list = []
        for user in users:
            user = User(user[1], user[2], user[3], user[4], user[5], user[0])
            users_list.append(user)
        print(users)

    @classmethod
    def query_for_match(cls):
        sql = ("SELECT * FROM users")
        result_set = CURSOR.execute(sql).fetchall()
        matching_users = []
        for row in result_set:
            user = User(row[1], row[2], row[3], row[4], row[5], row[0])
            matching_users.append(user)
        return matching_users

    @classmethod
    def grab_current_user(cls):
        sql = ("SELECT * FROM users ORDER BY id DESC LIMIT 1")
        current_user = CURSOR.execute(sql).fetchone()
        current_user = User(current_user[1], current_user[2], current_user[3], current_user[4], current_user[5], current_user[0])
        return current_user
    


    


