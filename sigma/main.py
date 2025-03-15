from pathlib import Path
import pickle
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Base64UrlBytes

from db import Data, User

data: Data = Data()


@asynccontextmanager
async def lifespan(app: FastAPI):
    global data

    path = Path("uwudb.fr")
    if path.exists() and (
        not path.stat().st_size
        or path.stat().st_ctime < Path(__file__).stat().st_ctime
    ):
        path.unlink()

    if path.exists():
        with open(path, "rb") as f:
            data = pickle.load(f)

    yield

    with open(path, "wb") as f:
        pickle.dump(data, f)


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def hi():
    return {"Hello": "World"}


class UserModel(BaseModel):
    name: str
    password: str


@app.post("/self")
async def newuser(user: UserModel):
    u = User(name=user.name, password=user.password, images=[])
    data.users[u.id] = u
    return u.id


@app.get("/users")
async def users():
    return data.users


class ImageModel(BaseModel):
    image: Base64UrlBytes


@app.post("/upimage/{id}")
async def upimage(id: str, image: ImageModel):
    if id not in data.users:
        raise HTTPException(status_code=400, detail="User not found")

    data.users[id].images.append(image.image)
    return ""
