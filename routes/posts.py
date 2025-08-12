from schemas import PostCreate, Post, PostUpdate
from fastapi import APIRouter, status, HTTPException
from typing import List
from crud import get_posts, get_post, send_post, update_posts, delete_post

router = APIRouter(prefix="/postsAPI", tags=["postsAPI"])

@router.get("/", response_model=List[Post], status_code=status.HTTP_200_OK)
async def read_posts():
    posts = await get_posts()
    if not posts:
        raise HTTPException(status_code=404, details="posts not found")
    return posts

@router.get("/{post_id}", response_model=Post, status_code=status.HTTP_200_OK)
async def read_post(post_id: int):
    post = await get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, details="post not found")
    return post

@router.post("/", response_model=PostCreate, status_code=status.HTTP_201_CREATED)
async def create_post(post: PostCreate):
    post_created = await send_post(post)
    if not post_created:
        raise HTTPException(status_code=404, details="post not send")
    return post

@router.patch("/", response_model=PostUpdate, status_code=status.HTTP_200_OK)
async def patch_post(post_id: int, post: PostUpdate):
    post_update = await update_posts(post_id, post)
    if not post_update:
        raise HTTPException(status_code=404, details="post not found")  
    return post

@router.delete("/{post_id}", status_code=status.HTTP_200_OK)
async def del_post(post_id: int):
    deleted_post = await delete_post(post_id)
    if not delete_post:
        raise HTTPException(status_code=404, details="post not found")
    print("post deleted")
    return delete_post