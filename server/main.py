from fastapi import FastAPI, status
import uvicorn
import routes
from fastapi.responses import RedirectResponse, HTMLResponse

app = FastAPI()

@app.get("/")
def root():
    redirect_url = "/redoc"
    return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)

@app.get("/hello")
def hello(name: str = ""):
    return {"message": f"Hello {name}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)