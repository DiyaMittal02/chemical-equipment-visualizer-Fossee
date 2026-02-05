# Chemical Equipment Parameter Visualizer
### Hybrid Web + Desktop Application

A comprehensive full-stack application for analyzing and visualizing chemical equipment parameters. This project demonstrates modern software architecture with a unified Django backend serving both React web and PyQt5 desktop frontends.

![Project Banner](https://via.placeholder.com/1200x300/1a237e/00bfa5?text=Chemical+Equipment+Visualizer)

## 🎯 Project Overview

This hybrid application allows users to upload CSV files containing chemical equipment data, perform analytics, and visualize results through interactive charts and tables. The system features:

- **Unified Django Backend**: RESTful API serving both frontends
- **React Web Frontend**: Modern, responsive web interface with Chart.js
- **PyQt5 Desktop App**: Native desktop application with Matplotlib
- **Data Analytics**: Pandas-powered CSV processing and statistics
- **PDF Reporting**: Automated report generation
- **Authentication**: Secure user management
- **History Management**: Store and access last 5 uploaded datasets

## 🏗️ Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Backend** | Django + Django REST Framework | Common API backend |
| **Web Frontend** | React.js + Chart.js | Interactive web visualization |
| **Desktop Frontend** | PyQt5 + Matplotlib | Native desktop application |
| **Data Processing** | Pandas | CSV parsing & analytics |
| **Database** | SQLite | Dataset storage |
| **Reporting** | ReportLab | PDF generation |
| **Version Control** | Git & GitHub | Code management |

## ✨ Key Features

### 1. CSV Upload
- ✅ Drag-and-drop file upload (Web & Desktop)
- ✅ File validation (format & size)
- ✅ Real-time processing feedback
- ✅ Progress indicators

### 2. Data Analytics
- ✅ Automatic statistics calculation
  - Total equipment count
  - Average flowrate, pressure, temperature
  - Equipment type distribution
- ✅ Data validation and error handling
- ✅ Comprehensive data summaries

### 3. Interactive Visualizations
- ✅ **Web (Chart.js)**:
  - Pie chart for equipment distribution
  - Bar chart for average parameters
  - Line chart for temperature trends
- ✅ **Desktop (Matplotlib)**:
  - Professional publication-quality charts
  - Customizable visualizations
  - Export capabilities

### 4. Data Management
- ✅ Detailed data tables with sorting
- ✅ Equipment records display
- ✅ History of last 5 uploads
- ✅ Dataset comparison

### 5. PDF Reporting
- ✅ Automated report generation
- ✅ Professional formatting
- ✅ Summary statistics included
- ✅ Equipment distribution analysis

### 6. Authentication
- ✅ User registration & login
- ✅ Session management
- ✅ Secure password handling
- ✅ User-specific data access

## 📁 Project Structure

```
FOOSEE/
├── backend/                    # Django REST API
│   ├── backend/
│   │   ├── __init__.py
│   │   ├── settings.py         # Django configuration
│   │   ├── urls.py             # URL routing
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── models.py           # Data models
│   │   ├── serializers.py      # DRF serializers
│   │   ├── views.py            # API endpoints
│   │   ├── urls.py             # API routing
│   │   ├── admin.py            # Admin interface
│   │   └── utils.py            # PDF generation
│   ├── manage.py
│   └── requirements.txt
│
├── web-frontend/               # React Application
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── Auth.js
│   │   │   ├── FileUpload.js
│   │   │   ├── Summary.js
│   │   │   ├── Charts.js
│   │   │   ├── DataTable.js
│   │   │   └── History.js
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   ├── index.css
│   │   └── api.js              # API client
│   └── package.json
│
├── desktop-app/                # PyQt5 Application
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── main_window.py
│   │   ├── auth_widget.py
│   │   ├── upload_widget.py
│   │   ├── visualization_widget.py
│   │   ├── history_widget.py
│   │   └── styles.py
│   ├── main.py                 # Entry point
│   ├── api_client.py           # API communication
│   └── requirements.txt
│
├── sample_equipment_data.csv   # Sample dataset
├── README.md                   # This file
├── .gitignore
└── LICENSE
```

## 🚀 Setup Instructions

### Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher
- Node.js 14 or higher
- npm or yarn
- Git

### 1. Backend Setup (Django)

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional, for admin access)
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

The backend will be available at `http://localhost:8000`

### 2. Web Frontend Setup (React)

Open a new terminal:

```bash
# Navigate to web frontend directory
cd web-frontend

# Install dependencies
npm install

# Start development server
npm start
```

The web app will open automatically at `http://localhost:3000`

### 3. Desktop App Setup (PyQt5)

Open a new terminal:

```bash
# Navigate to desktop app directory
cd desktop-app

# Create virtual environment (if not using backend's venv)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run desktop application
python main.py
```

### Important Notes

- **Run Order**: Start the Django backend FIRST, then launch either frontend
- **Port Configuration**: Backend runs on port 8000, React on port 3000
- **API Base URL**: Update if deploying to a different server
- **Sample Data**: Use `sample_equipment_data.csv` for testing

## 📊 Sample Data Format

Your CSV file should have the following columns:

```csv
Equipment Name,Type,Flowrate,Pressure,Temperature
Reactor-A1,Reactor,150.5,8.2,320.0
Heat Exchanger-B2,Heat Exchanger,200.3,5.5,280.5
Pump-C3,Pump,95.0,12.0,85.0
...
```

**Column Descriptions:**
- **Equipment Name**: Unique identifier for the equipment
- **Type**: Category (Reactor, Pump, Heat Exchanger, etc.)
- **Flowrate**: Flow rate in m³/h
- **Pressure**: Pressure in bar
- **Temperature**: Temperature in °C

## 🎮 Usage Guide

### Web Application

1. **Login/Register**: Create an account or sign in
2. **Upload Data**: 
   - Click "Upload Data" tab
   - Select or drag-and-drop CSV file
   - Click "Upload & Analyze"
3. **View Analysis**: Automatically switches to analysis view
4. **Download Report**: Click "Download PDF Report"
5. **View History**: Access "History" tab for past uploads

### Desktop Application

1. **Launch Application**: Run `python main.py`
2. **Authenticate**: Login with your credentials
3. **Upload**: Use "Upload Data" tab to select files
4. **Visualize**: View charts and statistics
5. **Export**: Download PDF reports to your computer

## 🔧 API Endpoints

### Authentication
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - User login
- `POST /api/auth/logout/` - User logout
- `GET /api/auth/user/` - Get current user

### Data Management
- `POST /api/upload/` - Upload CSV file
- `GET /api/datasets/` - List all datasets
- `GET /api/datasets/{id}/` - Get specific dataset
- `GET /api/datasets/{id}/download_pdf/` - Download PDF report
- `GET /api/history/` - Get last 5 datasets
- `GET /api/summary/{id}/` - Get dataset summary

## 🎨 Design Features

### Web Application
- **Dark Theme**: Modern, eye-friendly color scheme
- **Glassmorphism Effects**: Premium frosted glass aesthetics
- **Smooth Animations**: Micro-interactions for better UX
- **Responsive Design**: Mobile, tablet, and desktop support
- **Gradient Accents**: Vibrant color gradients

### Desktop Application
- **Native Look & Feel**: Qt-styled interface
- **Consistent Theming**: Matches web design
- **High DPI Support**: Sharp on retina displays
- **Custom Widgets**: Tailored components
- **Professional Charts**: Publication-quality matplotlib visualizations

## 🧪 Testing

### Test the Application

1. **Use Sample Data**: Start with `sample_equipment_data.csv`
2. **Create Test User**: Register with test credentials
3. **Upload Workflow**: 
   - Upload sample file
   - Verify statistics
   - Check visualizations
   - Download PDF
4. **History**: Upload multiple files to test history feature

### Expected Results

- Total equipment: 30
- Equipment types: Reactor, Pump, Heat Exchanger, Column, Compressor, Mixer, Separator, Valve, Tank, Furnace
- All averages should be calculated correctly
- Charts should display data distribution
- PDF should generate without errors

## 🚢 Deployment

### Backend (Django)

**Option 1: Heroku**
```bash
# Install Heroku CLI
# Login to Heroku
heroku login

# Create app
heroku create your-app-name

# Add buildpack
heroku buildpacks:set heroku/python

# Push code
git push heroku main

# Run migrations
heroku run python manage.py migrate
```

**Option 2: Railway/Render**
- Connect GitHub repository
- Set build command: `pip install -r requirements.txt`
- Set start command: `python manage.py runserver 0.0.0.0:$PORT`

### Web Frontend (React)

**Option 1: Vercel**
```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
cd web-frontend
vercel
```

**Option 2: Netlify**
```bash
# Build project
npm run build

# Deploy build folder via Netlify CLI or drag-and-drop
```

### Desktop App

**Distribution Options:**
1. **PyInstaller**: Create standalone executable
   ```bash
   pip install pyinstaller
   pyinstaller --onefile --windowed main.py
   ```

2. **Inno Setup** (Windows): Create installer
3. **DMG** (Mac): Create distributable package

## 📝 Configuration

### Environment Variables

Create `.env` files for production:

**Backend (.env)**
```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-domain.com
DATABASE_URL=your-database-url
CORS_ALLOWED_ORIGINS=https://your-frontend-domain.com
```

**Web Frontend (.env)**
```env
REACT_APP_API_URL=https://your-backend-domain.com/api
```

**Desktop App (config.py)**
```python
API_BASE_URL = "https://your-backend-domain.com/api"
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Your Name** - *Initial work* - [GitHub Profile](https://github.com/yourusername)

## 🙏 Acknowledgments

- Django and Django REST Framework teams
- React and Chart.js communities
- Qt and PyQt5 developers
- Pandas and Matplotlib contributors
- Open source community

## 📧 Contact

For questions or support:
- Email: your.email@example.com
- GitHub Issues: [Create an issue](https://github.com/yourusername/FOOSEE/issues)
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)

## 📸 Screenshots

### Web Application
![Web Dashboard](https://via.placeholder.com/800x450/1a237e/00bfa5?text=Web+Dashboard)

### Desktop Application
![Desktop App](https://via.placeholder.com/800x450/1a237e/00bfa5?text=Desktop+Application)

### PDF Report
![PDF Report](https://via.placeholder.com/800x450/1a237e/00bfa5?text=PDF+Report)

---

**Built with ❤️ for the FOOSEE Internship Screening Task**

*Last Updated: February 2026*
