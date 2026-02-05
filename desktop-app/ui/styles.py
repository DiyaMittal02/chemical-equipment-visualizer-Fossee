"""
Qt Style Sheet for the application - Premium Glass/Slate Adaptation
"""

# Premium Modern Theme (Tailwind-inspired)
DARK_THEME = """
/* Global Reset */
QMainWindow, QWidget {
    background-color: #0f172a;  /* slate-900 */
    color: #f8fafc;             /* slate-50 */
    font-family: 'Segoe UI', 'Inter', sans-serif;
    font-size: 10pt;
}

/* Typography */
QLabel {
    color: #e2e8f0;             /* slate-200 */
    background: transparent;
}

QLabel#titleLabel {
    color: #ffffff;
    font-size: 26pt;
    font-weight: bold;
    background: transparent;
    padding-bottom: 8px;
}

QLabel#subtitleLabel {
    color: #94a3b8;             /* slate-400 */
    font-size: 11pt;
    background: transparent;
}

QLabel#sectionLabel {
    color: #f1f5f9;             /* slate-100 */
    font-size: 16pt;
    font-weight: 600;
    margin-top: 16px;
    margin-bottom: 8px;
    background: transparent;
}

/* Cards / Containers with Glassmorphism */
QFrame#contentFrame, QFrame#cardFrame {
    background-color: rgba(30, 41, 59, 0.7); /* slate-800 with opacity */
    border: 1px solid rgba(148, 163, 184, 0.1);
    border-radius: 16px;
}

/* Buttons */
QPushButton {
    background-color: #334155;  /* slate-700 */
    color: white;
    border: 1px solid #475569;  /* slate-600 */
    border-radius: 8px;
    padding: 10px 20px;
    font-weight: 600;
    font-size: 10pt;
}

QPushButton:hover {
    background-color: #475569;  /* slate-600 */
    border: 1px solid #64748b;  /* slate-500 */
}

QPushButton:pressed {
    background-color: #1e293b;  /* slate-800 */
}

/* Primary Accent Button (Gradient) */
QPushButton#accentButton {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                stop:0 #4f46e5, stop:1 #7c3aed); /* indigo-600 to violet-600 */
    border: none;
    color: white;
    font-weight: bold;
}

QPushButton#accentButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                stop:0 #4338ca, stop:1 #6d28d9); /* darker gradient */
}

QPushButton#accentButton:pressed {
    background-color: #4338ca;
}

/* Input Fields */
QLineEdit, QTextEdit, QPlainTextEdit {
    background-color: #1e293b;  /* slate-800 */
    border: 1px solid #334155;  /* slate-700 */
    border-radius: 8px;
    padding: 10px;
    color: white;
    selection-background-color: #6366f1; /* indigo-500 */
}

QLineEdit:focus, QTextEdit:focus {
    border: 2px solid #6366f1;  /* indigo-500 */
    background-color: #0f172a;  /* slate-900 */
}

/* Tables */
QTableWidget {
    background-color: #1e293b;
    border: 1px solid #334155;
    border-radius: 12px;
    gridline-color: #334155;
    selection-background-color: rgba(99, 102, 241, 0.2);
}

QTableWidget::item {
    padding: 8px;
    border-bottom: 1px solid #334155;
}

QHeaderView::section {
    background-color: #0f172a;
    color: #94a3b8;
    padding: 10px;
    border: none;
    border-bottom: 2px solid #334155;
    font-weight: 600;
    text-transform: uppercase;
}

/* Scrollbars */
QScrollBar:vertical {
    border: none;
    background: #0f172a;
    width: 10px;
    border-radius: 5px;
}

QScrollBar::handle:vertical {
    background: #475569;
    min-height: 20px;
    border-radius: 5px;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

/* Tabs */
QTabWidget::pane {
    border: none;
    background: transparent;
}

QTabBar::tab {
    background: transparent;
    color: #94a3b8;
    padding: 12px 24px;
    border-bottom: 2px solid transparent;
    font-weight: 600;
}

QTabBar::tab:selected {
    color: #ffffff;
    border-bottom: 2px solid #6366f1;
}

QTabBar::tab:hover:!selected {
    color: #e2e8f0;
}

/* Combobox */
QComboBox {
    background-color: #1e293b;
    border: 1px solid #334155;
    border-radius: 8px;
    padding: 8px 12px;
    color: white;
}

QComboBox::drop-down {
    border: none;
    width: 20px;
}

QComboBox QAbstractItemView {
    background-color: #1e293b;
    border: 1px solid #334155;
    selection-background-color: #6366f1;
    color: white;
}
"""
