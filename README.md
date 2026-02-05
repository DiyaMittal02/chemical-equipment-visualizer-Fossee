# 🧪 Chemical Equipment Visualizer

A full-stack hybrid application for analyzing and visualizing chemical equipment parameters with support for both web and desktop interfaces.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2-green.svg)
![React](https://img.shields.io/badge/React-18.0-61DAFB.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Features

- **📊 Data Analysis**: Upload CSV files containing equipment parameters for instant statistical analysis
- **📈 Visualizations**: Interactive charts showing equipment distribution, correlations, and trends
- **📄 PDF Reports**: Generate comprehensive PDF reports with statistics and visualizations
- **🔄 History Tracking**: Manage up to 10 most recent dataset uploads
- **🌐 Dual Interface**: 
  - Modern web application with Tailwind CSS
  - Native desktop application with PyQt5
- **🔐 Authentication**: Secure user authentication and data management
- **⚡ Real-time Processing**: Instant data processing and visualization

## 🏗️ Architecture

```
FOOSEE/
├── backend/              # Django REST Framework API
│   ├── api/             # API endpoints and models
│   ├── backend/         # Django settings and configuration
│   └── manage.py
├── web-frontend/        # React web application
│   ├── public/
│   └── src/
│       ├── components/  # React components
│       └── api.js      # API client
├── desktop-app/         # PyQt5 desktop application
│   ├── ui/             # UI components
│   ├── api_client.py   # Backend communication
│   └── main.py
└── sample_equipment_data.csv  # Sample data file
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+**
- **Node.js 14+** and npm
- **Git**

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/FOOSEE.git
cd FOOSEE
```

2. **Backend Setup**
```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # Create admin account
```

3. **Frontend Setup**
```bash
cd web-frontend
npm install
```

4. **Desktop App Setup** (Optional)
```bash
# From project root with backend venv activated
pip install PyQt5 matplotlib requests
```

### Running the Application

**Option 1: Use the Launch Script (Windows)**
```bash
# From project root
LAUNCH_APP.bat
```

**Option 2: Manual Start**

**Terminal 1 - Backend:**
```bash
cd backend
venv\Scripts\activate
python manage.py runserver 127.0.0.1:8000
```

**Terminal 2 - Web Frontend:**
```bash
cd web-frontend
npm start
```

**Terminal 3 - Desktop App (Optional):**
```bash
cd desktop-app
..\backend\venv\Scripts\python main.py
```

### Access

- **Web App**: http://localhost:3000
- **Backend API**: http://127.0.0.1:8000/api/
- **Admin Panel**: http://127.0.0.1:8000/admin/

**Default Test Credentials:**
- Username: `admin`
- Password: `admin`

## 📂 Data Format

Upload CSV files with the following columns:

| Equipment Name | Type | Flowrate | Pressure | Temperature |
|----------------|------|----------|----------|-------------|
| Pump-01 | Pump | 150.5 | 5.2 | 85.0 |
| HX-101 | Heat Exchanger | 200.0 | 3.8 | 120.5 |

See `sample_equipment_data.csv` for a complete example.

## 🛠️ Technology Stack

### Backend
- **Django 4.2.7** - Web framework
- **Django REST Framework** - API framework
- **Django CORS Headers** - Cross-origin resource sharing
- **Pandas** - Data processing
- **ReportLab** - PDF generation
- **SQLite** - Database (default)

### Frontend (Web)
- **React 18** - UI library
- **Tailwind CSS** - Styling framework
- **Axios** - HTTP client
- **Chart.js** - Data visualization

### Frontend (Desktop)
- **PyQt5** - GUI framework
- **Matplotlib** - Charting library
- **Requests** - HTTP client

## 📊 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/auth/register/` | POST | User registration |
| `/api/auth/login/` | POST | User login |
| `/api/auth/logout/` | POST | User logout |
| `/api/auth/user/` | GET | Current user info |
| `/api/data/upload/` | POST | Upload CSV file |
| `/api/data/datasets/` | GET | List datasets |
| `/api/data/datasets/{id}/` | GET | Dataset details |
| `/api/data/history/` | GET | Recent uploads |
| `/api/data/download-pdf/{id}/` | GET | Download PDF report |

## 🧪 Testing

### Verification Steps

1. **Upload Test**: Upload `sample_equipment_data.csv`
2. **Summary Validation**: Check stats match the CSV data
3. **Visualization Check**: Verify charts display correctly
4. **PDF Download**: Generate and review PDF report
5. **History Verification**: Check upload appears in history

See `VERIFICATION_GUIDE.md` for detailed testing instructions.

## 🔒 Security Notes

**⚠️ Development Mode Only**

This configuration is for **development/demonstration** purposes:
- CSRF protection is disabled on auth endpoints
- CORS is configured for localhost origins
- Debug mode is enabled
- SQLite database is used

**For Production:**
1. Set `DEBUG = False` in `settings.py`
2. Configure proper `ALLOWED_HOSTS`
3. Use PostgreSQL or MySQL
4. Enable CSRF protection
5. Configure production CORS settings
6. Use environment variables for secrets
7. Set up HTTPS

## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For issues or questions, please open an issue on GitHub.

---

**Built with ❤️ using Django, React, and PyQt5**
