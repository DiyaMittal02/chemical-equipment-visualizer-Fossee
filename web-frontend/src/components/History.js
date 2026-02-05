import React, { useState, useEffect } from 'react';
import { getDatasetHistory } from '../api';
import './History.css';

function History({ refresh, onDatasetSelect }) {
    const [datasets, setDatasets] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    useEffect(() => {
        fetchHistory();
    }, [refresh]);

    const fetchHistory = async () => {
        setLoading(true);
        setError('');

        try {
            const data = await getDatasetHistory();
            setDatasets(data);
        } catch (err) {
            setError('Failed to load history');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const formatDate = (dateString) => {
        const date = new Date(dateString);
        return date.toLocaleString('en-US', {
            year: 'numeric',
            month: 'short',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit',
        });
    };

    if (loading) {
        return (
            <div className="history-loading">
                <div className="spinner"></div>
                <p>Loading history...</p>
            </div>
        );
    }

    if (error) {
        return (
            <div className="alert alert-error">
                <span>⚠️</span>
                <span>{error}</span>
            </div>
        );
    }

    if (datasets.length === 0) {
        return (
            <div className="history-empty card">
                <div className="empty-icon">📭</div>
                <h3>No Upload History</h3>
                <p>Upload your first dataset to see it here!</p>
            </div>
        );
    }

    return (
        <div className="history-container">
            <div className="history-header">
                <h2 className="history-title">📜 Upload History</h2>
                <p className="history-subtitle">Your last {datasets.length} uploaded datasets</p>
            </div>

            <div className="history-grid">
                {datasets.map((dataset, index) => (
                    <div
                        key={dataset.id}
                        className="history-card card"
                        onClick={() => onDatasetSelect(dataset)}
                    >
                        <div className="history-card-header">
                            <div className="history-number">{index + 1}</div>
                            <div className="history-info">
                                <h4 className="history-filename">{dataset.filename}</h4>
                                <p className="history-date">{formatDate(dataset.uploaded_at)}</p>
                                {dataset.uploaded_by && (
                                    <p className="history-user">by {dataset.uploaded_by.username}</p>
                                )}
                            </div>
                        </div>

                        <div className="history-stats">
                            <div className="history-stat">
                                <span className="stat-icon">📦</span>
                                <span className="stat-text">{dataset.total_count} records</span>
                            </div>
                            <div className="history-stat">
                                <span className="stat-icon">💨</span>
                                <span className="stat-text">{dataset.avg_flowrate.toFixed(1)} m³/h</span>
                            </div>
                            <div className="history-stat">
                                <span className="stat-icon">🔧</span>
                                <span className="stat-text">{dataset.avg_pressure.toFixed(1)} bar</span>
                            </div>
                            <div className="history-stat">
                                <span className="stat-icon">🌡️</span>
                                <span className="stat-text">{dataset.avg_temperature.toFixed(1)} °C</span>
                            </div>
                        </div>

                        <div className="history-types">
                            {Object.keys(dataset.equipment_distribution || {}).map((type) => (
                                <span key={type} className="type-tag">
                                    {type}
                                </span>
                            ))}
                        </div>

                        <div className="view-details">
                            <span>Click to view details</span>
                            <span>→</span>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default History;
