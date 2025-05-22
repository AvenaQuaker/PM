from fastapi import APIRouter, HTTPException
from app.models.users import userModel

class UsersController:
    def __init__(self, db):
        self.user_model = userModel(db)

    async def useLogin(self, username, password):
        user = await self.user_model.login(username, password)
        return user

    async def useRegister(self, username, password):
        user = await self.user_model.register(username, password)
        return user
    
    async def getUserByName(self, username):
        user = await self.user_model.getUserByName(username)
        print(user)
        return user

