import requests

URL = "http://127.0.0.1:8000/api"

def test_login():
    print("1. Checking connection to backend...")
    try:
        requests.get(f"{URL}/")
        print("✅ Backend is ALIVE")
    except Exception as e:
        print(f"❌ Backend is DEAD. Error: {e}")
        return

    print("\n2. Trying to Login as 'admin'...")
    try:
        payload = {"username": "admin", "password": "admin"}
        response = requests.post(f"{URL}/auth/login/", json=payload)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 200:
            print("✅ LOGIN SUCCESSFUL!")
            print("Token/User Data received.")
        else:
            print("❌ LOGIN FAILED.")
    except Exception as e:
        print(f"❌ Connection Error during login: {e}")

if __name__ == "__main__":
    test_login()
