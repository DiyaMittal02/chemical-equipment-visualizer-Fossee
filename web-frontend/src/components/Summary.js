import React from 'react';
import { downloadPDF } from '../api';
import './Summary.css';

function Summary({ dataset }) {
    const handleDownloadPDF = async () => {
        try {
            const pdfBlob = await downloadPDF(dataset.id);
            const url = window.URL.createObjectURL(pdfBlob);
            const link = document.createElement('a');
            link.href = url;
            link.download = `${dataset.filename}_report.pdf`;
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            window.URL.revokeObjectURL(url);
        } catch (error) {
            console.error('Error downloading PDF:', error);
            alert('Failed to download PDF report');
        }
    };

    const formatDate = (dateString) => {
        const date = new Date(dateString);
        return date.toLocaleString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit',
        });
    };

    return (
        <div className="summary-container">
            <div className="summary-header">
                <div>
                    <h2 className="summary-title">📊 Dataset Summary</h2>
                    <p className="summary-subtitle">{dataset.filename}</p>
                    <p className="summary-date">
                        Uploaded on {formatDate(dataset.uploaded_at)}
                        {dataset.uploaded_by && ` by ${dataset.uploaded_by.username}`}
                    </p>
                </div>
                <button className="btn btn-primary" onClick={handleDownloadPDF}>
                    📄 Download PDF Report
                </button>
            </div>

            <div className="stats-grid">
                <div className="stat-card card">
                    <div className="stat-icon">📦</div>
                    <div className="stat-content">
                        <p className="stat-label">Total Equipment</p>
                        <p className="stat-value">{dataset.total_count}</p>
                    </div>
                </div>

                <div className="stat-card card">
                    <div className="stat-icon">💨</div>
                    <div className="stat-content">
                        <p className="stat-label">Avg Flowrate</p>
                        <p className="stat-value">{dataset.avg_flowrate.toFixed(2)}</p>
                        <p className="stat-unit">m³/h</p>
                    </div>
                </div>

                <div className="stat-card card">
                    <div className="stat-icon">🔧</div>
                    <div className="stat-content">
                        <p className="stat-label">Avg Pressure</p>
                        <p className="stat-value">{dataset.avg_pressure.toFixed(2)}</p>
                        <p className="stat-unit">bar</p>
                    </div>
                </div>

                <div className="stat-card card">
                    <div className="stat-icon">🌡️</div>
                    <div className="stat-content">
                        <p className="stat-label">Avg Temperature</p>
                        <p className="stat-value">{dataset.avg_temperature.toFixed(2)}</p>
                        <p className="stat-unit">°C</p>
                    </div>
                </div>
            </div>

            <div className="distribution-section card">
                <h3 className="section-title">Equipment Type Distribution</h3>
                <div className="distribution-grid">
                    {Object.entries(dataset.equipment_distribution || {}).map(([type, count]) => (
                        <div key={type} className="distribution-item">
                            <div className="distribution-bar-container">
                                <div
                                    className="distribution-bar"
                                    style={{
                                        width: `${(count / dataset.total_count) * 100}%`,
                                    }}
                                ></div>
                            </div>
                            <div className="distribution-info">
                                <span className="distribution-type">{type}</span>
                                <span className="distribution-count">
                                    {count} ({((count / dataset.total_count) * 100).toFixed(1)}%)
                                </span>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
}

export default Summary;
