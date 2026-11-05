from tinydb import TinyDB, Query

DB_FILE = "rpg_save_data.json"
db = TinyDB(DB_FILE)
users_table = db.table("users")

def register_user(username, password):
    User = Query()
    if not username.strip() or not password.strip():
        return False, "Username and password cannot be empty!"
    if users_table.search(User.username == username):
        return False, "Username already exists!"
    
    new_user = {
        "username": username,
        "password": password,
        "hp": 50,
        "max_hp": 50,
        "xp": 0,
        "level": 1,
        "gold": 100,
        "skills": ["Slash"],
        "inventory": ["Health Potion"],
        "current_map": "town_map",
        "player_row": 1,
        "player_col": 1,
        "quest_step": 0,
        "monsters_killed": 0,
        "side_quest_1_done": False,
        "side_quest_2_done": False
    }
    users_table.insert(new_user)
    return True, "Registration successful!"

def login_user(username, password):
    User = Query()
    user = users_table.get((User.username == username) & (User.password == password))
    if user:
        return True, user
    return False, "Invalid username or password!"

def save_game_data(username, data):
    User = Query()
    users_table.update(data, User.username == username)