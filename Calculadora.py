import flet as ft
from flet import colors

botoes = [
     {'operador': 'AC', 'fonte': colors.BLACK, 'fundo': colors.GREY_200},
     {'operador': '±', 'fonte': colors.BLACK, 'fundo': colors.GREY_200},
     {'operador': '%', 'fonte': colors.BLACK, 'fundo': colors.GREY_200},
     {'operador': '/', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
     {'operador': '7', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
     {'operador': '8', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
     {'operador': '9', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
     {'operador': '*', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
     {'operador': '4', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
     {'operador': '5', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
     {'operador': '6', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
     {'operador': '-', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
     {'operador': '1', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
     {'operador': '2', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
     {'operador': '3', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
     {'operador': '+', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
     {'operador': '0', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
     {'operador': '.', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
     {'operador': '=', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
 ]

def main(page: ft.Page):
    page.bgcolor = '#4F4F4F'
    page.window_resizable = False
    page.window_width = 300
    page.window_height = 400
    page.title = 'Calculadora Python'
    page.window_always_on_top = True    
    
    result = ft.Text(value = 0, color = colors.BLACK, size = 35)
    
    display = ft.Row(
        width=300 ,
        controls=[result] ,
        alignment= 'end',
    )
    
    btn = [ft.Container(
        content=ft.Text(value=btn['operador'], color =btn['fonte']),
        width=50,
        height=50,
        bgcolor=btn['fundo'],
        border_radius=100,
        alignment=ft.alignment.center,
    )for btn in botoes]
    
    keyboard = ft.Row(
        width=300,
        wrap=True,
        controls=btn,
        alignment='end',
    )
    
    page.add(result, btn)
    
    
ft.app(target = main)