"""
Visualization widget with charts and tables
"""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QTableWidget, QTableWidgetItem, QHeaderView, QFrame,
    QScrollArea, QFileDialog, QMessageBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class VisualizationWidget(QWidget):
    """Widget for data visualization"""
    
    def __init__(self, api_client):
        super().__init__()
        self.api_client = api_client
        self.dataset = None
        self.init_ui()
    
    def init_ui(self):
        """Initialize UI"""
        # Main scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; }")
        
        container = QWidget()
        self.main_layout = QVBoxLayout(container)
        self.main_layout.setSpacing(24)
        
        scroll.setWidget(container)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(scroll)
        
        # Initially show empty state
        self.show_empty_state()
    
    def show_empty_state(self):
        """Show empty state when no dataset"""
        # Clear existing widgets
        while self.main_layout.count():
            child = self.main_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        empty_label = QLabel("📊 No dataset loaded\n\nUpload a CSV file to view analysis")
        empty_label.setAlignment(Qt.AlignCenter)
        empty_label.setStyleSheet("""
            color: #6b7280;
            font-size: 16pt;
            padding: 80px;
        """)
        self.main_layout.addWidget(empty_label)
    
    def set_dataset(self, dataset):
        """Set dataset and display visualizations"""
        self.dataset = dataset
        self.display_data()
    
    def display_data(self):
        """Display dataset visualizations"""
        # Clear existing widgets
        while self.main_layout.count():
            child = self.main_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        # Summary section
        self.create_summary_section()
        
        # Charts section
        self.create_charts_section()
        
        # Table section
        self.create_table_section()
    
    def create_summary_section(self):
        """Create summary statistics section"""
        # Header
        header = QHBoxLayout()
        
        title_container = QVBoxLayout()
        title = QLabel("📊 Dataset Summary")
        title.setObjectName("sectionLabel")
        title_container.addWidget(title)
        
        subtitle = QLabel(self.dataset['filename'])
        subtitle.setStyleSheet("color: white; font-size: 14pt; font-weight: 600;")
        title_container.addWidget(subtitle)
        
        upload_time = self.dataset.get('uploaded_at', '')
        if upload_time:
            time_label = QLabel(f"Uploaded: {upload_time[:19].replace('T', ' ')}")
            time_label.setStyleSheet("color: #6b7280; font-size: 10pt;")
            title_container.addWidget(time_label)
        
        header.addLayout(title_container)
        header.addStretch()
        
        # PDF download button
        pdf_btn = QPushButton("📄 Download PDF Report")
        pdf_btn.setMinimumHeight(40)
        pdf_btn.clicked.connect(self.download_pdf)
        header.addWidget(pdf_btn)
        
        self.main_layout.addLayout(header)
        
        # Stats cards
        stats_container = QHBoxLayout()
        stats_container.setSpacing(16)
        
        stats = [
            ("📦", "Total Equipment", str(self.dataset['total_count']), ""),
            ("💨", "Avg Flowrate", f"{self.dataset['avg_flowrate']:.2f}", "m³/h"),
            ("🔧", "Avg Pressure", f"{self.dataset['avg_pressure']:.2f}", "bar"),
            ("🌡️", "Avg Temperature", f"{self.dataset['avg_temperature']:.2f}", "°C"),
        ]
        
        for icon, label, value, unit in stats:
            card = self.create_stat_card(icon, label, value, unit)
            stats_container.addWidget(card)
        
        self.main_layout.addLayout(stats_container)
    
    def create_stat_card(self, icon, label, value, unit):
        """Create a stat card widget"""
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                          stop:0 rgba(26, 35, 126, 0.3),
                                          stop:1 rgba(83, 75, 174, 0.2));
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 12px;
                padding: 16px;
            }
        """)
        
        layout = QHBoxLayout(card)
        
        icon_label = QLabel(icon)
        icon_label.setStyleSheet("font-size: 32pt;")
        layout.addWidget(icon_label)
        
        text_layout = QVBoxLayout()
        
        label_widget = QLabel(label)
        label_widget.setStyleSheet("""
            color: #6b7280;
            font-size: 9pt;
            font-weight: 600;
            text-transform: uppercase;
        """)
        text_layout.addWidget(label_widget)
        
        value_widget = QLabel(value)
        value_widget.setStyleSheet("""
            color: #5df2d6;
            font-size: 20pt;
            font-weight: 700;
        """)
        text_layout.addWidget(value_widget)
        
        if unit:
            unit_widget = QLabel(unit)
            unit_widget.setStyleSheet("color: #b0b8d4; font-size: 10pt;")
            text_layout.addWidget(unit_widget)
        
        layout.addLayout(text_layout)
        layout.addStretch()
        
        return card
    
    def create_charts_section(self):
        """Create charts section"""
        section_title = QLabel("📈 Visual Analytics")
        section_title.setObjectName("sectionLabel")
        self.main_layout.addWidget(section_title)
        
        # Charts container
        charts_layout = QHBoxLayout()
        charts_layout.setSpacing(16)
        
        # Equipment distribution pie chart
        pie_chart = self.create_pie_chart()
        charts_layout.addWidget(pie_chart)
        
        # Parameters bar chart
        bar_chart = self.create_bar_chart()
        charts_layout.addWidget(bar_chart)
        
        self.main_layout.addLayout(charts_layout)
    
    def create_pie_chart(self):
        """Create equipment type distribution pie chart"""
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background: rgba(26, 31, 58, 0.4);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 12px;
                padding: 20px;
            }
        """)
        
        layout = QVBoxLayout(card)
        
        title = QLabel("Equipment Type Distribution")
        title.setStyleSheet("color: white; font-size: 14pt; font-weight: 600;")
        layout.addWidget(title)
        
        # Create matplotlib figure
        fig = Figure(figsize=(6, 5), facecolor='#0a0e27')
        ax = fig.add_subplot(111)
        
        distribution = self.dataset.get('equipment_distribution', {})
        if distribution:
            labels = list(distribution.keys())
            sizes = list(distribution.values())
            
            colors = ['#1a237e', '#0288d1', '#00bfa5', '#534bae', '#5eb8ff', '#5df2d6']
            
            ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,
                   colors=colors[:len(labels)], textprops={'color': 'white'})
            ax.axis('equal')
        
        ax.set_facecolor('#0a0e27')
        fig.tight_layout()
        
        canvas = FigureCanvas(fig)
        canvas.setStyleSheet("background: transparent;")
        layout.addWidget(canvas)
        
        return card
    
    def create_bar_chart(self):
        """Create average parameters bar chart"""
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background: rgba(26, 31, 58, 0.4);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 12px;
                padding: 20px;
            }
        """)
        
        layout = QVBoxLayout(card)
        
        title = QLabel("Average Parameters by Type")
        title.setStyleSheet("color: white; font-size: 14pt; font-weight: 600;")
        layout.addWidget(title)
        
        # Create matplotlib figure
        fig = Figure(figsize=(6, 5), facecolor='#0a0e27')
        ax = fig.add_subplot(111)
        
        # Calculate averages by type
        records = self.dataset.get('records', [])
        type_data = {}
        
        for record in records:
            eq_type = record['equipment_type']
            if eq_type not in type_data:
                type_data[eq_type] = {'flowrate': [], 'pressure': [], 'temperature': []}
            
            type_data[eq_type]['flowrate'].append(record['flowrate'])
            type_data[eq_type]['pressure'].append(record['pressure'])
            type_data[eq_type]['temperature'].append(record['temperature'])
        
        types = list(type_data.keys())
        avg_flowrate = [sum(type_data[t]['flowrate']) / len(type_data[t]['flowrate']) for t in types]
        avg_pressure = [sum(type_data[t]['pressure']) / len(type_data[t]['pressure']) for t in types]
        
        x = range(len(types))
        width = 0.35
        
        ax.bar([i - width/2 for i in x], avg_flowrate, width, label='Flowrate (m³/h)', color='#00bfa5')
        ax.bar([i + width/2 for i in x], avg_pressure, width, label='Pressure (bar)', color='#0288d1')
        
        ax.set_xlabel('Equipment Type', color='#b0b8d4')
        ax.set_ylabel('Average Value', color='#b0b8d4')
        ax.set_xticks(x)
        ax.set_xticklabels(types, rotation=45, ha='right', color='#b0b8d4')
        ax.tick_params(colors='#b0b8d4')
        ax.legend(facecolor='#1a1f3a', edgecolor='#00bfa5', labelcolor='white')
        ax.set_facecolor('#0a0e27')
        ax.spines['bottom'].set_color('#b0b8d4')
        ax.spines['top'].set_color('#b0b8d4')
        ax.spines['left'].set_color('#b0b8d4')
        ax.spines['right'].set_color('#b0b8d4')
        
        fig.tight_layout()
        
        canvas = FigureCanvas(fig)
        canvas.setStyleSheet("background: transparent;")
        layout.addWidget(canvas)
        
        return card
    
    def create_table_section(self):
        """Create data table section"""
        section_title = QLabel("📋 Equipment Records")
        section_title.setObjectName("sectionLabel")
        self.main_layout.addWidget(section_title)
        
        # Table
        table = QTableWidget()
        table.setStyleSheet("""
            QTableWidget {
                background: rgba(26, 31, 58, 0.4);
                border-radius: 12px;
            }
        """)
        
        records = self.dataset.get('records', [])
        
        # Set up table
        table.setColumnCount(6)
        table.setRowCount(len(records))
        table.setHorizontalHeaderLabels([
            '#', 'Equipment Name', 'Type', 'Flowrate (m³/h)', 'Pressure (bar)', 'Temperature (°C)'
        ])
        
        # Populate table
        for i, record in enumerate(records):
            table.setItem(i, 0, QTableWidgetItem(str(i + 1)))
            table.setItem(i, 1, QTableWidgetItem(record['equipment_name']))
            table.setItem(i, 2, QTableWidgetItem(record['equipment_type']))
            table.setItem(i, 3, QTableWidgetItem(f"{record['flowrate']:.2f}"))
            table.setItem(i, 4, QTableWidgetItem(f"{record['pressure']:.2f}"))
            table.setItem(i, 5, QTableWidgetItem(f"{record['temperature']:.2f}"))
        
        # Configure table
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setAlternatingRowColors(True)
        table.setEditTriggers(QTableWidget.NoEditTriggers)
        table.setSelectionBehavior(QTableWidget.SelectRows)
        table.setMaximumHeight(400)
        
        self.main_layout.addWidget(table)
    
    def download_pdf(self):
        """Download PDF report"""
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save PDF Report",
            f"{self.dataset['filename']}_report.pdf",
            "PDF Files (*.pdf)"
        )
        
        if file_path:
            try:
                self.api_client.download_pdf(self.dataset['id'], file_path)
                QMessageBox.information(
                    self,
                    "Success",
                    f"PDF report saved to:\n{file_path}"
                )
            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Error",
                    f"Failed to download PDF: {str(e)}"
                )
