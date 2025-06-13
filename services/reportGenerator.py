from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_survey_report_pdf(data) -> BytesIO:
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, height - 50, "Survey Results Report")

    p.setFont("Helvetica", 12)
    y = height - 100
    for item in data:
        line = f"Q{item['questionId']}: {item['question']}"
        avg = f"Average Rate: {item['average_rate']} | Responses: {item['responses']}"
        p.drawString(50, y, line)
        y -= 20
        p.drawString(70, y, avg)
        y -= 30
        if y < 100:
            p.showPage()
            y = height - 50

    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer
