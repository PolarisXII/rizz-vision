from pathlib import Path
import pickle
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Base64UrlBytes

from db import Data, User


import asyncio
from openai import OpenAI, AsyncOpenAI
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate
from langchain.schema import AIMessage, HumanMessage
from dotenv import load_dotenv
import os

data: Data = Data()
load_dotenv()


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
    u = User(name=user.name, password=user.password, images=[], keywords={})
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
    api_key = os.getenv("OPENAI_API_KEY")

    # ai analysis
    print(api_key)
    client = AsyncOpenAI(api_key=api_key)
    output_parser = CommaSeparatedListOutputParser()

    prompt_template = PromptTemplate(
        template="Based on the image posted by the user, provide 20 hobbies, interests and characteristics that can be inferred from the image. The interests, hobbies or characteristics should only be one word. Separate the hobbies, interests and characteristics by commas.",
        input_variables=[],
    )
    # print(image)
    # print(image.image)
    messages = [
      {"role": "system", "content": "You are an AI that extracts keywords from images."},
        {"role": "user", "content": [
            {"type": "text", "text": prompt_template.format()},
            {"type": "image_url", 
             "image_url": {
                 "url": f"data:image/jpeg;base64,{image.image}", 
                "detail": "low"}
            }
        ]}
    ]
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    # Extract text response
    raw_text = response.choices[0].message.content

    keywordsList = output_parser.parse(raw_text)

    for keywords in keywordsList:
        formatted_keyword = keywords.lower()
        if len(formatted_keyword.split()) < 2:
            if formatted_keyword not in data.users[id].keywords:
                data.users[id].keywords[formatted_keyword] = 0
            data.users[id].keywords[formatted_keyword]+=1


    data.users[id].images.append(image.image)





    return str(data.users[id].keywords)

@app.post("/match/{id}")
async def match(id: str):
    matchScore = []

    keywords = data.users[id].keywords.keys()
    for userId in data.users.keys():
        if userId != id:
            score = 0
            for keyword in keywords:
                if keyword in data.users[userId].keywords:
                    score = score + data.users[userId].keywords[keyword] + data.users[id].keywords[keyword]
            matchScore.append({
                'name': data.users[id].name,
                'images': data.users[id].images,
                'score': score
            })


    matchScore.sort(key=lambda x: x['score'], reverse=True)
    return matchScore

