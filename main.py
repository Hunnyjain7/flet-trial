import flet as ft


def main(page: ft.Page):
    page.title = "Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.TextField(
            label="Email",
            hint_text="Please enter your Email",
            width=400,
            height=50
        ),
        ft.TextField(
            label="Password with reveal button",
            hint_text="Please enter your Password",
            password=True, can_reveal_password=True,
            width=400,
            height=50
        ),
        ft.Container(
            left=True,
            content=ft.Text("Login"),
            margin=10,
            padding=10,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLUE_200,
            width=150,
            height=50,
            border_radius=10,
            on_click=lambda e: print("Clickable transparent with Ink clicked!"),
        ),
    )


def homepage(page: ft.Page):
    page.title = "Homepage"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.TextField(
            label="Email",
            hint_text="Please enter your Email",
            width=400,
            height=50
        ),
        ft.TextField(
            label="Password with reveal button",
            hint_text="Please enter your Password",
            password=True, can_reveal_password=True,
            width=400,
            height=50
        ),
    )


ft.app(target=main, view=ft.WEB_BROWSER)
# ft.app(target=main)
