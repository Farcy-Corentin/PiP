from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def read_boot():
    return {"message": "Hello World"}
