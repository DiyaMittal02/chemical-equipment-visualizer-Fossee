# System Architecture Diagram

## Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    CHEMICAL EQUIPMENT VISUALIZER                 │
│                     Hybrid Application System                    │
└─────────────────────────────────────────────────────────────────┘

                              ┌──────────────┐
                              │    USER      │
                              └──────┬───────┘
                                     │
                     ┌───────────────┴────────────────┐
                     │                                │
              ┌──────▼──────┐                  ┌─────▼──────┐
              │ Web Browser │                  │  Desktop   │
              │  (Chrome,   │                  │    App     │
              │   Firefox)  │                  │  (PyQt5)   │
              └──────┬──────┘                  └─────┬──────┘
                     │                               │
                     │                               │
              ┌──────▼──────────────────────────────▼──────┐
              │          REACT WEB FRONTEND                │
              │                                             │
              │  ┌─────────────────────────────────────┐   │
              │  │  Components:                        │   │
              │  │  • Auth (Login/Register)            │   │
              │  │  • FileUpload (Drag & Drop)         │   │
              │  │  • Summary (Statistics Cards)       │   │
              │  │  • Charts (Chart.js Visualizations) │   │
              │  │  • DataTable (Equipment Records)    │   │
              │  │  • History (Past Uploads)           │   │
              │  └─────────────────────────────────────┘   │
              │                                             │
              │  Libraries: React, Chart.js, Axios          │
              └──────────────────┬──────────────────────────┘
                                 │
                                 │ HTTP/REST API
                                 │
              ┌──────────────────▼──────────────────────────┐
              │     DJANGO REST FRAMEWORK BACKEND           │
              │                                             │
              │  ┌─────────────────────────────────────┐   │
              │  │  API Endpoints:                     │   │
              │  │  POST /api/auth/login/              │   │
              │  │  POST /api/auth/register/           │   │
              │  │  POST /api/upload/                  │   │
              │  │  GET  /api/datasets/                │   │
              │  │  GET  /api/datasets/{id}/           │   │
              │  │  GET  /api/history/                 │   │
              │  │  GET  /api/datasets/{id}/download_pdf/ │
              │  └─────────────────────────────────────┘   │
              │                                             │
              │  ┌─────────────────────────────────────┐   │
              │  │  Core Components:                   │   │
              │  │  • Models (EquipmentDataset, etc.)  │   │
              │  │  • Serializers (DRF)                │   │
              │  │  • Views (API Logic)                │   │
              │  │  • Utils (PDF Generation)           │   │
              │  │  • Authentication (Session/Basic)   │   │
              │  └─────────────────────────────────────┘   │
              │                                             │
              │  Libraries: Django, DRF, Pandas, ReportLab │
              └──────────────────┬──────────────────────────┘
                                 │
                                 │ ORM
                                 │
              ┌──────────────────▼──────────────────────────┐
              │           SQLite DATABASE                   │
              │                                             │
              │  Tables:                                    │
              │  ┌─────────────────────────────────────┐   │
              │  │ auth_user                           │   │
              │  │  - id, username, password, email    │   │
              │  ├─────────────────────────────────────┤   │
              │  │ api_equipmentdataset                │   │
              │  │  - id, filename, uploaded_at        │   │
              │  │  - total_count, avg_flowrate        │   │
              │  │  - avg_pressure, avg_temperature    │   │
              │  │  - equipment_distribution (JSON)    │   │
              │  │  - csv_data (TEXT)                  │   │
              │  ├─────────────────────────────────────┤   │
              │  │ api_equipmentrecord                 │   │
              │  │  - id, equipment_name               │   │
              │  │  - equipment_type, flowrate         │   │
              │  │  - pressure, temperature            │   │
              │  └─────────────────────────────────────┘   │
              └─────────────────────────────────────────────┘


═══════════════════════════════════════════════════════════════════

DATA FLOW: CSV Upload Process

  ┌─────────┐
  │  USER   │
  └────┬────┘
       │ Selects CSV file
       ▼
  ┌─────────────────┐
  │  Web/Desktop    │
  │   Frontend      │
  └────┬────────────┘
       │ POST /api/upload/
       │ (multipart/form-data)
       ▼
  ┌─────────────────────────┐
  │  Django Backend         │
  │  1. Validate file       │
  │  2. Read with Pandas    │
  │  3. Calculate stats     │
  │  4. Save to database    │
  │  5. Create records      │
  │  6. Maintain history(5) │
  └────┬────────────────────┘
       │ Return dataset JSON
       ▼
  ┌─────────────────┐
  │   Frontend      │
  │  1. Display     │
  │     summary     │
  │  2. Render      │
  │     charts      │
  │  3. Show table  │
  └─────────────────┘

═══════════════════════════════════════════════════════════════════

VISUALIZATION FLOW

  Chart.js (Web)              Matplotlib (Desktop)
       │                            │
       ├── Pie Chart ───────────────┼── Equipment Distribution
       │                            │
       ├── Bar Chart ───────────────┼── Average Parameters
       │                            │
       └── Line Chart ──────────────┼── Temperature Trends


═══════════════════════════════════════════════════════════════════

SECURITY LAYERS

┌─────────────────────────────────────────────────────────────────┐
│  Layer 1: Authentication                                        │
│  • User registration with password hashing                       │
│  • Session-based authentication                                  │
│  • Login required for most endpoints                            │
└─────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────┐
│  Layer 2: Data Validation                                       │
│  • CSV file type validation                                     │
│  • File size limits (10MB)                                      │
│  • Required column validation                                   │
│  • Data type validation                                         │
└─────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────┐
│  Layer 3: CORS & CSRF                                           │
│  • CORS headers configured                                      │
│  • CSRF protection enabled                                      │
│  • Allowed hosts restriction                                    │
└─────────────────────────────────────────────────────────────────┘


═══════════════════════════════════════════════════════════════════

TECHNOLOGY STACK

Frontend (Web)          Frontend (Desktop)       Backend
    │                        │                      │
    ├─ React 18              ├─ PyQt5              ├─ Django 4.2
    ├─ Chart.js              ├─ Matplotlib         ├─ DRF 3.14
    ├─ Axios                 ├─ Requests           ├─ Pandas 2.1
    └─ CSS3                  └─ Python 3.8+        └─ ReportLab


════════════════════════════════════════════════════════════════════

DEPLOYMENT ARCHITECTURE (Optional)

┌────────────────────────────────────────────────────────────────┐
│                         PRODUCTION                              │
└────────────────────────────────────────────────────────────────┘

    ┌──────────────┐              ┌──────────────┐
    │   Vercel/    │              │   Render/    │
    │   Netlify    │◄────────────►│   Railway    │
    │  (Frontend)  │   API Calls  │  (Backend)   │
    └──────────────┘              └──────┬───────┘
                                         │
                                         ▼
                                  ┌─────────────┐
                                  │ PostgreSQL  │
                                  │  Database   │
                                  └─────────────┘

Desktop App: Distributed as standalone executable (PyInstaller)


════════════════════════════════════════════════════════════════════

FEATURES MATRIX

Feature              Web    Desktop    Backend
─────────────────────────────────────────────────
Authentication       ✅      ✅         ✅
CSV Upload           ✅      ✅         ✅
Drag & Drop          ✅      ✅         N/A
Data Validation      ✅      ✅         ✅
Statistics           ✅      ✅         ✅
Pie Chart            ✅      ✅         N/A
Bar Chart            ✅      ✅         N/A
Line Chart           ✅      ✅         N/A
Data Table           ✅      ✅         N/A
History (5)          ✅      ✅         ✅
PDF Download         ✅      ✅         ✅
Dark Theme           ✅      ✅         N/A
Responsive           ✅      N/A        N/A
Native UI            N/A     ✅         N/A


════════════════════════════════════════════════════════════════════
```

## Component Interaction

### 1. Authentication Flow
```
User Input → Frontend → POST /api/auth/login/ → Django Auth
                     ← Session Cookie ← Success/Failure
```

### 2. Upload Flow
```
CSV File → Frontend → POST /api/upload/ → Django
                                        ↓
                                    Pandas Process
                                        ↓
                                    Save to DB
                                        ↓
                     ← Dataset JSON ← Success
```

### 3. Visualization Flow
```
Dataset → Frontend → Chart.js/Matplotlib → Render Charts
```

### 4. PDF Generation Flow
```
Request → Backend → ReportLab → Generate PDF → Return Binary
```

## Performance Considerations

- **Pandas**: Efficient CSV processing
- **Database**: Indexed queries for fast retrieval
- **Frontend**: React virtual DOM for smooth updates
- **Desktop**: Threaded uploads prevent UI freezing
- **Caching**: Browser cache for static assets

## Scalability

Current capacity:
- CSV files: Up to 10MB
- Records: Thousands per dataset
- Users: Concurrent authentication
- History: Last 5 datasets per user

Future improvements:
- Redis caching
- Celery for background tasks
- PostgreSQL for production
- S3 for file storage
- Load balancing
