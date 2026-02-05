"""
Authentication widget for login/register
"""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QMessageBox, QFrame
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont


class AuthWidget(QWidget):
    """Widget for user authentication"""
    
    login_success = pyqtSignal(dict)
    
    def __init__(self, api_client):
        super().__init__()
        self.api_client = api_client
        self.is_login_mode = True
        self.init_ui()
    
    def init_ui(self):
        """Initialize UI"""
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        
        # Card container
        card = QFrame()
        card.setMaximumWidth(500)
        card.setStyleSheet("""
            QFrame {
                background: rgba(26, 31, 58, 0.6);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 16px;
                padding: 32px;
            }
        """)
        
        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(20)
        
        # Title
        self.title_label = QLabel("🔐 Sign In")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("""
            font-size: 28pt;
            font-weight: 700;
            color: #00bfa5;
            margin-bottom: 8px;
        """)
        card_layout.addWidget(self.title_label)
        
        # Description
        self.desc_label = QLabel("Welcome back! Sign in to access your equipment data.")
        self.desc_label.setAlignment(Qt.AlignCenter)
        self.desc_label.setWordWrap(True)
        self.desc_label.setStyleSheet("color: #b0b8d4; font-size: 12pt;")
        card_layout.addWidget(self.desc_label)
        
        card_layout.addSpacing(20)
        
        # Username
        username_label = QLabel("Username")
        username_label.setStyleSheet("font-weight: 600; font-size: 10pt; color: white;")
        card_layout.addWidget(username_label)
        
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")
        self.username_input.setMinimumHeight(45)
        card_layout.addWidget(self.username_input)
        
        # Email (for registration)
        self.email_label = QLabel("Email")
        self.email_label.setStyleSheet("font-weight: 600; font-size: 10pt; color: white;")
        self.email_label.setVisible(False)
        card_layout.addWidget(self.email_label)
        
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email")
        self.email_input.setMinimumHeight(45)
        self.email_input.setVisible(False)
        card_layout.addWidget(self.email_input)
        
        # Password
        password_label = QLabel("Password")
        password_label.setStyleSheet("font-weight: 600; font-size: 10pt; color: white;")
        card_layout.addWidget(password_label)
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMinimumHeight(45)
        self.password_input.returnPressed.connect(self.authenticate)
        card_layout.addWidget(self.password_input)
        
        card_layout.addSpacing(10)
        
        # Submit button
        self.submit_btn = QPushButton("Sign In")
        self.submit_btn.setObjectName("accentButton")
        self.submit_btn.setMinimumHeight(50)
        self.submit_btn.clicked.connect(self.authenticate)
        card_layout.addWidget(self.submit_btn)
        
        # Toggle link
        toggle_container = QHBoxLayout()
        toggle_container.setAlignment(Qt.AlignCenter)
        
        self.toggle_label = QLabel("Don't have an account? ")
        self.toggle_label.setStyleSheet("color: #b0b8d4;")
        toggle_container.addWidget(self.toggle_label)
        
        self.toggle_btn = QPushButton("Sign Up")
        self.toggle_btn.setFlat(True)
        self.toggle_btn.setStyleSheet("""
            QPushButton {
                color: #00bfa5;
                font-weight: 600;
                background: none;
                border: none;
                padding: 0;
                text-decoration: underline;
            }
            QPushButton:hover {
                color: #5df2d6;
            }
        """)
        self.toggle_btn.clicked.connect(self.toggle_mode)
        toggle_container.addWidget(self.toggle_btn)
        
        card_layout.addLayout(toggle_container)
        
        layout.addWidget(card)
    
    def toggle_mode(self):
        """Toggle between login and register mode"""
        self.is_login_mode = not self.is_login_mode
        
        if self.is_login_mode:
            self.title_label.setText("🔐 Sign In")
            self.desc_label.setText("Welcome back! Sign in to access your equipment data.")
            self.submit_btn.setText("Sign In")
            self.toggle_label.setText("Don't have an account? ")
            self.toggle_btn.setText("Sign Up")
            self.email_label.setVisible(False)
            self.email_input.setVisible(False)
        else:
            self.title_label.setText("✨ Create Account")
            self.desc_label.setText("Join us to start analyzing your equipment parameters.")
            self.submit_btn.setText("Create Account")
            self.toggle_label.setText("Already have an account? ")
            self.toggle_btn.setText("Sign In")
            self.email_label.setVisible(True)
            self.email_input.setVisible(True)
    
    def authenticate(self):
        """Handle authentication"""
        username = self.username_input.text().strip()
        password = self.password_input.text()
        
        if not username or not password:
            QMessageBox.warning(self, "Error", "Please fill in all required fields")
            return
        
        try:
            if self.is_login_mode:
                user = self.api_client.login(username, password)
                self.login_success.emit(user)
            else:
                email = self.email_input.text().strip()
                self.api_client.register(username, password, email)
                QMessageBox.information(
                    self,
                    "Success",
                    "Registration successful! Please login."
                )
                self.toggle_mode()
                self.password_input.clear()
        
        except Exception as e:
            error_msg = str(e)
            if hasattr(e, 'response') and e.response is not None:
                try:
                    error_data = e.response.json()
                    error_msg = error_data.get('error', str(e))
                except:
                    pass
            
            QMessageBox.critical(self, "Error", f"Authentication failed: {error_msg}")
