"""
PDF Report Generator
Creates beautiful premium PDF reports for baby names
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from typing import Dict
import os
from datetime import datetime

class PDFReportGenerator:
    """Generate premium PDF reports for baby names"""
    
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()
    
    def _setup_custom_styles(self):
        """Setup custom paragraph styles"""
        # Title style
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#FF9933'),
            spaceAfter=30,
            alignment=TA_CENTER
        ))
        
        # Subtitle style
        self.styles.add(ParagraphStyle(
            name='CustomSubtitle',
            parent=self.styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#3E2723'),
            spaceAfter=12,
            alignment=TA_CENTER
        ))
        
        # Name style
        self.styles.add(ParagraphStyle(
            name='NameStyle',
            parent=self.styles['Heading2'],
            fontSize=18,
            textColor=colors.HexColor('#7E57C2'),
            spaceAfter=10
        ))
    
    def generate_report(self, data: Dict) -> str:
        """
        Generate PDF report
        
        Args:
            data: Dictionary containing report data
        
        Returns:
            Path to generated PDF file
        """
        # Create output directory
        output_dir = "reports"
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{output_dir}/naamveda_report_{timestamp}.pdf"
        
        # Create PDF
        doc = SimpleDocTemplate(filename, pagesize=A4)
        story = []
        
        # Add content
        story.extend(self._create_cover_page(data))
        story.append(PageBreak())
        story.extend(self._create_names_section(data))
        story.append(PageBreak())
        story.extend(self._create_numerology_section(data))
        
        # Build PDF
        doc.build(story)
        
        return filename
    
    def _create_cover_page(self, data: Dict) -> list:
        """Create cover page"""
        elements = []
        
        # Title
        elements.append(Spacer(1, 2*inch))
        elements.append(Paragraph("🕉️ Naamveda", self.styles['CustomTitle']))
        elements.append(Paragraph(
            "Premium Baby Name Report",
            self.styles['CustomSubtitle']
        ))
        
        elements.append(Spacer(1, 1*inch))
        
        # User info
        elements.append(Paragraph(
            f"Prepared for: {data.get('user_name', 'Parent')}",
            self.styles['Normal']
        ))
        elements.append(Paragraph(
            f"Date: {datetime.now().strftime('%B %d, %Y')}",
            self.styles['Normal']
        ))
        
        elements.append(Spacer(1, 2*inch))
        
        # Blessing
        blessing = Paragraph(
            "<i>May this name bring prosperity, happiness, and success to your child. "
            "May they grow with wisdom, strength, and compassion.</i>",
            ParagraphStyle(
                'Blessing',
                parent=self.styles['Normal'],
                alignment=TA_CENTER,
                fontSize=12,
                textColor=colors.HexColor('#7E57C2')
            )
        )
        elements.append(blessing)
        
        return elements
    
    def _create_names_section(self, data: Dict) -> list:
        """Create names section"""
        elements = []
        
        elements.append(Paragraph("Recommended Names", self.styles['Heading1']))
        elements.append(Spacer(1, 0.3*inch))
        
        # Add each name
        for i, name_data in enumerate(data.get('names', []), 1):
            elements.append(Paragraph(
                f"{i}. {name_data.get('name', 'Name')}",
                self.styles['NameStyle']
            ))
            
            elements.append(Paragraph(
                f"<b>Meaning:</b> {name_data.get('meaning', 'N/A')}",
                self.styles['Normal']
            ))
            
            elements.append(Paragraph(
                f"<b>Numerology Score:</b> {name_data.get('compatibility_score', 0)}/100",
                self.styles['Normal']
            ))
            
            elements.append(Paragraph(
                f"<b>Why this name:</b> {name_data.get('why_this_name', 'N/A')}",
                self.styles['Normal']
            ))
            
            elements.append(Spacer(1, 0.3*inch))
        
        return elements
    
    def _create_numerology_section(self, data: Dict) -> list:
        """Create numerology analysis section"""
        elements = []
        
        elements.append(Paragraph("Numerology Analysis", self.styles['Heading1']))
        elements.append(Spacer(1, 0.3*inch))
        
        elements.append(Paragraph(
            "Each name has been carefully analyzed using ancient Vedic numerology "
            "to ensure compatibility with your child's life path.",
            self.styles['Normal']
        ))
        
        return elements
