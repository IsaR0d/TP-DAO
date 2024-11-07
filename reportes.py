from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


def generar_reporte_mas_libros():
    #Consulta SQL
    data = [("ID", "Nombre", "Apellido", "Prestamos"),(1, 'Juan', 'Perez', 6), (2, 'Maria', 'Gomez', 8), (3, 'Pedro', 'Gonzalez', 10), (4, 'Ana', 'Lopez', 12)]
    #Crear un documento
    doc = SimpleDocTemplate("./reportes/reporte_mas_libros.pdf", pagesize=letter)
    #Lista de elementos
    elements = []

    styles = getSampleStyleSheet()

    title = "Reporte de usuarios con mas libros prestados"
    elements.append(Paragraph(title, styles['Title']))

    #Crear tabla
    t = Table(data, colWidths=[1 * inch, 1 * inch, 1 * inch, 1 * inch])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                           ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                           ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                           ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                           ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                           ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                           ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    

    elements.append(t)
    doc.build(elements)


def generar_reporte_mas_prestados():
    #Consulta SQL
    data = [("ISBN", "Titulo", "Autor", "Prestamos", "Fecha prestamo" ), ("978-987-612-778-9", "El principito", "Antoine de Saint-Exupéry", 6, "2021-10-01"), ("978-987-612-778-9", "El principito", "Antoine de Saint-Exupéry", 6, "2021-10-01"), ("978-987-612-778-9", "El principito", "Antoine de Saint-Exupéry", 6, "2021-10-01"), ("978-987-612-778-9", "El principito", "Antoine de Saint-Exupéry", 6, "2021-10-01")]


    doc = SimpleDocTemplate("reporte_mas_prestamos.pdf", pagesize=letter)
    #Lista de elementos
    elements = []

    styles = getSampleStyleSheet()

    title = "Reporte de libros mas prestados en el ultimo mes"
    elements.append(Paragraph(title, styles['Title']))

    #Crear tabla
    t = Table(data, colWidths=[1.6 * inch, 2.5 * inch, 2 * inch, 0.8 * inch, 1.2 * inch])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                           ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                           ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                           ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                           ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                           ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                           ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(t)
    doc.build(elements)


def generar_reporte_prestamos_vencidos():
    #Consulta SQL
    data = [("ID", "Nombre", "Apellido", "Titulo", "Fecha Prestamo", "Fecha Vencimiento"), (1, 'Juan', 'Perez', 'El principito', '2021-10-01', '2021-10-15'), (2, 'Maria', 'Gomez', 'El principito', '2021-10-01', '2021-10-15'), (3, 'Pedro', 'Gonzalez', 'El principito', '2021-10-01', '2021-10-15'), (4, 'Ana', 'Lopez', 'El principito', '2021-10-01', '2021-10-15')]

    doc = SimpleDocTemplate("reporte_mas_prestamos.pdf", pagesize=letter)
    #Lista de elementos
    elements = []

    styles = getSampleStyleSheet()

    title = "Reporte de prestamos vencidos"
    elements.append(Paragraph(title, styles['Title']))

    #Crear tabla
    t = Table(data, colWidths=[0.5 * inch, 1 * inch, 1 * inch, 2.8 * inch, 1.2 * inch, 1.3 * inch])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                           ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                           ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                           ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                           ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                           ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                           ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(t)
    doc.build(elements)
    