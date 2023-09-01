import os
from fastapi import APIRouter, FastAPI, WebSocket, Request

chat = APIRouter()

# @route    POST /token
# @desc     Route to generate chat token
# @access   Public

@chat.post("/token")
async def token_generator(request: Request):
    return None

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