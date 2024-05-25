from fastapi import FastAPI, HTTPException

import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

app = FastAPI()

def check_network_connection():
    try:
        # Replace the IP address and port with an external service or resource you want to check connectivity to
        sock = socket.create_connection((IPAddr, 8000), timeout=2)
        sock.close()
        return True
    except Exception as e:
        return False
    
@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/network-health")
async def network_health_check():
    network_status = check_network_connection()
    if not network_status:
        raise HTTPException(status_code=503, detail="Network connection error")
    return {"status": "ok"}

