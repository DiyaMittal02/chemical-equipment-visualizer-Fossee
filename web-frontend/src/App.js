import React, { useState, useEffect } from 'react';
import './App.css';
import FileUpload from './components/FileUpload';
import DataTable from './components/DataTable';
import Charts from './components/Charts';
import Summary from './components/Summary';
import History from './components/History';
import Auth from './components/Auth';
import { getCurrentUser, logoutUser, getDataset } from './api';

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

    const handleDatasetSelect = async (dataset) => {
        try {
            // Use summary dataset initially or show loading
            // Fetch full details
            const fullDataset = await getDataset(dataset.id);
            setCurrentDataset(fullDataset);
            setActiveTab('view');
        } catch (err) {
            console.error("Failed to load full dataset:", err);
            // Fallback to summary if fetch fails, though graph might break
            setCurrentDataset(dataset);
            setActiveTab('view');
        }
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
            <div className="min-h-screen bg-gradient-to-br from-gray-900 via-blue-900 to-gray-900 flex items-center justify-center">
                <div className="text-center">
                    <div className="animate-spin rounded-full h-16 w-16 border-b-4 border-blue-500 mx-auto mb-4"></div>
                    <p className="text-gray-300 text-lg">Loading...</p>
                </div>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-gradient-to-br from-gray-900 via-blue-900 to-gray-900">
            <header className="bg-gray-800/50 backdrop-blur-md border-b border-gray-700 sticky top-0 z-50">
                <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
                    <div className="flex items-center gap-4">
                        <div className="text-4xl">⚗️</div>
                        <div>
                            <h1 className="text-2xl font-bold text-white">Chemical Equipment Visualizer</h1>
                            <p className="text-sm text-blue-400 font-medium">Advanced Parameter Analysis & Visualization</p>
                        </div>
                    </div>

                    {user ? (
                        <div className="flex items-center gap-4">
                            <div className="flex items-center gap-2 bg-gray-700/50 px-4 py-2 rounded-lg">
                                <span className="text-2xl">👤</span>
                                <span className="text-gray-200 font-medium">{user.username}</span>
                            </div>
                            <button
                                onClick={handleLogout}
                                className="px-4 py-2 bg-red-600 hover:bg-red-700 text-white rounded-lg font-medium transition-colors"
                            >
                                Logout
                            </button>
                        </div>
                    ) : (
                        <div className="text-gray-400 text-sm">
                            Sign in for full access
                        </div>
                    )}
                </div>
            </header>

            <main className="max-w-7xl mx-auto px-6 py-8">
                {!user ? (
                    <div className="max-w-md mx-auto mt-16">
                        <Auth onLoginSuccess={handleLoginSuccess} />
                    </div>
                ) : (
                    <>
                        <nav className="flex gap-2 mb-8 bg-gray-800/50 backdrop-blur-md p-2 rounded-xl border border-gray-700 w-fit">
                            <button
                                className={`px-6 py-3 rounded-lg font-semibold transition-all ${activeTab === 'upload'
                                    ? 'bg-blue-600 text-white shadow-lg shadow-blue-500/50'
                                    : 'text-gray-400 hover:text-white hover:bg-gray-700/50'
                                    }`}
                                onClick={() => setActiveTab('upload')}
                            >
                                📤 Upload Data
                            </button>
                            <button
                                className={`px-6 py-3 rounded-lg font-semibold transition-all ${activeTab === 'view'
                                    ? 'bg-blue-600 text-white shadow-lg shadow-blue-500/50'
                                    : 'text-gray-400 hover:text-white hover:bg-gray-700/50'
                                    } ${!currentDataset ? 'opacity-50 cursor-not-allowed' : ''}`}
                                onClick={() => setActiveTab('view')}
                                disabled={!currentDataset}
                            >
                                📊 View Analysis
                            </button>
                            <button
                                className={`px-6 py-3 rounded-lg font-semibold transition-all ${activeTab === 'history'
                                    ? 'bg-blue-600 text-white shadow-lg shadow-blue-500/50'
                                    : 'text-gray-400 hover:text-white hover:bg-gray-700/50'
                                    }`}
                                onClick={() => setActiveTab('history')}
                            >
                                📜 History
                            </button>
                        </nav>

                        <div className="transition-all duration-300">
                            {activeTab === 'upload' && (
                                <div className="bg-gray-800/50 backdrop-blur-md rounded-2xl border border-gray-700 p-8 animate-fadeIn">
                                    <FileUpload onUploadSuccess={handleUploadSuccess} />
                                </div>
                            )}

                            {activeTab === 'view' && currentDataset && (
                                <div className="space-y-6 animate-fadeIn">
                                    <Summary dataset={currentDataset} />
                                    <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                                        <Charts dataset={currentDataset} />
                                    </div>
                                    <DataTable dataset={currentDataset} />
                                </div>
                            )}

                            {activeTab === 'history' && (
                                <div className="bg-gray-800/50 backdrop-blur-md rounded-2xl border border-gray-700 p-8 animate-fadeIn">
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

            <footer className="mt-16 border-t border-gray-700 py-6">
                <p className="text-center text-gray-400 text-sm">
                    © 2026 Chemical Equipment Visualizer | Built with React & Django
                </p>
            </footer>
        </div>
    );
}

export default App;
