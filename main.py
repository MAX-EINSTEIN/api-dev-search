from fastapi import FastAPI
import httpx

app = FastAPI()

GITHUB_SEARCH_API_URL = 'https://api.github.com/search'

@app.get("/")
async def read_root():
    return {"About": "REST API for DevSearch - a developer search website for hiring managers"}

@app.get("/users/{location}")
async def get_github_users(location: str, technology: str | None = None, experience:int | None = None):
    # Building Request URI using the required location parameter
    request_uri = f'{GITHUB_SEARCH_API_URL}/users?q=location:{location} type:user'
    
    # Adding query parameters for filtering users
    if technology:
        request_uri += f' language:{technology}'
    if experience and experience > 0:
        request_uri += f' created:<2018-01-01'

    print(request_uri)
    response = {"Error: " : "Request not made"}
    async with httpx.AsyncClient() as client:
        response = await(client.get(request_uri))
        response = response.json()
    return response
