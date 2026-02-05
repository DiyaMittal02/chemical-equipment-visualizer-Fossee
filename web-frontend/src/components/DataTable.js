import React from 'react';
import './DataTable.css';

function DataTable({ dataset }) {
    const records = dataset.records || [];

    return (
        <div className="data-table-section card">
            <div className="table-header">
                <h3 className="table-title">📋 Equipment Records</h3>
                <p className="table-count">
                    Showing {records.length} {records.length === 1 ? 'record' : 'records'}
                </p>
            </div>

            <div className="table-container">
                <table>
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Equipment Name</th>
                            <th>Type</th>
                            <th>Flowrate (m³/h)</th>
                            <th>Pressure (bar)</th>
                            <th>Temperature (°C)</th>
                        </tr>
                    </thead>
                    <tbody>
                        {records.map((record, index) => (
                            <tr key={record.id || index}>
                                <td>{index + 1}</td>
                                <td className="equipment-name">{record.equipment_name}</td>
                                <td>
                                    <span className="equipment-type-badge">{record.equipment_type}</span>
                                </td>
                                <td className="numeric-value">{record.flowrate.toFixed(2)}</td>
                                <td className="numeric-value">{record.pressure.toFixed(2)}</td>
                                <td className="numeric-value">{record.temperature.toFixed(2)}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}

export default DataTable;
