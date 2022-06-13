def user_data(user) -> dict:
    return{
        "id":str(user["_id"]),
        "username": user["username"],
        "date_joined": user["date_joined"],
        "location": user["location"],
        "age": user["age"]
}

def users_data(users) ->list:
    return [user_data(user) for user in users]