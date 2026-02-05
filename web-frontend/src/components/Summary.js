import React from 'react';
import { downloadPDF } from '../api';

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
        <div className="space-y-6">
            {/* Header Section */}
            <div className="bg-gray-800/50 backdrop-blur-md rounded-2xl border border-gray-700 p-6 flex justify-between items-start">
                <div>
                    <h2 className="text-2xl font-bold text-white mb-2 flex items-center gap-2">
                        <span>📊</span> Dataset Summary
                    </h2>
                    <p className="text-lg text-blue-400 font-medium">{dataset.filename}</p>
                    <p className="text-sm text-gray-400 mt-1">
                        Uploaded on {formatDate(dataset.uploaded_at)}
                        {dataset.uploaded_by && ` by ${dataset.uploaded_by.username}`}
                    </p>
                </div>
                <button
                    className="px-6 py-3 bg-gradient-to-r from-green-600 to-emerald-600 hover:from-green-700 hover:to-emerald-700 text-white font-semibold rounded-lg shadow-lg shadow-green-500/30 hover:shadow-green-500/50 transition-all duration-200 flex items-center gap-2"
                    onClick={handleDownloadPDF}
                >
                    <span>📄</span> Download PDF Report
                </button>
            </div>

            {/* Stats Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                <div className="bg-gradient-to-br from-blue-900/40 to-blue-800/20 backdrop-blur-md rounded-xl border border-blue-700/50 p-6 hover:shadow-lg hover:shadow-blue-500/20 transition-all duration-200">
                    <div className="flex items-start justify-between mb-3">
                        <div className="text-4xl">📦</div>
                    </div>
                    <p className="text-sm text-gray-400 uppercase tracking-wide font-semibold mb-1">Total Equipment</p>
                    <p className="text-4xl font-bold text-white">{dataset.total_count}</p>
                </div>

                <div className="bg-gradient-to-br from-purple-900/40 to-purple-800/20 backdrop-blur-md rounded-xl border border-purple-700/50 p-6 hover:shadow-lg hover:shadow-purple-500/20 transition-all duration-200">
                    <div className="flex items-start justify-between mb-3">
                        <div className="text-4xl">💨</div>
                    </div>
                    <p className="text-sm text-gray-400 uppercase tracking-wide font-semibold mb-1">Avg Flowrate</p>
                    <p className="text-4xl font-bold text-white">{dataset.avg_flowrate.toFixed(2)}</p>
                    <p className="text-sm text-gray-400 mt-1">m³/h</p>
                </div>

                <div className="bg-gradient-to-br from-green-900/40 to-emerald-800/20 backdrop-blur-md rounded-xl border border-green-700/50 p-6 hover:shadow-lg hover:shadow-green-500/20 transition-all duration-200">
                    <div className="flex items-start justify-between mb-3">
                        <div className="text-4xl">🔧</div>
                    </div>
                    <p className="text-sm text-gray-400 uppercase tracking-wide font-semibold mb-1">Avg Pressure</p>
                    <p className="text-4xl font-bold text-white">{dataset.avg_pressure.toFixed(2)}</p>
                    <p className="text-sm text-gray-400 mt-1">bar</p>
                </div>

                <div className="bg-gradient-to-br from-orange-900/40 to-red-800/20 backdrop-blur-md rounded-xl border border-orange-700/50 p-6 hover:shadow-lg hover:shadow-orange-500/20 transition-all duration-200">
                    <div className="flex items-start justify-between mb-3">
                        <div className="text-4xl">🌡️</div>
                    </div>
                    <p className="text-sm text-gray-400 uppercase tracking-wide font-semibold mb-1">Avg Temperature</p>
                    <p className="text-4xl font-bold text-white">{dataset.avg_temperature.toFixed(2)}</p>
                    <p className="text-sm text-gray-400 mt-1">°C</p>
                </div>
            </div>

            {/* Distribution Section */}
            <div className="bg-gray-800/50 backdrop-blur-md rounded-2xl border border-gray-700 p-6">
                <h3 className="text-xl font-bold text-white mb-4">Equipment Type Distribution</h3>
                <div className="space-y-3">
                    {Object.entries(dataset.equipment_distribution || {}).map(([type, count]) => (
                        <div key={type} className="group">
                            <div className="flex justify-between items-center mb-1">
                                <span className="text-gray-300 font-medium">{type}</span>
                                <span className="text-gray-400 text-sm">
                                    {count} ({((count / dataset.total_count) * 100).toFixed(1)}%)
                                </span>
                            </div>
                            <div className="w-full bg-gray-700/50 rounded-full h-3 overflow-hidden">
                                <div
                                    className="bg-gradient-to-r from-blue-500 to-blue-600 h-3 rounded-full transition-all duration-500 ease-out group-hover:from-blue-400 group-hover:to-blue-500"
                                    style={{ width: `${(count / dataset.total_count) * 100}%` }}
                                ></div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
}

export default Summary;
