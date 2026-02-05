import React, { useState } from 'react';
import { uploadCSV } from '../api';
import './FileUpload.css';

function FileUpload({ onUploadSuccess }) {
    const [file, setFile] = useState(null);
    const [uploading, setUploading] = useState(false);
    const [error, setError] = useState('');
    const [dragActive, setDragActive] = useState(false);

    const handleFileChange = (e) => {
        const selectedFile = e.target.files[0];
        validateAndSetFile(selectedFile);
    };

    const validateAndSetFile = (selectedFile) => {
        setError('');

        if (!selectedFile) return;

        if (!selectedFile.name.endsWith('.csv')) {
            setError('Please select a CSV file');
            return;
        }

        if (selectedFile.size > 10 * 1024 * 1024) { // 10MB limit
            setError('File size must be less than 10MB');
            return;
        }

        setFile(selectedFile);
    };

    const handleDrag = (e) => {
        e.preventDefault();
        e.stopPropagation();
        if (e.type === 'dragenter' || e.type === 'dragover') {
            setDragActive(true);
        } else if (e.type === 'dragleave') {
            setDragActive(false);
        }
    };

    const handleDrop = (e) => {
        e.preventDefault();
        e.stopPropagation();
        setDragActive(false);

        if (e.dataTransfer.files && e.dataTransfer.files[0]) {
            validateAndSetFile(e.dataTransfer.files[0]);
        }
    };

    const handleUpload = async () => {
        if (!file) {
            setError('Please select a file first');
            return;
        }

        setUploading(true);
        setError('');

        try {
            const result = await uploadCSV(file);
            onUploadSuccess(result);
            setFile(null);
            // Reset file input
            document.getElementById('file-input').value = '';
        } catch (err) {
            setError(err.response?.data?.error || 'Error uploading file. Please try again.');
        } finally {
            setUploading(false);
        }
    };

    return (
        <div className="file-upload-container card">
            <div className="upload-header">
                <h2 className="upload-title">📁 Upload Equipment Data</h2>
                <p className="upload-description">
                    Upload a CSV file containing equipment parameters (Equipment Name, Type, Flowrate, Pressure, Temperature)
                </p>
            </div>

            {error && (
                <div className="alert alert-error">
                    <span>⚠️</span>
                    <span>{error}</span>
                </div>
            )}

            <div
                className={`drop-zone ${dragActive ? 'drag-active' : ''} ${file ? 'has-file' : ''}`}
                onDragEnter={handleDrag}
                onDragLeave={handleDrag}
                onDragOver={handleDrag}
                onDrop={handleDrop}
                onClick={() => document.getElementById('file-input').click()}
            >
                <input
                    id="file-input"
                    type="file"
                    accept=".csv"
                    onChange={handleFileChange}
                    style={{ display: 'none' }}
                />

                {file ? (
                    <div className="file-info">
                        <div className="file-icon">📄</div>
                        <div className="file-details">
                            <p className="file-name">{file.name}</p>
                            <p className="file-size">{(file.size / 1024).toFixed(2)} KB</p>
                        </div>
                        <button
                            className="remove-file"
                            onClick={(e) => {
                                e.stopPropagation();
                                setFile(null);
                                document.getElementById('file-input').value = '';
                            }}
                        >
                            ✕
                        </button>
                    </div>
                ) : (
                    <div className="drop-zone-content">
                        <div className="upload-icon">📤</div>
                        <p className="drop-text">
                            <strong>Click to browse</strong> or drag and drop
                        </p>
                        <p className="drop-subtext">CSV files only (max 10MB)</p>
                    </div>
                )}
            </div>

            <button
                className="btn btn-accent"
                onClick={handleUpload}
                disabled={!file || uploading}
                style={{ width: '100%', marginTop: '16px' }}
            >
                {uploading ? (
                    <>
                        <div className="spinner" style={{ width: '20px', height: '20px' }}></div>
                        Uploading & Processing...
                    </>
                ) : (
                    <>
                        <span>⚡</span>
                        Upload & Analyze
                    </>
                )}
            </button>

            <div className="sample-info">
                <p>
                    <strong>Sample Format:</strong> Download the <code>sample_equipment_data.csv</code> file
                    from the project root to see the expected format.
                </p>
            </div>
        </div>
    );
}

export default FileUpload;
