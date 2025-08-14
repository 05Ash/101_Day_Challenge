# Import FastAPI
from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from h11 import Request
from controller.user_controller import router as user_router


# Create app instance
app = FastAPI()

@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content = {"error": exc.detail, "status_code": exc.status_code})

@app.exception_handler(Exception)
def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error":"Internal Server Error", "details":str(exc)})

app.include_router(user_router)
