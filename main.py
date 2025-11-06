import flet as ft

def main_page(page:ft.Page):
    page.title = 'Мое первое приложение'
    greeting_text = ft.Text(value='Привет, как тебя зовут и сколько тебе лет?')



    def on_button_click(_):
        name = name_input.value.strip()
        age = age_input.value.strip()

        print(greeting_text.value)
        greeting_text.value = f'Привет{name} , тебе {age} лет'
        print(greeting_text.value)

        if age:
            greeting_text.color = None
            greeting_text.value = f'Привет {name} , тебе {age} лет'
            age_input.value = None

        else:
            greeting_text.value = 'Введите возраст!'
            greeting_text.color = ft.Colors.RED    

        

        page.update()

            
    name_input = ft.TextField(label='введите имя' , on_submit=on_button_click)
    age_input = ft.TextField(label='введите возраст' , on_submit=on_button_click)
    input_button_text = ft.TextButton(text='send', icon =ft.Icons.SEND_ROUNDED , on_click=on_button_click)

    page.add(greeting_text , name_input ,age_input, input_button_text)


    
ft.app(target=main_page)