# ✅ Data Verification Guide

This guide explains how to verify that the **Chemical Equipment Visualizer** is processing your data correctly.

## 1. Input Data Verification (The Source)
Before uploading, open your CSV file (`sample_equipment_data.csv`) in Excel or Notepad.
Note down a few key stats manually or using Excel formulas:
- **Total Rows**: (e.g., 20 rows excluding header)
- **Average Flowrate**: `=AVERAGE(C2:C21)`
- **Max Temperature**: `=MAX(E2:E21)`

## 2. Dashboard Verification (The Output)
Once you upload the file to the web app:

### A. Summary Cards
Check the top summary cards. They should match your manual calculations exactly.
- **Total Equipment**: Should equal your CSV row count.
- **Avg Flowrate**: Should act match up to 2 decimal places.
- **Avg Pressure**: Should match the average of the Pressure column.

### B. Data Table
Scroll down to the "Detailed Data" table.
- Check the **first row** and **last row**. Do they match your CSV?
- If they match, the parsing logic is correct.

### C. Charts
- **Distribution Chart** (Pie/Doughnut): Count how many "Pump" items are in your CSV. Does the chart show the same number?
- **Correlation Chart** (Scatter): Look for outliers. If your CSV has a machine with `Temperature: 1000` (high), is there a dot way up high on the chart?

## 3. PDF Report Verification
Click the **"Download Report"** button.
1. Open the PDF.
2. Check the **Header**: Does it have the correct filename and date?
3. Check the **Statistics Table**: Does it match the web dashboard?
4. **Visual Check**: Are the charts generated in the PDF readable?

## 4. Cross-Platform Verification (Desktop vs Web)
1. Open the **Desktop App**.
2. Go to the **History** tab.
3. Select the same dataset you uploaded on the Web.
4. **Compare**: Do the Web numbers match the Desktop numbers?
   - If YES: The Backend API is functioning perfectly as the "Single Source of Truth".

## Troubleshooting "Incorrect" Data
- **Issue**: Numbers are slightly off (e.g., 50.01 vs 50.02).
  - **Cause**: Floating point rounding differences between Excel and Python. This is normal.
- **Issue**: Missing rows.
  - **Cause**: Check if your CSV has empty lines at the end. The app handles this, but Excel might count them differently.
