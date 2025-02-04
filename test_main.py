import logging
import pytest
from fastapi.testclient import TestClient
from main import app

# Configure logging for tests
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = TestClient(app)

def test_root_endpoint():
    logger.info("Testing root endpoint")
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastAPI!"}

def test_hello_endpoint():
    logger.info("Testing hello endpoint")
    test_name = "TestUser"
    response = client.get(f"/hello/{test_name}")
    assert response.status_code == 200
    assert response.json() == {"message": f"Hello, {test_name}!"}

def test_health_endpoint():
    logger.info("Testing health endpoint")
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"} 
    
    
if __name__ == "__main__":
    pytest.main()
