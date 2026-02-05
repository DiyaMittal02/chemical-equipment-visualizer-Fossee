from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import io
from datetime import datetime


def generate_pdf_report(dataset):
    """
    Generate a PDF report for an equipment dataset
    
    Args:
        dataset: EquipmentDataset instance
    
    Returns:
        BytesIO buffer containing the PDF
    """
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1a237e'),
        spaceAfter=30,
        alignment=TA_CENTER,
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#283593'),
        spaceAfter=12,
    )
    
    # Title
    title = Paragraph("Chemical Equipment Parameter Report", title_style)
    elements.append(title)
    elements.append(Spacer(1, 0.2 * inch))
    
    # Dataset Information
    info_heading = Paragraph("Dataset Information", heading_style)
    elements.append(info_heading)
    
    info_data = [
        ['Filename:', dataset.filename],
        ['Upload Date:', dataset.uploaded_at.strftime('%Y-%m-%d %H:%M:%S')],
        ['Total Records:', str(dataset.total_count)],
    ]
    
    if dataset.uploaded_by:
        info_data.append(['Uploaded By:', dataset.uploaded_by.username])
    
    info_table = Table(info_data, colWidths=[2 * inch, 4 * inch])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#e8eaf6')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ]))
    
    elements.append(info_table)
    elements.append(Spacer(1, 0.3 * inch))
    
    # Summary Statistics
    summary_heading = Paragraph("Summary Statistics", heading_style)
    elements.append(summary_heading)
    
    summary_data = [
        ['Parameter', 'Average Value', 'Unit'],
        ['Flowrate', f'{dataset.avg_flowrate:.2f}', 'm³/h'],
        ['Pressure', f'{dataset.avg_pressure:.2f}', 'bar'],
        ['Temperature', f'{dataset.avg_temperature:.2f}', '°C'],
    ]
    
    summary_table = Table(summary_data, colWidths=[2 * inch, 2 * inch, 1.5 * inch])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3f51b5')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    elements.append(summary_table)
    elements.append(Spacer(1, 0.3 * inch))
    
    # Equipment Type Distribution
    distribution_heading = Paragraph("Equipment Type Distribution", heading_style)
    elements.append(distribution_heading)
    
    distribution = dataset.get_distribution_dict()
    dist_data = [['Equipment Type', 'Count', 'Percentage']]
    
    for eq_type, count in distribution.items():
        percentage = (count / dataset.total_count) * 100
        dist_data.append([eq_type, str(count), f'{percentage:.1f}%'])
    
    dist_table = Table(dist_data, colWidths=[2.5 * inch, 1.5 * inch, 1.5 * inch])
    dist_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3f51b5')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#e8eaf6')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#e8eaf6'), colors.white]),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    elements.append(dist_table)
    elements.append(Spacer(1, 0.3 * inch))
    
    # Equipment Records
    records_heading = Paragraph("Equipment Records", heading_style)
    elements.append(records_heading)
    
    # Limit to first 20 records for readability
    records = dataset.records.all()[:20]
    records_data = [['Equipment Name', 'Type', 'Flow', 'Press.', 'Temp.']]
    
    for record in records:
        records_data.append([
            record.equipment_name[:20],  # Truncate if too long
            record.equipment_type[:15],
            f'{record.flowrate:.1f}',
            f'{record.pressure:.1f}',
            f'{record.temperature:.1f}',
        ])
    
    records_table = Table(records_data, colWidths=[2 * inch, 1.5 * inch, 1 * inch, 1 * inch, 1 * inch])
    records_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3f51b5')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f5f5f5')]),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ]))
    
    elements.append(records_table)
    
    if dataset.total_count > 20:
        note = Paragraph(
            f"<i>Note: Showing first 20 of {dataset.total_count} records</i>",
            styles['Normal']
        )
        elements.append(Spacer(1, 0.1 * inch))
        elements.append(note)
    
    # Footer
    elements.append(Spacer(1, 0.4 * inch))
    footer = Paragraph(
        f"<i>Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</i>",
        ParagraphStyle('Footer', parent=styles['Normal'], alignment=TA_CENTER, fontSize=8)
    )
    elements.append(footer)
    
    # Build PDF
    doc.build(elements)
    buffer.seek(0)
    return buffer
