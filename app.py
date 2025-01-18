from fastapi import FastAPI
from router import router as chat_router

app = FastAPI(title="ChatGPT-Powered Store Chat Agent")

# Include routes from the chat router
app.include_router(chat_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
