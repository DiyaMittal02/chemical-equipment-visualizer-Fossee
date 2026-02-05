"""
Upload widget for CSV file selection and upload
"""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton,
    QFileDialog, QMessageBox, QFrame, QProgressBar
)
from PyQt5.QtCore import Qt, pyqtSignal, QThread
from PyQt5.QtGui import QFont, QDragEnterEvent, QDropEvent
import os


class UploadThread(QThread):
    """Thread for uploading file"""
    
    success = pyqtSignal(dict)
    error = pyqtSignal(str)
    
    def __init__(self, api_client, file_path):
        super().__init__()
        self.api_client = api_client
        self.file_path = file_path
    
    def run(self):
        """Upload file in background"""
        try:
            result = self.api_client.upload_csv(self.file_path)
            self.success.emit(result)
        except Exception as e:
            error_msg = str(e)
            if hasattr(e, 'response') and e.response is not None:
                try:
                    error_data = e.response.json()
                    error_msg = error_data.get('error', str(e))
                except:
                    pass
            self.error.emit(error_msg)


class UploadWidget(QWidget):
    """Widget for file upload"""
    
    upload_success = pyqtSignal(dict)
    
    def __init__(self, api_client):
        super().__init__()
        self.api_client = api_client
        self.selected_file = None
        self.upload_thread = None
        self.init_ui()
    
    def init_ui(self):
        """Initialize UI"""
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        
        # Card container
        card = QFrame()
        card.setMaximumWidth(800)
        card.setStyleSheet("""
            QFrame {
                background: rgba(26, 31, 58, 0.6);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 16px;
                padding: 32px;
            }
        """)
        
        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(24)
        
        # Title
        title = QLabel("📁 Upload Equipment Data")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size: 24pt;
            font-weight: 700;
            color: white;
        """)
        card_layout.addWidget(title)
        
        # Description
        desc = QLabel(
            "Upload a CSV file containing equipment parameters "
            "(Equipment Name, Type, Flowrate, Pressure, Temperature)"
        )
        desc.setAlignment(Qt.AlignCenter)
        desc.setWordWrap(True)
        desc.setStyleSheet("color: #b0b8d4; font-size: 12pt;")
        card_layout.addWidget(desc)
        
        # Drop zone
        self.drop_zone = QFrame()
        self.drop_zone.setMinimumHeight(250)
        self.drop_zone.setAcceptDrops(True)
        self.drop_zone.setStyleSheet("""
            QFrame {
                border: 3px dashed rgba(255, 255, 255, 0.2);
                border-radius: 16px;
                background: rgba(255, 255, 255, 0.02);
            }
            QFrame:hover {
                border-color: #00bfa5;
                background: rgba(0, 191, 165, 0.05);
            }
        """)
        
        drop_layout = QVBoxLayout(self.drop_zone)
        drop_layout.setAlignment(Qt.AlignCenter)
        
        # File info
        self.file_icon = QLabel("📤")
        self.file_icon.setAlignment(Qt.AlignCenter)
        self.file_icon.setStyleSheet("font-size: 48pt;")
        drop_layout.addWidget(self.file_icon)
        
        self.file_label = QLabel("Click to browse or drag and drop")
        self.file_label.setAlignment(Qt.AlignCenter)
        self.file_label.setStyleSheet("color: white; font-size: 14pt; font-weight: 600;")
        drop_layout.addWidget(self.file_label)
        
        self.file_subtext = QLabel("CSV files only (max 10MB)")
        self.file_subtext.setAlignment(Qt.AlignCenter)
        self.file_subtext.setStyleSheet("color: #6b7280; font-size: 11pt;")
        drop_layout.addWidget(self.file_subtext)
        
        card_layout.addWidget(self.drop_zone)
        
        # Buttons
        button_layout = QVBoxLayout()
        button_layout.setSpacing(12)
        
        self.browse_btn = QPushButton("📂 Browse Files")
        self.browse_btn.setMinimumHeight(50)
        self.browse_btn.clicked.connect(self.browse_file)
        button_layout.addWidget(self.browse_btn)
        
        self.upload_btn = QPushButton("⚡ Upload & Analyze")
        self.upload_btn.setObjectName("accentButton")
        self.upload_btn.setMinimumHeight(50)
        self.upload_btn.setEnabled(False)
        self.upload_btn.clicked.connect(self.upload_file)
        button_layout.addWidget(self.upload_btn)
        
        card_layout.addLayout(button_layout)
        
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: none;
                border-radius: 8px;
                background: rgba(255, 255, 255, 0.05);
                height: 8px;
            }
            QProgressBar::chunk {
                border-radius: 8px;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                          stop:0 #00bfa5, stop:1 #5df2d6);
            }
        """)
        card_layout.addWidget(self.progress_bar)
        
        # Sample info
        info = QLabel(
            "<b>Sample Format:</b> Download the sample_equipment_data.csv "
            "file from the project root to see the expected format."
        )
        info.setWordWrap(True)
        info.setStyleSheet("""
            background: rgba(0, 191, 165, 0.05);
            border-left: 4px solid #00bfa5;
            border-radius: 8px;
            padding: 16px;
            color: #b0b8d4;
            font-size: 10pt;
        """)
        card_layout.addWidget(info)
        
        layout.addWidget(card)
    
    def dragEnterEvent(self, event: QDragEnterEvent):
        """Handle drag enter"""
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
    
    def dropEvent(self, event: QDropEvent):
        """Handle file drop"""
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        if files:
            self.select_file(files[0])
    
    def browse_file(self):
        """Open file browser"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select CSV File",
            "",
            "CSV Files (*.csv)"
        )
        
        if file_path:
            self.select_file(file_path)
    
    def select_file(self, file_path):
        """Select a file"""
        # Validate file
        if not file_path.endswith('.csv'):
            QMessageBox.warning(self, "Error", "Please select a CSV file")
            return
        
        file_size = os.path.getsize(file_path)
        if file_size > 10 * 1024 * 1024:  # 10MB
            QMessageBox.warning(self, "Error", "File size must be less than 10MB")
            return
        
        self.selected_file = file_path
        filename = os.path.basename(file_path)
        size_kb = file_size / 1024
        
        # Update UI
        self.file_icon.setText("📄")
        self.file_label.setText(filename)
        self.file_subtext.setText(f"{size_kb:.2f} KB")
        self.upload_btn.setEnabled(True)
        
        self.drop_zone.setStyleSheet("""
            QFrame {
                border: 3px dashed #10b981;
                border-radius: 16px;
                background: rgba(16, 185, 129, 0.05);
            }
        """)
    
    def upload_file(self):
        """Upload selected file"""
        if not self.selected_file:
            return
        
        # Disable buttons
        self.browse_btn.setEnabled(False)
        self.upload_btn.setEnabled(False)
        self.progress_bar.setVisible(True)
        self.progress_bar.setRange(0, 0)  # Indeterminate progress
        
        # Start upload thread
        self.upload_thread = UploadThread(self.api_client, self.selected_file)
        self.upload_thread.success.connect(self.on_upload_success)
        self.upload_thread.error.connect(self.on_upload_error)
        self.upload_thread.start()
    
    def on_upload_success(self, dataset):
        """Handle successful upload"""
        self.progress_bar.setVisible(False)
        self.browse_btn.setEnabled(True)
        self.upload_btn.setEnabled(True)
        
        QMessageBox.information(
            self,
            "Success",
            f"Dataset '{dataset['filename']}' uploaded successfully!\n"
            f"Total records: {dataset['total_count']}"
        )
        
        self.upload_success.emit(dataset)
        self.reset_ui()
    
    def on_upload_error(self, error_msg):
        """Handle upload error"""
        self.progress_bar.setVisible(False)
        self.browse_btn.setEnabled(True)
        self.upload_btn.setEnabled(True)
        
        QMessageBox.critical(
            self,
            "Upload Failed",
            f"Error uploading file: {error_msg}"
        )
    
    def reset_ui(self):
        """Reset UI to initial state"""
        self.selected_file = None
        self.file_icon.setText("📤")
        self.file_label.setText("Click to browse or drag and drop")
        self.file_subtext.setText("CSV files only (max 10MB)")
        self.upload_btn.setEnabled(False)
        self.drop_zone.setStyleSheet("""
            QFrame {
                border: 3px dashed rgba(255, 255, 255, 0.2);
                border-radius: 16px;
                background: rgba(255, 255, 255, 0.02);
            }
            QFrame:hover {
                border-color: #00bfa5;
                background: rgba(0, 191, 165, 0.05);
            }
        """)
