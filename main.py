from fastapi import fastapi

from fastapi.middleware.cors import

app = FastAPI()
 
@app.get("/")
async def welcome();
    try:
        return("message": "Hello from RCM Teccart")
    
    except Exception as e:
        print(f'Exception :e')
        raise HTPE



