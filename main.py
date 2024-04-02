from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Create an instance of the FastAPI class
app = FastAPI()

# Define allowed origins
origins = [
    "http://127.0.0.1:5500",
    # Add other origins as needed
]

# Add CORS middleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str
    password:str

# Define a route and its handler function
@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}


@app.post("/login")
def login(item:Item):
    return {"data":item.name}

# Run the server with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
