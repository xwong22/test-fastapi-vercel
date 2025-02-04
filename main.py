import logging
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from typing import Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Simple FastAPI App")

# Get FastAPI version
from fastapi import __version__

@app.get("/", response_class=HTMLResponse)
async def root() -> str:
    logger.info("Root endpoint accessed - serving HTML page")
    html = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>FastAPI on Vercel</title>
            <link rel="icon" href="/static/favicon.ico" type="image/x-icon" />
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    min-height: 100vh;
                    margin: 0;
                    background-color: #f0f2f5;
                }}
                .container {{
                    background-color: #ffffff;
                    padding: 2rem;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                    max-width: 600px;
                }}
                h1 {{
                    color: #2d3748;
                    margin-bottom: 1rem;
                }}
                ul {{
                    list-style-type: none;
                    padding: 0;
                }}
                li {{
                    margin: 0.5rem 0;
                }}
                a {{
                    color: #4299e1;
                    text-decoration: none;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
                .footer {{
                    margin-top: 1.5rem;
                    padding-top: 1rem;
                    border-top: 1px solid #e2e8f0;
                    font-size: 0.875rem;
                    color: #718096;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Hello from FastAPI@{__version__}</h1>
                <ul>
                    <li><a href="/docs">📚 API Documentation</a></li>
                    <li><a href="/redoc">📖 ReDoc Documentation</a></li>
                    <li><a href="/hello/user">👋 Try the Hello Endpoint</a></li>
                    <li><a href="/health">🏥 Health Check</a></li>
                </ul>
                <div class="footer">
                    <p>Powered by <a href="https://vercel.com" target="_blank">Vercel</a></p>
                </div>
            </div>
        </body>
    </html>
    """
    return html

@app.get("/hello/{name}")
async def say_hello(name: str) -> Dict[str, str]:
    logger.info(f"Hello endpoint accessed with name: {name}")
    return {"message": f"Hello, {name}!"}

@app.get("/health")
async def health_check() -> Dict[str, str]:
    logger.info("Health check endpoint accessed")
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting FastAPI application")
    uvicorn.run(app, host="0.0.0.0", port=8000)
