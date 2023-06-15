from fastapi import APIRouter
import bcrypt
from models.users import Users
from config.database import conn
from schemas.users import serializeDict, usersEntity
from bson import ObjectId
user = APIRouter()

@user.get('/')
async def find_all_users():
    return usersEntity(conn.local.users.find())

@user.get('/{id}')
async def find_one_user(id):
    return serializeDict(conn.local.user.find_one({"_id":ObjectId(id)}))

@user.post('/')
async def create_user(user: Users):
    user.password = bcrypt.hashpw(user.password.encode(),bcrypt.gensalt())
    conn.local.users.insert_one(dict(user))
    return usersEntity(conn.local.users.find())

@user.put('/{id}')
async def update_user_by_id(id,user:Users):
    user.password = bcrypt.hashpw(user.password.encode(),bcrypt.gensalt())
    conn.local.users.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return usersEntity(conn.local.users.find({"_id":ObjectId(id)}))

@user.delete('/{id}')
async def delete_user_by_id(id,user: Users):
    return serializeDict(conn.local.user.find_one_and_delete({"_id":ObjectId(id)}))

@user.delete('/{name}')
async def delete_user_by_name(name,user: Users):
    return serializeDict(conn.local.user.find_one_and_delete({"name":name}))