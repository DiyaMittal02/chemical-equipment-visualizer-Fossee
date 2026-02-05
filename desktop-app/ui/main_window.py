"""
Main Window for the desktop application
"""

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QStackedWidget, QMessageBox, QStatusBar
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont
from api_client import APIClient
from ui.styles import DARK_THEME
from ui.auth_widget import AuthWidget
from ui.upload_widget import UploadWidget
from ui.visualization_widget import VisualizationWidget
from ui.history_widget import HistoryWidget


class MainWindow(QMainWindow):
    """Main application window"""
    
    def __init__(self):
        super().__init__()
        self.api_client = APIClient()
        self.current_dataset = None
        
        self.init_ui()
        self.apply_styles()
        self.check_authentication()
    
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle("Chemical Equipment Parameter Visualizer")
        self.setGeometry(100, 100, 1400, 900)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Header
        self.create_header(main_layout)
        
        # Stacked widget for different views
        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget)
        
        # Auth widget
        self.auth_widget = AuthWidget(self.api_client)
        self.auth_widget.login_success.connect(self.on_login_success)
        self.stacked_widget.addWidget(self.auth_widget)
        
        # Main content widget (shown after login)
        self.main_content = self.create_main_content()
        self.stacked_widget.addWidget(self.main_content)
        
        # Status bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("Ready")
    
    def create_header(self, layout):
        """Create the application header"""
        header = QWidget()
        header.setMinimumHeight(100)
        header.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                      stop:0 rgba(26, 35, 126, 0.9),
                                      stop:1 rgba(83, 75, 174, 0.9));
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        """)
        
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(24, 12, 24, 12)
        
        # Logo and title
        title_container = QVBoxLayout()
        
        title_label = QLabel("⚗️ Chemical Equipment Visualizer")
        title_label.setObjectName("titleLabel")
        title_container.addWidget(title_label)
        
        subtitle_label = QLabel("Advanced Parameter Analysis & Visualization")
        subtitle_label.setObjectName("subtitleLabel")
        title_container.addWidget(subtitle_label)
        
        header_layout.addLayout(title_container)
        header_layout.addStretch()
        
        # User info (will be set after login)
        self.user_label = QLabel()
        self.user_label.setStyleSheet("color: #00bfa5; font-weight: 600;")
        header_layout.addWidget(self.user_label)
        
        # Logout button
        self.logout_btn = QPushButton("Logout")
        self.logout_btn.clicked.connect(self.logout)
        self.logout_btn.setVisible(False)
        header_layout.addWidget(self.logout_btn)
        
        layout.addWidget(header)
    
    def create_main_content(self):
        """Create main content area with tabs"""
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setContentsMargins(24, 24, 24, 24)
        
        # Tab buttons
        tab_container = QWidget()
        tab_container.setStyleSheet("""
            background: rgba(26, 31, 58, 0.4);
            border-radius: 12px;
            padding: 8px;
        """)
        tab_layout = QHBoxLayout(tab_container)
        tab_layout.setSpacing(12)
        
        self.upload_tab_btn = QPushButton("📤 Upload Data")
        self.upload_tab_btn.setObjectName("accentButton")
        self.upload_tab_btn.clicked.connect(lambda: self.switch_tab(0))
        tab_layout.addWidget(self.upload_tab_btn)
        
        self.view_tab_btn = QPushButton("📊 View Analysis")
        self.view_tab_btn.clicked.connect(lambda: self.switch_tab(1))
        self.view_tab_btn.setEnabled(False)
        tab_layout.addWidget(self.view_tab_btn)
        
        self.history_tab_btn = QPushButton("📜 History")
        self.history_tab_btn.clicked.connect(lambda: self.switch_tab(2))
        tab_layout.addWidget(self.history_tab_btn)
        
        tab_layout.setStretchFactor(self.upload_tab_btn, 1)
        tab_layout.setStretchFactor(self.view_tab_btn, 1)
        tab_layout.setStretchFactor(self.history_tab_btn, 1)
        
        layout.addWidget(tab_container)
        
        # Content stack
        self.content_stack = QStackedWidget()
        
        # Upload widget
        self.upload_widget = UploadWidget(self.api_client)
        self.upload_widget.upload_success.connect(self.on_upload_success)
        self.content_stack.addWidget(self.upload_widget)
        
        # Visualization widget
        self.viz_widget = VisualizationWidget(self.api_client)
        self.content_stack.addWidget(self.viz_widget)
        
        # History widget
        self.history_widget = HistoryWidget(self.api_client)
        self.history_widget.dataset_selected.connect(self.on_dataset_selected)
        self.content_stack.addWidget(self.history_widget)
        
        layout.addWidget(self.content_stack)
        
        return content
    
    def switch_tab(self, index):
        """Switch between tabs"""
        self.content_stack.setCurrentIndex(index)
        
        # Update button styles
        buttons = [self.upload_tab_btn, self.view_tab_btn, self.history_tab_btn]
        for i, btn in enumerate(buttons):
            if i == index:
                btn.setObjectName("accentButton")
            else:
                btn.setObjectName("")
            btn.setStyle(btn.style())  # Force style refresh
    
    def apply_styles(self):
        """Apply application styles"""
        self.setStyleSheet(DARK_THEME)
    
    def check_authentication(self):
        """Check if user is already authenticated"""
        user = self.api_client.get_current_user()
        if user:
            self.on_login_success(user)
        else:
            self.stacked_widget.setCurrentIndex(0)
    
    def on_login_success(self, user):
        """Handle successful login"""
        self.user_label.setText(f"👤 {user['username']}")
        self.logout_btn.setVisible(True)
        self.stacked_widget.setCurrentIndex(1)
        self.statusBar.showMessage(f"Logged in as {user['username']}")
    
    def on_upload_success(self, dataset):
        """Handle successful file upload"""
        self.current_dataset = dataset
        self.view_tab_btn.setEnabled(True)
        self.viz_widget.set_dataset(dataset)
        self.switch_tab(1)
        self.history_widget.refresh()
        self.statusBar.showMessage("Dataset uploaded successfully")
    
    def on_dataset_selected(self, dataset):
        """Handle dataset selection from history"""
        self.current_dataset = dataset
        self.view_tab_btn.setEnabled(True)
        self.viz_widget.set_dataset(dataset)
        self.switch_tab(1)
        self.statusBar.showMessage(f"Loaded dataset: {dataset['filename']}")
    
    def logout(self):
        """Logout current user"""
        reply = QMessageBox.question(
            self,
            "Logout",
            "Are you sure you want to logout?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            self.api_client.logout()
            self.user_label.setText("")
            self.logout_btn.setVisible(False)
            self.current_dataset = None
            self.view_tab_btn.setEnabled(False)
            self.stacked_widget.setCurrentIndex(0)
            self.statusBar.showMessage("Logged out")
