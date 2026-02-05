"""
API Client for communicating with Django backend
"""

import requests
from typing import Dict, List, Optional


class APIClient:
    """Client for making requests to the Django backend API"""
    
    def __init__(self, base_url: str = "http://localhost:8000/api"):
        self.base_url = base_url
        self.session = requests.Session()
        self.user = None
    
    def login(self, username: str, password: str) -> Dict:
        """Login user and store session"""
        url = f"{self.base_url}/auth/login/"
        response = self.session.post(url, json={
            'username': username,
            'password': password
        })
        response.raise_for_status()
        self.user = response.json()
        return self.user
    
    def register(self, username: str, password: str, email: str = "") -> Dict:
        """Register a new user"""
        url = f"{self.base_url}/auth/register/"
        response = self.session.post(url, json={
            'username': username,
            'password': password,
            'email': email
        })
        response.raise_for_status()
        return response.json()
    
    def logout(self) -> None:
        """Logout current user"""
        url = f"{self.base_url}/auth/logout/"
        self.session.post(url)
        self.user = None
    
    def get_current_user(self) -> Optional[Dict]:
        """Get current authenticated user"""
        try:
            url = f"{self.base_url}/auth/user/"
            response = self.session.get(url)
            response.raise_for_status()
            self.user = response.json()
            return self.user
        except:
            return None
    
    def upload_csv(self, file_path: str) -> Dict:
        """Upload CSV file and get processed data"""
        url = f"{self.base_url}/upload/"
        
        with open(file_path, 'rb') as file:
            files = {'file': file}
            response = self.session.post(url, files=files)
            response.raise_for_status()
            return response.json()
    
    def get_dataset(self, dataset_id: int) -> Dict:
        """Get dataset by ID"""
        url = f"{self.base_url}/datasets/{dataset_id}/"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()
    
    def get_history(self) -> List[Dict]:
        """Get upload history"""
        url = f"{self.base_url}/history/"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()
    
    def download_pdf(self, dataset_id: int, save_path: str) -> None:
        """Download PDF report for a dataset"""
        url = f"{self.base_url}/datasets/{dataset_id}/download_pdf/"
        response = self.session.get(url)
        response.raise_for_status()
        
        with open(save_path, 'wb') as file:
            file.write(response.content)
