import requests
import sys

def test_cors():
    url = "http://localhost:8000/api/auth/login/"
    origin = "http://localhost:3001"
    headers = {
        "Origin": origin,
        "Content-Type": "application/json"
    }
    
    print(f"Testing CORS request from {origin} to {url}...")
    
    try:
        # Send an OPTIONS request (Preflight)
        response = requests.options(url, headers=headers)
        print(f"OPTIONS Status: {response.status_code}")
        print("Access-Control-Allow-Origin:", response.headers.get("Access-Control-Allow-Origin"))
        print("Access-Control-Allow-Credentials:", response.headers.get("Access-Control-Allow-Credentials"))
        
        if response.headers.get("Access-Control-Allow-Origin") == origin:
            print("✅ CORS Configuration is CORRECT")
        else:
            print("❌ CORS Configuration FAILURE")
            
    except Exception as e:
        print(f"❌ Connection Error: {e}")

if __name__ == "__main__":
    test_cors()
