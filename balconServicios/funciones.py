from random import choice
import os
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle, Image
from datetime import date, datetime
from textwrap import wrap


def get_numero_cuenta(numero: int, tipo: str) -> str:
    numero += 1
    cuenta = 'CC'
    if tipo == 'Ahorros':
        cuenta = 'CA'

    # Genera el string del numero de cuenta
    return cuenta + ((5 - len(str(numero)))*'0')+str(numero)


def get_passwd():
    alfabeto = 'abcdefghijklmnopqrstuvwxyz1234567890'
    password = ''
    password = password.join([choice(alfabeto) for i in range(8)])
    return password


def get_nombre_usuario(nombre: str, apellido: str) -> str:
    return (nombre[0]+apellido).upper()


def generar_pdf(datos: dict):

    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    # Header
    t = c.beginText()
    c.setLineWidth(.3)
    c.setFont('Helvetica', 22)
    c.drawString(30, 750, 'Segundo Banco Nacional')

    c.setFont('Helvetica', 22)
    c.drawString(150, 700, 'Contrato de Cuenta Bancaria')

    c.setFont('Helvetica-Bold', 12)
    c.drawString(480, 750, date.isoformat(date.today()))
    c.line(460, 747, 560, 747)
    

    t.setFont('Helvetica', 10)
    t.setCharSpace(1)
    texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur tincidunt, est ac dapibus mollis, erat ex maximus risus, quis mattis eros eros eget risus. Sed tempus pellentesque diam, ut placerat risus congue et. Nulla vel lacinia lectus. Praesent iaculis ipsum vel eros convallis, a vehicula enim rhoncus. Donec posuere cursus sapien vel commodo. Morbi sem risus, finibus sed malesuada id, dignissim non felis. Sed feugiat dictum sem, in condimentum tellus tempor vel. Cras id feugiat urna, quis molestie urna. Quisque at dolor ut felis bibendum scelerisque sit amet vel mi. Curabitur eget metus arcu. Curabitur lorem libero, hendrerit ut tincidunt pulvinar, porta et sapien. Mauris id sapien eros. Pellentesque quis sem ac elit accumsan feugiat. Duis blandit commodo magna, eget malesuada diam elementum ac."
    texto = '\n'.join(wrap(texto, 90))
    t.setTextOrigin(50, 680)
    t.textLines(texto)
    c.drawText(t)

    c.setFont('Helvetica', 10)
    c.drawString(50, 550, 'No de Cuenta : {}'.format(datos['numero_cuenta']))
    c.drawString(50, 530, 'Nombre y Apellido : {} {}'.format(datos['nombre'], datos['apellido']))
    c.drawString(50, 510, 'No identificación : {}'.format(datos['identificacion']))
    c.drawString(50, 490, 'Dirección : {}'.format(datos['direccion']))
    c.drawString(50, 470, 'Telefono : {} '.format(datos['telefono']))
    c.drawString(50, 450, 'Tipo de Cuenta : {} '.format(datos['tipo_cuenta']))
    c.line(50, 400, 150, 400)

    c.setFont('Helvetica', 10)
    c.drawString(50, 390, 'FIRMA')
    c.showPage()
    c.save()

    pdf = buffer.getvalue()
    buffer.close()
    return(pdf)

