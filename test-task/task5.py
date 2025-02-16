from fastapi import FastAPI
import requests
import asyncio


async def nomer(info:dict,id):
    t = None

    for i in range(len(info)):
        r = info[i]

        if r['id'] == id:
            t = r
            break



    return t

async def comment(info,id):

    a=[]

    for i in range(len(info)):
        r = info[i]

        if r['user_id'] == id:
            a.append('Заголовок  '+r['title']+' Тело '+r['body'])


    return a


app = FastAPI()



@app.get("/{path}/{item_id}")
async def read_item(path,item_id:int):
    site1 = "https://gorest.co.in/public/v2/users"
    site2 = "https://gorest.co.in/public/v2/posts"
    request_user = requests.get(site1)
    request_post = requests.get(site2)
    info_user= request_user.json()
    info_post=request_post.json()
    if path =='user':
        # выборка по юзеру
        result = await nomer(info_user, item_id)
        Viborka = "Выборка по номеру юзера"

    elif path =='post':
        # выборка сообщений по юзеру
        result = await comment(info_post, item_id)
        Viborka = "Выборка собщений по номеру юзера"

    else:
        #Полная выборка всех юзеров
        result=info_user
        Viborka = "Список всех юзеров"
    return {Viborka: result}


