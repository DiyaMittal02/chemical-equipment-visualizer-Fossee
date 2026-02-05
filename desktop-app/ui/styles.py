"""
Qt Style Sheet for the application
"""

DARK_THEME = """
QMainWindow {
    background-color: #0a0e27;
}

QWidget {
    background-color: #0a0e27;
    color: #ffffff;
    font-family: 'Inter', 'Segoe UI', sans-serif;
    font-size: 11pt;
}

QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #1a237e, stop:1 #534bae);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 12px 24px;
    font-weight: 600;
    font-size: 11pt;
}

QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #534bae, stop:1 #5eb8ff);
}

QPushButton:pressed {
    background: #1a237e;
}

QPushButton:disabled {
    background: #2a2e45;
    color: #6b7280;
}

QPushButton#accentButton {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #00bfa5, stop:1 #5df2d6);
    color: #0a0e27;
}

QPushButton#accentButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #5df2d6, stop:1 #00bfa5);
}

QLineEdit, QTextEdit {
    background-color: rgba(255, 255, 255, 0.05);
    border: 2px solid rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    padding: 12px;
    color: white;
    font-size: 11pt;
}

QLineEdit:focus, QTextEdit:focus {
    border: 2px solid #00bfa5;
    background-color: rgba(255, 255, 255, 0.08);
}

QLabel {
    color: #b0b8d4;
    font-size: 11pt;
}

QLabel#titleLabel {
    color: #00bfa5;
    font-size: 24pt;
    font-weight: 700;
}

QLabel#subtitleLabel {
    color: #b0b8d4;
    font-size: 13pt;
}

QLabel#sectionLabel {
    color: #ffffff;
    font-size: 16pt;
    font-weight: 600;
}

QTableWidget {
    background-color: rgba(26, 31, 58, 0.4);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    gridline-color: rgba(255, 255, 255, 0.05);
}

QTableWidget::item {
    padding: 8px;
    color: #b0b8d4;
}

QTableWidget::item:selected {
    background-color: rgba(0, 191, 165, 0.2);
    color: white;
}

QHeaderView::section {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                stop:0 #1a237e, stop:1 #534bae);
    color: white;
    padding: 12px;
    border: none;
    font-weight: 600;
    text-transform: uppercase;
    font-size: 10pt;
}

QTabWidget::pane {
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    background: rgba(26, 31, 58, 0.4);
}

QTabBar::tab {
    background: transparent;
    color: #b0b8d4;
    padding: 12px 24px;
    margin-right: 4px;
    border-radius: 8px 8px 0 0;
    font-weight: 600;
}

QTabBar::tab:selected {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #00bfa5, stop:1 #5df2d6);
    color: #0a0e27;
}

QTabBar::tab:hover:!selected {
    background: rgba(255, 255, 255, 0.05);
    color: white;
}

QScrollBar:vertical {
    background: #131829;
    width: 12px;
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background: #1a237e;
    border-radius: 6px;
    min-height: 20px;
}

QScrollBar::handle:vertical:hover {
    background: #534bae;
}

QScrollBar:horizontal {
    background: #131829;
    height: 12px;
    border-radius: 6px;
}

QScrollBar::handle:horizontal {
    background: #1a237e;
    border-radius: 6px;
    min-width: 20px;
}

QScrollBar::handle:horizontal:hover {
    background: #534bae;
}

QMessageBox {
    background-color: #1a1f3a;
}

QMessageBox QLabel {
    color: #ffffff;
}

QComboBox {
    background-color: rgba(255, 255, 255, 0.05);
    border: 2px solid rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    padding: 8px 12px;
    color: white;
}

QComboBox:hover {
    border: 2px solid #00bfa5;
}

QComboBox::drop-down {
    border: none;
}

QComboBox QAbstractItemView {
    background-color: #1a1f3a;
    border: 1px solid rgba(255, 255, 255, 0.1);
    selection-background-color: rgba(0, 191, 165, 0.3);
    color: white;
}
"""
