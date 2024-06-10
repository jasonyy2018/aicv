from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

def generate_resume(name, email, phone, address, education, experience, skills, template):
    pdf_path = 'resume.pdf'
    doc = SimpleDocTemplate(pdf_path, pagesize=A4)
    story = []

    styles = getSampleStyleSheet()
    style_title = styles[template['title']]
    style_heading = styles[template['heading_style']]
    style_body = styles[template['body_style']]

    story.append(Paragraph(name, style_title))
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"Email: {email}", style_body))
    story.append(Paragraph(f"Phone: {phone}", style_body))
    story.append(Paragraph(f"Address: {address}", style_body))
    story.append(Spacer(1, 12))
    story.append(Paragraph("教育背景", style_heading))
    for year, content in education:
        story.append(Paragraph(f"{year}: {content}", style_body))
    story.append(Spacer(1, 12))
    story.append(Paragraph("工作经历", style_heading))
    for year, content in experience:
        story.append(Paragraph(f"{year}: {content}", style_body))
    story.append(Spacer(1, 12))
    story.append(Paragraph("技能", style_heading))
    for year, content in skills:
        story.append(Paragraph(f"{year}: {content}", style_body))
    story.append(Spacer(1, 12))

    doc.build(story)

    return pdf_path