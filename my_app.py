from docx import Document
import pyttsx3

def speak(text):
    pyttsx3.speak(text)

document = Document()

name = input('name ')
phone_number = input('phone ')
email = input('email ')

document.add_paragraph(name + ' | ' + phone_number + ' | ' + email)

document.save('cv.docx')