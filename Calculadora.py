import flet as ft
from flet import colors
from decimal import Decimal

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
    page.window_width = 280
    page.window_height = 400
    page.title = 'Calculadora Python'
    page.window_always_on_top = True
    
    result = ft.Text(value='0', color=colors.BLACK, size=35)

    def calculate(operator, value_at):
        try:
            value = eval(value_at)

            if operator == '%':
                value /= 100
            elif operator == '±':
                value = -value
        except:
            return 'Error'
        
        digits = min(abs(Decimal(value).as_tuple().exponent), 5)
        return format(value, f'.{digits}f')
        
    def select(e):
        value_at = result.value if result.value not in ('0', 'Error') else ''
        value = e.control.content.value

        if value.isdigit():
            value = value_at + value
        elif value == 'AC':
            value = '0'
        else:
            if value_at and value_at[-1] in ('/', '*', '-', '+', '.'):
                value_at = value_at[:-1]

            value = value_at + value

            if value[-1] in ('=', '%', '±'):
                value = calculate(operator=value[-1], value_at=value_at)

        result.value = value
        result.update()
        
    
    btn_rows = []
    for i in range(0, len(botoes), 4):
        btn_row = ft.Row(
            width=300,
            wrap=True,
            controls=[
                ft.Container(
                    content=ft.Text(value=btn['operador'], color=btn['fonte']),
                    width=50,
                    height=50,
                    bgcolor=btn['fundo'],
                    border_radius=100,
                    alignment=ft.alignment.center,
                    on_click=select
                ) for btn in botoes[i:i+4]
            ],
            alignment='center',
        )
        btn_rows.append(btn_row)
    
    page.add(result, *btn_rows)

ft.app(target=main)
