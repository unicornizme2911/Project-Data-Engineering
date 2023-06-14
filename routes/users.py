from fastapi import APIRouter
import bcrypt
from models.users import Users
from config.database import conn
from schemas.users import userEntity, usersEntity
from bson import ObjectId
user = APIRouter()

@user.get('/')
async def find_all_users():
    return usersEntity(conn.local.users.find())

@user.post('/')
async def create_user(user: Users):
    user.password = bcrypt.hashpw(user.password.encode(),bcrypt.gensalt())
    conn.local.users.insert_one(dict(user))
    return usersEntity(conn.local.users.find())

@user.put('/{id}')
async def update_user(id,user:Users):
    user.password = bcrypt.hashpw(user.password.encode(),bcrypt.gensalt())
    conn.local.users.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return usersEntity(conn.local.users.find({"_id":ObjectId(id)}))