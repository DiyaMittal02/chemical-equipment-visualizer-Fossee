import requests
import sys

def check_server():
    url = "http://127.0.0.1:8000/api/"
    print(f"Checking connection to {url}...")
    
    try:
        response = requests.get(url, timeout=2)
        if response.status_code == 200:
            print("✅ SUCCESS: Backend is running and reachable!")
            print("Response Headers:", response.headers)
            return True
        else:
            print(f"⚠️ WARNING: Backend is running but returned status code {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ ERROR: Connection Refused. Backend is NOT running or not reachable at 127.0.0.1:8000")
        print("Tip: Make sure 'python manage.py runserver' is running in another terminal.")
        return False
    except Exception as e:
        print(f"❌ ERROR: An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    check_server()
