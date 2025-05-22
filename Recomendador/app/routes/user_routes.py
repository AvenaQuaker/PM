from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse,RedirectResponse
from app.controllers.users import UsersController
from data.database import get_db


def userRouter():
    router = APIRouter()

    @router.post("/auth/login")
    async def login_user(request: Request,db=Depends(get_db)):
        data = await request.form()
        username = data.get("username")
        password = data.get("password")

        controller = UsersController(db)
        user = await controller.useLogin(username, password)

        if not user:
            return {"message": "Usuario o contraseña incorrectos"}
        
        response = RedirectResponse(url="/songs",status_code=302)
        response.set_cookie(key="username", value=username)

        return response

    @router.post("/auth/register")
    async def register_user(request: Request,db=Depends(get_db)):
        data = await request.json()
        username = data.get("username")
        password = data.get("password")

        controller = UsersController(db)
        result =  await controller.useRegister(username, password)

        if "error" in result:
            return JSONResponse(status_code=400, content={"message": result["error"]})
        return {"message": "Registro exitoso", "user": result}
    
    @router.get("/auth/user/{username}")
    async def get_user_by_name(username: str, db=Depends(get_db)):
        controller = UsersController(db)
        user = await controller.getUserByName(username)

        if not user:
            return JSONResponse(status_code=404, content={"message": "Usuario no encontrado"})
        return user

    return router
