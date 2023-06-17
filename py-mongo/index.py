from fastapi import FastAPI
from routes.users import user
app = FastAPI()

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(user)