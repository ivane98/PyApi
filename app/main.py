from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title : str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{'title': 'title 1', 'content': 'content 1', 'id': 1}, {'title': 'title 2', 'content': 'content 2', 'id': 2}]

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p
        
def find_post_index(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


@app.get("/")
def root():
    return {"message": "Hello World!!"}

@app.get('/posts')
def get_posts():
    return {'data': my_posts}

@app.get('/posts/{id}')
def get_post(id: int):
    post = find_post(id)
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
        
    return {'post': post}

@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_posts(post:Post):
    post_dict = post.model_dump()
    post_dict['id'] = randrange(1, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_post_index(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")

    my_posts.pop(index)

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put('/posts/{id}')
def update_post(id: int, post: Post):
    index = find_post_index(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    
    post_dict = post.model_dump()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"data": post_dict}