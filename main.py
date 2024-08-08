import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Погода"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    user_data = ft.TextField(label='Введите город', width=400)
    weather_data = ft.Text("")

    def get_info(e):

        if len(user_data.value) < 2:
            return

        API = 'e8121997d7233a3a3dda8fabb56ebcb5'
        URL = f'https://api.openweathermap.org/data/2.5/weather?q={user_data.value}&appid={API}&units=metric'
        res = requests.get(URL).json()
        temp = res['main']['temp']
        weather_data.value = 'Погода: ' + str(temp)
        page.update()

    def change_theme(y):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.SUNNY, on_click=change_theme),
                ft.Text('Погодная программа')
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([user_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([weather_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton(text='Поиск', on_click=get_info)], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main) #view=ft.AppView.WEB_BROWSER (WebSite)
