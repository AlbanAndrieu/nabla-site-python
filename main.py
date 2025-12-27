from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Root endpoint returning hello world message."""
    return {"message": "Hello World"}


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy"}


@app.get("/api/info")
async def info():
    """API info endpoint."""
    return {
        "name": "nabla-site-python",
        "version": "1.0.0",
        "description": "Sample FastAPI Hello World for Vercel and Cloudflare deployment"
    }
