import httpx
from schemas import PostCreate, PostUpdate

base_url = "https://jsonplaceholder.typicode.com/posts"

async def get_posts():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{base_url}")
    if response:
        return response.json()
    return None

async def get_posts_titles():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{base_url}")
    if response:
        dict_posts = response.json()
        only_titles = [{"title": post["title"]} for post in dict_posts]
        return only_titles
    return None

async def get_post(post_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{base_url}/{post_id}")
    if response:
        return response.json()
    return None

async def send_post(post: PostCreate):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{base_url}", json=post.dict())
    if response:
        return response.json()
    return None

async def update_posts(post_id: int, post: PostUpdate):
    async with httpx.AsyncClient() as client:
        response = await client.patch(f"{base_url}/{post_id}", json=post.dict())
    if response:
        return response.json()
    return None

async def delete_post(post_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{base_url}/{post_id}")
    if response:
        return response.json()
    return None




