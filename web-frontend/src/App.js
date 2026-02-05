import React, { useState, useEffect } from 'react';
import './App.css';
import FileUpload from './components/FileUpload';
import DataTable from './components/DataTable';
import Charts from './components/Charts';
import Summary from './components/Summary';
import History from './components/History';
import Auth from './components/Auth';
import { getCurrentUser, logoutUser } from './api';

function App() {
    const [currentDataset, setCurrentDataset] = useState(null);
    const [refreshHistory, setRefreshHistory] = useState(0);
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const [activeTab, setActiveTab] = useState('upload');

    useEffect(() => {
        checkAuth();
    }, []);

    const checkAuth = async () => {
        try {
            const userData = await getCurrentUser();
            setUser(userData);
        } catch (error) {
            setUser(null);
        } finally {
            setLoading(false);
        }
    };

    const handleUploadSuccess = (dataset) => {
        setCurrentDataset(dataset);
        setRefreshHistory(prev => prev + 1);
        setActiveTab('view');
    };

    const handleDatasetSelect = (dataset) => {
        setCurrentDataset(dataset);
        setActiveTab('view');
    };

    const handleLogout = async () => {
        try {
            await logoutUser();
            setUser(null);
            setCurrentDataset(null);
        } catch (error) {
            console.error('Logout error:', error);
        }
    };

    const handleLoginSuccess = (userData) => {
        setUser(userData);
    };

    if (loading) {
        return (
            <div className="app-container">
                <div className="loading-container">
                    <div className="spinner"></div>
                    <p>Loading...</p>
                </div>
            </div>
        );
    }

    return (
        <div className="app-container">
            <header className="app-header">
                <div className="header-content">
                    <div className="logo-section">
                        <div className="logo-icon">⚗️</div>
                        <div>
                            <h1 className="app-title">Chemical Equipment Visualizer</h1>
                            <p className="app-subtitle">Advanced Parameter Analysis & Visualization</p>
                        </div>
                    </div>

                    {user ? (
                        <div className="user-section">
                            <div className="user-info">
                                <span className="user-icon">👤</span>
                                <span className="username">{user.username}</span>
                            </div>
                            <button onClick={handleLogout} className="btn btn-secondary">
                                Logout
                            </button>
                        </div>
                    ) : (
                        <div className="auth-prompt">
                            <span className="auth-text">Sign in for full access</span>
                        </div>
                    )}
                </div>
            </header>

            <main className="app-main">
                {!user ? (
                    <div className="auth-container fade-in">
                        <Auth onLoginSuccess={handleLoginSuccess} />
                    </div>
                ) : (
                    <>
                        <nav className="tab-nav">
                            <button
                                className={`tab-button ${activeTab === 'upload' ? 'active' : ''}`}
                                onClick={() => setActiveTab('upload')}
                            >
                                📤 Upload Data
                            </button>
                            <button
                                className={`tab-button ${activeTab === 'view' ? 'active' : ''}`}
                                onClick={() => setActiveTab('view')}
                                disabled={!currentDataset}
                            >
                                📊 View Analysis
                            </button>
                            <button
                                className={`tab-button ${activeTab === 'history' ? 'active' : ''}`}
                                onClick={() => setActiveTab('history')}
                            >
                                📜 History
                            </button>
                        </nav>

                        <div className="tab-content">
                            {activeTab === 'upload' && (
                                <div className="upload-section fade-in">
                                    <FileUpload onUploadSuccess={handleUploadSuccess} />
                                </div>
                            )}

                            {activeTab === 'view' && currentDataset && (
                                <div className="analysis-section fade-in">
                                    <Summary dataset={currentDataset} />
                                    <div className="charts-grid">
                                        <Charts dataset={currentDataset} />
                                    </div>
                                    <DataTable dataset={currentDataset} />
                                </div>
                            )}

                            {activeTab === 'history' && (
                                <div className="history-section fade-in">
                                    <History
                                        refresh={refreshHistory}
                                        onDatasetSelect={handleDatasetSelect}
                                    />
                                </div>
                            )}
                        </div>
                    </>
                )}
            </main>

            <footer className="app-footer">
                <p>© 2026 Chemical Equipment Visualizer | Built with React & Django</p>
            </footer>
        </div>
    );
}

export default App;
