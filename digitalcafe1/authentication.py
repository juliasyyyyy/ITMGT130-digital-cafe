import database as db

def login(username, password):
    is_valid_login = False
    user=None
    temp_user = db.get_user(username)
    if(temp_user != None):
        if(temp_user["password"]==password):
            is_valid_login=True
            user={"username":username,
                  "first_name":temp_user["first_name"],
                  "last_name":temp_user["last_name"]}
        else:
             flash("Invalid Username or password! Please try again")

    return is_valid_login, user


def change(password):
    password=None
    temp_user= db.change_pass(password)
    return temp_user["password"]==password
