import React, { useState } from 'react';
import { uploadCSV } from '../api';

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

        if (selectedFile.size > 10 * 1024 * 1024) {
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
            document.getElementById('file-input').value = '';
        } catch (err) {
            setError(err.response?.data?.error || 'Error uploading file. Please try again.');
        } finally {
            setUploading(false);
        }
    };

    return (
        <div className="space-y-6">
            <div className="text-center">
                <h2 className="text-3xl font-bold text-white mb-2 flex items-center justify-center gap-2">
                    <span>📁</span> Upload Equipment Data
                </h2>
                <p className="text-gray-400">
                    Upload a CSV file containing equipment parameters
                    <span className="block text-sm mt-1 text-gray-500">
                        (Equipment Name, Type, Flowrate, Pressure, Temperature)
                    </span>
                </p>
            </div>

            {error && (
                <div className="p-4 bg-red-500/10 border border-red-500/50 rounded-lg flex items-center gap-3 text-red-400">
                    <span className="text-xl">⚠️</span>
                    <span>{error}</span>
                </div>
            )}

            <div
                className={`
                    border-2 border-dashed rounded-2xl p-12 text-center cursor-pointer
                    transition-all duration-200
                    ${dragActive
                        ? 'border-blue-500 bg-blue-500/10'
                        : file
                            ? 'border-green-500 bg-green-500/5'
                            : 'border-gray-600 bg-gray-900/20 hover:border-blue-500/50 hover:bg-blue-500/5'
                    }
                `}
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
                    className="hidden"
                />

                {file ? (
                    <div className="flex items-center justify-center gap-4">
                        <div className="text-6xl">📄</div>
                        <div className="text-left">
                            <p className="text-lg font-semibold text-white">{file.name}</p>
                            <p className="text-sm text-gray-400">{(file.size / 1024).toFixed(2)} KB</p>
                        </div>
                        <button
                            className="ml-4 p-2 bg-red-600/20 hover:bg-red-600/40 text-red-400 rounded-lg transition-colors"
                            onClick={(e) => {
                                e.stopPropagation();
                                setFile(null);
                                document.getElementById('file-input').value = '';
                            }}
                        >
                            <span className="text-2xl">✕</span>
                        </button>
                    </div>
                ) : (
                    <div className="space-y-4">
                        <div className="text-7xl">📤</div>
                        <div>
                            <p className="text-xl text-gray-300 mb-1">
                                <strong className="text-blue-400">Click to browse</strong> or drag and drop
                            </p>
                            <p className="text-sm text-gray-500">CSV files only (max 10MB)</p>
                        </div>
                    </div>
                )}
            </div>

            <button
                className="w-full py-4 px-6 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white font-bold text-lg rounded-xl shadow-lg shadow-blue-500/30 hover:shadow-blue-500/50 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-3"
                onClick={handleUpload}
                disabled={!file || uploading}
            >
                {uploading ? (
                    <>
                        <div className="animate-spin rounded-full h-6 w-6 border-b-2 border-white"></div>
                        Uploading & Processing...
                    </>
                ) : (
                    <>
                        <span className="text-2xl">⚡</span>
                        Upload & Analyze
                    </>
                )}
            </button>

            <div className="bg-blue-500/5 border border-blue-500/20 rounded-lg p-4 text-center">
                <p className="text-sm text-gray-400">
                    <strong className="text-blue-400">Sample Format:</strong> Download the{' '}
                    <code className="bg-gray-900/50 px-2 py-1 rounded text-blue-300">sample_equipment_data.csv</code>{' '}
                    file from the project root to see the expected format.
                </p>
            </div>
        </div>
    );
}

export default FileUpload;
