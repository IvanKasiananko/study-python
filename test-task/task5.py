from fastapi import FastAPI
import requests
import asyncio


async def number(info:dict,id):
    number_user = None

    for i in range(len(info)):
        r = info[i]

        if r['id'] == id:
            number_user = r
            break



    return number_user

async def comment(info,id):

    comment_list=[]

    for i in range(len(info)):
        r = info[i]

        if r['user_id'] == id:
            comment_list.append('Заголовок  '+r['title']+' Тело '+r['body'])


    return comment_list



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
        result = await number(info_user, item_id)
        sample = "Выборка по номеру юзера"

    elif path =='post':
        # выборка сообщений по юзеру
        result = await comment(info_post, item_id)
        sample = "Выборка собщений по номеру юзера"

    else:
        #Полная выборка всех юзеров
        result=info_user
        sample = "Список всех юзеров"
    return {sample: result}


