import flet as ft


class My_snackbar(ft.SnackBar):
    def __init__(self, msg: str, close_cb):
        super().__init__(content=ft.Text(msg))
        self.action = "Cerrar"
        self.on_action = close_cb
