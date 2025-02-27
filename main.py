import flet as ft
import os

def main(page: ft.Page):
    page.title = "Mi App Flet en Render"
    page.bgcolor = ft.colors.BLUE_50  # Color de fondo
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text("Bienvenido a mi App en Render", size=20, weight=ft.FontWeight.BOLD)

    contador = ft.Text("0", size=30, color=ft.colors.BLUE)
    
    def aumentar(e):
        contador.value = str(int(contador.value) + 1)
        page.update()
    
    boton = ft.ElevatedButton("Aumentar", on_click=aumentar, bgcolor=ft.colors.BLUE, color=ft.colors.WHITE)

    page.add(titulo, contador, boton)

ft.app(target=main, view=ft.WEB_BROWSER, port=int(os.getenv("PORT", 8000)))
