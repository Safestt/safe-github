from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI()
active_connections = []  # Lista de conexiones activas

@app.get("/")
async def get():
    return HTMLResponse(content=Path("index.html").read_text(encoding="utf-8"))


@app.websocket("/ws")
async def websocket_connection(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_text() 
            for connection in active_connections:
                if connection != websocket:  # No reenviar el mensaje al mismo cliente que lo envió
                    await connection.send_text(f"Anonimo  {data}")
    except:
        print("❌ Cliente desconectado")
    finally:
        active_connections.remove(websocket)
