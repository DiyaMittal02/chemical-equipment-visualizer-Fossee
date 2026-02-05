"""
History widget to view past uploads
"""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QFrame,
    QScrollArea, QHBoxLayout, QMessageBox
)
from PyQt5.QtCore import Qt, pyqtSignal


class HistoryWidget(QWidget):
    """Widget for viewing upload history"""
    
    dataset_selected = pyqtSignal(dict)
    
    def __init__(self, api_client):
        super().__init__()
        self.api_client = api_client
        self.datasets = []
        self.init_ui()
    
    def init_ui(self):
        """Initialize UI"""
        layout = QVBoxLayout(self)
        layout.setSpacing(24)
        
        # Header
        header = QVBoxLayout()
        header.setAlignment(Qt.AlignCenter)
        
        title = QLabel("📜 Upload History")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size: 28pt;
            font-weight: 700;
            color: #00bfa5;
        """)
        header.addWidget(title)
        
        self.subtitle = QLabel("Your recent uploaded datasets")
        self.subtitle.setAlignment(Qt.AlignCenter)
        self.subtitle.setStyleSheet("color: #b0b8d4; font-size: 12pt;")
        header.addWidget(self.subtitle)
        
        layout.addLayout(header)
        
        # Refresh button
        refresh_btn = QPushButton("🔄 Refresh")
        refresh_btn.setMaximumWidth(200)
        refresh_btn.clicked.connect(self.refresh)
        
        refresh_container = QHBoxLayout()
        refresh_container.setAlignment(Qt.AlignCenter)
        refresh_container.addWidget(refresh_btn)
        layout.addLayout(refresh_container)
        
        # Scroll area for history cards
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; }")
        
        self.history_container = QWidget()
        self.history_layout = QVBoxLayout(self.history_container)
        self.history_layout.setSpacing(16)
        self.history_layout.setAlignment(Qt.AlignTop)
        
        scroll.setWidget(self.history_container)
        layout.addWidget(scroll)
        
        # Load history
        self.refresh()
    
    def refresh(self):
        """Refresh history"""
        try:
            self.datasets = self.api_client.get_history()
            self.display_history()
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Failed to load history: {str(e)}"
            )
    
    def display_history(self):
        """Display history items"""
        # Clear existing items
        while self.history_layout.count():
            child = self.history_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        if not self.datasets:
            self.show_empty_state()
            return
        
        self.subtitle.setText(f"Your last {len(self.datasets)} uploaded datasets")
        
        # Create cards
        for i, dataset in enumerate(self.datasets):
            card = self.create_history_card(i + 1, dataset)
            self.history_layout.addWidget(card)
    
    def show_empty_state(self):
        """Show empty state"""
        empty_label = QLabel("📭\n\nNo Upload History\n\nUpload your first dataset to see it here!")
        empty_label.setAlignment(Qt.AlignCenter)
        empty_label.setStyleSheet("""
            color: #6b7280;
            font-size: 14pt;
            padding: 60px;
        """)
        self.history_layout.addWidget(empty_label)
    
    def create_history_card(self, index, dataset):
        """Create history card"""
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background: rgba(26, 31, 58, 0.6);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-left: 4px solid #00bfa5;
                border-radius: 12px;
                padding: 20px;
            }
            QFrame:hover {
                background: rgba(26, 31, 58, 0.8);
                border-color: rgba(0, 191, 165, 0.5);
            }
        """)
        card.setCursor(Qt.PointingHandCursor)
        
        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(16)
        
        # Header
        header_layout = QHBoxLayout()
        
        number_label = QLabel(str(index))
        number_label.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                      stop:0 #1a237e, stop:1 #534bae);
            color: white;
            font-size: 16pt;
            font-weight: 700;
            border-radius: 20px;
            padding: 8px;
            min-width: 40px;
            max-width: 40px;
            min-height: 40px;
            max-height: 40px;
        """)
        number_label.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(number_label)
        
        info_layout = QVBoxLayout()
        
        filename_label = QLabel(dataset['filename'])
        filename_label.setStyleSheet("""
            color: white;
            font-size: 14pt;
            font-weight: 700;
        """)
        info_layout.addWidget(filename_label)
        
        upload_time = dataset.get('uploaded_at', '')[:19].replace('T', ' ')
        date_label = QLabel(f"Uploaded: {upload_time}")
        date_label.setStyleSheet("color: #6b7280; font-size: 10pt;")
        info_layout.addWidget(date_label)
        
        if dataset.get('uploaded_by'):
            user_label = QLabel(f"by {dataset['uploaded_by']['username']}")
            user_label.setStyleSheet("color: #00bfa5; font-size: 9pt; font-weight: 600;")
            info_layout.addWidget(user_label)
        
        header_layout.addLayout(info_layout)
        header_layout.addStretch()
        
        card_layout.addLayout(header_layout)
        
        # Stats
        stats_layout = QHBoxLayout()
        stats_layout.setSpacing(12)
        
        stats = [
            ("📦", f"{dataset['total_count']} records"),
            ("💨", f"{dataset['avg_flowrate']:.1f} m³/h"),
            ("🔧", f"{dataset['avg_pressure']:.1f} bar"),
            ("🌡️", f"{dataset['avg_temperature']:.1f} °C"),
        ]
        
        for icon, text in stats:
            stat_widget = QFrame()
            stat_widget.setStyleSheet("""
                background: rgba(255, 255, 255, 0.03);
                border: 1px solid rgba(255, 255, 255, 0.05);
                border-radius: 8px;
                padding: 8px;
            """)
            
            stat_layout = QHBoxLayout(stat_widget)
            stat_layout.setSpacing(8)
            
            icon_label = QLabel(icon)
            icon_label.setStyleSheet("font-size: 14pt;")
            stat_layout.addWidget(icon_label)
            
            text_label = QLabel(text)
            text_label.setStyleSheet("color: #b0b8d4; font-size: 10pt; font-weight: 500;")
            stat_layout.addWidget(text_label)
            
            stats_layout.addWidget(stat_widget)
        
        card_layout.addLayout(stats_layout)
        
        # Equipment types
        if dataset.get('equipment_distribution'):
            types_layout = QHBoxLayout()
            types_layout.setSpacing(8)
            
            for eq_type in list(dataset['equipment_distribution'].keys())[:4]:
                type_badge = QLabel(eq_type)
                type_badge.setStyleSheet("""
                    background: rgba(0, 191, 165, 0.1);
                    border: 1px solid rgba(0, 191, 165, 0.3);
                    border-radius: 12px;
                    padding: 4px 10px;
                    font-size: 9pt;
                    font-weight: 600;
                    color: #5df2d6;
                """)
                types_layout.addWidget(type_badge)
            
            types_layout.addStretch()
            card_layout.addLayout(types_layout)
        
        # Click action
        view_label = QLabel("Click to view details →")
        view_label.setStyleSheet("""
            color: #00bfa5;
            font-size: 10pt;
            font-weight: 600;
            padding-top: 12px;
        """)
        view_label.setAlignment(Qt.AlignRight)
        card_layout.addWidget(view_label)
        
        # Make card clickable
        card.mousePressEvent = lambda event: self.dataset_selected.emit(dataset)
        
        return card
