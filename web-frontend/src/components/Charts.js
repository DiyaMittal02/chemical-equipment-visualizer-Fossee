import React from 'react';
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend,
    ArcElement,
    PointElement,
    LineElement,
} from 'chart.js';
import { Bar, Pie, Line } from 'react-chartjs-2';
import './Charts.css';

ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend,
    ArcElement,
    PointElement,
    LineElement
);

function Charts({ dataset }) {
    const chartOptions = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                labels: {
                    color: '#b0b8d4',
                    font: {
                        family: 'Inter',
                        size: 12,
                    },
                },
            },
            tooltip: {
                backgroundColor: 'rgba(26, 31, 58, 0.95)',
                titleColor: '#ffffff',
                bodyColor: '#b0b8d4',
                borderColor: 'rgba(0, 191, 165, 0.5)',
                borderWidth: 1,
                padding: 12,
                cornerRadius: 8,
            },
        },
        scales: {
            y: {
                ticks: {
                    color: '#b0b8d4',
                },
                grid: {
                    color: 'rgba(255, 255, 255, 0.05)',
                },
            },
            x: {
                ticks: {
                    color: '#b0b8d4',
                },
                grid: {
                    color: 'rgba(255, 255, 255, 0.05)',
                },
            },
        },
    };

    // Equipment Type Distribution (Pie Chart)
    const typeDistributionData = {
        labels: Object.keys(dataset.equipment_distribution || {}),
        datasets: [
            {
                label: 'Count',
                data: Object.values(dataset.equipment_distribution || {}),
                backgroundColor: [
                    'rgba(26, 35, 126, 0.8)',
                    'rgba(2, 136, 209, 0.8)',
                    'rgba(0, 191, 165, 0.8)',
                    'rgba(83, 75, 174, 0.8)',
                    'rgba(94, 184, 255, 0.8)',
                    'rgba(93, 242, 214, 0.8)',
                    'rgba(0, 91, 159, 0.8)',
                    'rgba(0, 142, 118, 0.8)',
                ],
                borderColor: [
                    'rgba(26, 35, 126, 1)',
                    'rgba(2, 136, 209, 1)',
                    'rgba(0, 191, 165, 1)',
                    'rgba(83, 75, 174, 1)',
                    'rgba(94, 184, 255, 1)',
                    'rgba(93, 242, 214, 1)',
                    'rgba(0, 91, 159, 1)',
                    'rgba(0, 142, 118, 1)',
                ],
                borderWidth: 2,
            },
        ],
    };

    // Average Parameters by Type (Bar Chart)
    const records = dataset.records || [];
    const typeAverages = {};

    records.forEach((record) => {
        if (!typeAverages[record.equipment_type]) {
            typeAverages[record.equipment_type] = {
                flowrate: [],
                pressure: [],
                temperature: [],
            };
        }
        typeAverages[record.equipment_type].flowrate.push(record.flowrate);
        typeAverages[record.equipment_type].pressure.push(record.pressure);
        typeAverages[record.equipment_type].temperature.push(record.temperature);
    });

    const types = Object.keys(typeAverages);
    const avgFlowrates = types.map(
        (type) =>
            typeAverages[type].flowrate.reduce((a, b) => a + b, 0) /
            typeAverages[type].flowrate.length
    );
    const avgPressures = types.map(
        (type) =>
            typeAverages[type].pressure.reduce((a, b) => a + b, 0) /
            typeAverages[type].pressure.length
    );
    const avgTemperatures = types.map(
        (type) =>
            typeAverages[type].temperature.reduce((a, b) => a + b, 0) /
            typeAverages[type].temperature.length
    );

    const parametersBarData = {
        labels: types,
        datasets: [
            {
                label: 'Avg Flowrate (m³/h)',
                data: avgFlowrates,
                backgroundColor: 'rgba(0, 191, 165, 0.7)',
                borderColor: 'rgba(0, 191, 165, 1)',
                borderWidth: 2,
            },
            {
                label: 'Avg Pressure (bar)',
                data: avgPressures,
                backgroundColor: 'rgba(2, 136, 209, 0.7)',
                borderColor: 'rgba(2, 136, 209, 1)',
                borderWidth: 2,
            },
        ],
    };

    const temperatureLineData = {
        labels: types,
        datasets: [
            {
                label: 'Avg Temperature (°C)',
                data: avgTemperatures,
                borderColor: 'rgba(245, 158, 11, 1)',
                backgroundColor: 'rgba(245, 158, 11, 0.2)',
                borderWidth: 3,
                tension: 0.4,
                fill: true,
                pointRadius: 6,
                pointHoverRadius: 8,
                pointBackgroundColor: 'rgba(245, 158, 11, 1)',
                pointBorderColor: '#fff',
                pointBorderWidth: 2,
            },
        ],
    };

    return (
        <>
            <div className="chart-card card">
                <h3 className="chart-title">📊 Equipment Type Distribution</h3>
                <div className="chart-container">
                    <Pie data={typeDistributionData} options={{ ...chartOptions, maintainAspectRatio: false }} />
                </div>
            </div>

            <div className="chart-card card">
                <h3 className="chart-title">📈 Average Parameters by Type</h3>
                <div className="chart-container">
                    <Bar data={parametersBarData} options={chartOptions} />
                </div>
            </div>

            <div className="chart-card card" style={{ gridColumn: '1 / -1' }}>
                <h3 className="chart-title">🌡️ Temperature Distribution</h3>
                <div className="chart-container">
                    <Line data={temperatureLineData} options={chartOptions} />
                </div>
            </div>
        </>
    );
}

export default Charts;
