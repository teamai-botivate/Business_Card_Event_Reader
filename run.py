import uvicorn
import os
import sys

# Ensure the root directory is in the path so 'backend' acts as a package
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    # Get port from environment (Render sets this) or default to 8000
    port = int(os.environ.get("PORT", 8000))
    host = "0.0.0.0" if os.environ.get("RENDER") or os.environ.get("PORT") else "127.0.0.1"
    
    print(f"🚀 Starting Business Card Reader on {host}:{port}...")
    uvicorn.run("backend.main:app", host=host, port=port, reload=False if os.environ.get("PORT") else True)
