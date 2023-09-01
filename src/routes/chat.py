import os
from fastapi import APIRouter, FastAPI, WebSocket, Request, BackgroundTasks, HTTPException
import uuid

chat = APIRouter()

# @route    POST /token
# @desc     Route generating chat token
# @access   Public

@chat.post("/token")
async def token_generator(name: str, request: Request):
    
    if name == "":
        raise HTTPException(status_code=400, detail={
            "loc": "name", "msg": "Enter a valid name"
        })
        
    token = str(uuid.uuid4())
    
    data = {"name": name, "token": token}
    
    return data

# @route    POST /refresh_tokens
# @desc    Route to refresh chat token
# @access   Public

@chat.post("/refresh_tokens")
async def refresh_token(request: Request):
    return None

# @route    Websocket /chat
# @desc     Socket for Chatbot
# @access   Public

@chat.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket = WebSocket):
    return None