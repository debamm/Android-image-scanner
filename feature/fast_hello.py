from fastapi import FastAPI,status
from pydantic import BaseModel 
import uvicorn
app = FastAPI()


class HealthCheck(BaseModel):
    """Output model for the health check response."""

    status: str = "OK"



@app.get("/")
def test():
    return{"text":"hello world"}

@app.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def get_health() -> HealthCheck:
    return HealthCheck(status="OK")


def main() -> None:
    """Entrypoint to invoke when this module is invoked on the remote server."""
    uvicorn.run("fast_hello:app", host="0.0.0.0",port=8080, reload=True)

if __name__ =="__main__":
    main()