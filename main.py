import flet as ft
import os

def main(page: ft.Page):
    page.title = "Prueba de Deploy en Render"
    page.add(ft.Text("¡Hola, Render! 🎉"))

ft.app(target=main, view=ft.WEB_BROWSER, port=int(os.getenv("PORT", 8000)))  
