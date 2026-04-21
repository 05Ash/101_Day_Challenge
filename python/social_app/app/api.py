from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from h11 import Request
from .src.routes import posts


app = FastAPI()

@app.get("/", tags = ["root"], status_code = status.HTTP_200_OK)
async def read_root() -> dict:
    return {"message": "Welcome"}

@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content = {"error": exc.detail, "status_code": exc.status_code})

@app.exception_handler(Exception)
def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content = {"error": "Internal Server Error", "details": str(exc)})

app.include_router(posts.router)
