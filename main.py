from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World!!"}

@app.get('/posts')
def get_posts():
    return {'data': 'this is your post'}

@app.post('/createposts')
def create_posts(payload: dict = Body(...)):
    return {'newpost': f"title: {payload['title']}, content: {payload['content']}"}
