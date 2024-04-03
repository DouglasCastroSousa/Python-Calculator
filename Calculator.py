# Python-Calculator

# I have made this Python calculator using only flet and my own skills, enjoy it and take care about the bugs

from flet import *

style = ButtonStyle(shape=RoundedRectangleBorder(radius=6))

def main(page: Page):
    page.title = "Calculadora"
    page.window_height = 380
    page.window_width = 350
    page.window_min_height = 390
    page.window_min_width = 350
    
    def teclado(e):
        data = e.control.data
        lista = list(str(resultado.value))
        # 'AC','◄', '='
        if resultado.value == "0":
            if data not in ['AC','◄','%','/','*','-','+','=','.']:
                resultado.value = str(data)
            elif data == ".":
                resultado.value += str(data)
        else:
            if lista[-1] in ['%','/','*','-','+','.'] and data in ['%','/','*','-','+','.']:
                lista[-1] = data
                novo_resultado = "".join(lista)
                resultado.value = novo_resultado
            elif lista[-1] in ['%','/','*','-','+','.'] and data in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                resultado.value = str(resultado.value) + str(data)
            elif lista[-1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] and data not in ["AC","◄","="]:
                resultado.value = str(resultado.value) + str(data)
            elif data == '=':
                resultado.value = eval(str(resultado.value))
            elif data == 'AC':
                resultado.value = '0'
            elif data == '◄' and len(lista) > 1:
                lista.pop()
                resultado.value = "".join(map(str,lista))
                print(lista)
                page.update()
            else:
                resultado.value = '0'
        page.update()
        
    resultado = TextField(value='0',
                          read_only = True,
                          expand = 1,
                          border_width=4,
                          border_radius=4
                          )
    page.add(
        Row(expand = 1,controls=[resultado]),
        Row(expand=1,controls=[
            
                ElevatedButton(text="AC",
                           expand=True,
                           style=style,
                           height=60,
                           
                           data="AC",
                           on_click=teclado),
            
                ElevatedButton(text="◄",
                           expand=True,
                           height=60,
                           style=style,
                           data="◄",
                           on_click=teclado),
            
                ElevatedButton(text="%",
                           expand=True,
                           height=60,
                           style=style,
                           data="%",
                           on_click=teclado),
            
                ElevatedButton(text="/",
                           expand=True,
                           height=60,
                           style=style,
                           data="/",
                           on_click=teclado)
        ]),
        Row(expand=1,controls=[
            
                ElevatedButton(text="7",
                           expand=True,
                           height=60,
                           style=style,
                           data="7",
                           on_click=teclado),
            
                ElevatedButton(text="8",
                           expand=True,
                           height=60,
                           style=style,
                           data="8",
                           on_click=teclado),
            
                ElevatedButton(text="9",
                           expand=True,
                           height=60,
                           style=style,
                           data="9",
                           on_click=teclado),
            
                ElevatedButton(text="x",
                           expand=True,
                           height=60,
                           style=style,
                           data="*",
                           on_click=teclado)
        ]),
        Row(expand=1,controls=[
            
                ElevatedButton(text="4",
                           expand=True,
                           height=60,
                           style=style,
                           data="4",
                           on_click=teclado),
            
                ElevatedButton(text="5",
                           expand=1,
                           height=60,
                           style=style,
                           data="5",
                           on_click=teclado),
            
                ElevatedButton(text="6",
                           expand=True,
                           height=60,
                           style=style,
                           data="6",
                           on_click=teclado),
            
                ElevatedButton(text="-",
                           expand=True,
                           height=60,
                           style=style,
                           data="-",
                           on_click=teclado)
        ]),
        Row(expand=1,controls=[
            
                ElevatedButton(text="1",
                           expand=True,
                           height=60,
                           style=style,
                           data="1",
                           on_click=teclado),
            
                ElevatedButton(text="2",
                           expand=True,
                           height=60,
                           
                           style=style,
                           data="2",
                           on_click=teclado),
            
                ElevatedButton(text="3",
                           expand=True,
                           height=60,
                           style=style,
                           data="3",
                           on_click=teclado),
            
                ElevatedButton(text="+",
                           expand=True,
                           height=60,
                           style=style,
                           data="+",
                           on_click=teclado)
        ]),
        Row(expand=1,controls=[
            
                ElevatedButton(text="0",
                           expand=2,
                           height=60,
                           style=style,
                           data="0",
                           on_click=teclado),
            
                ElevatedButton(text=".",
                           expand=True,
                           height=60,
                           style=style,
                           data=".",
                           on_click=teclado),
            
                ElevatedButton(text="=",
                           expand=True,
                           height=60,
                           style=style,
                           data="=",
                           on_click=teclado)
        ])
    )
    
    
if __name__ == '__main__':
    app(target=main)#, view=AppView.WEB_BROWSER)
