from fastapi import APIRouter, HTTPException, status
import bcrypt
from models.users import Users
from config.database import conn
from schemas.users import serializeDict, usersEntity
from bson import ObjectId
from typing import List

user = APIRouter()

@user.get('/',response_description="List all users", response_model=List[Users])
async def find_all_users():
    return list(usersEntity(conn.local.users.find(limit=100)))


@user.get('/{id}', response_description="Get a single user by id", response_model=Users)
async def find_one_user(id:str):
    if user:= serializeDict(conn.local.user.find_one({"_id":ObjectId(id)})) is not None:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {id} not found.")


@user.post('/', response_description="Create a new book", status_code=status.HTTP_201_CREATED, response_model=Users)
async def create_user(user: Users):
    if conn.local.users.find({"email":user.email}) is not None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with Email: {user.email} has exsits.")
    user.password = bcrypt.hashpw(user.password.encode(),bcrypt.gensalt())
    conn.local.users.insert_one(dict(user))


@user.put('/{id}', response_description="Update a book with id", response_model=Users)
async def update_user_by_id(id,user:Users):
    if conn.local.users.find({"_id":id}) is not None:
        user.password = bcrypt.hashpw(user.password.encode(),bcrypt.gensalt())
        conn.local.users.find_one_and_update({"_id":ObjectId(id)},{
            "$set":dict(user)
        })
        return usersEntity(conn.local.users.find({"_id":ObjectId(id)}))
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {id} not found.")

@user.delete('/{id}', response_description="Delete a user with id", response_model=Users)
async def delete_user_by_id(id,user: Users):
    return serializeDict(conn.local.user.find_one_and_delete({"_id":ObjectId(id)}))


@user.delete('/{name}', response_description="Delete a user with name", response_model=Users)
async def delete_user_by_name(name,user: Users):
    return serializeDict(conn.local.user.find_one_and_delete({"name":name}))

@user.delete('/', response_description="Delete all users", response_model=List[Users])
async def delete_all_users():
    conn.local.users.remove()
