from fastapi import APIRouter
from config.database import collection_name
from models.user_model import User
from schemas.user_schema import user_data,users_data
from bson import ObjectId

user_api_router =APIRouter()

@user_api_router.get('/')
async def get_users():
    users=users_data(collection_name.find())
    return {"status": "ok","data":users}

@user_api_router.get("/{id}")
async def get_user(id:str):
    user = users_data(collection_name.find({"_id": ObjectId(id)}))
    return {"status": "ok","data":user}

@user_api_router.post('/')
async def post_user(user:User):
    _id = collection_name.insert_one(dict(user))
    user = users_data(collection_name.find({"_id": _id.inserted_id}))
    return {"status": "ok","data":user}

@user_api_router.put("/{id}")
async def update_todo(id: str, todo: User):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(todo)
    })
    return users_data(collection_name.find({"_id": ObjectId(id)}))

# delete
@user_api_router.delete("/{id}")
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}