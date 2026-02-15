import textwrap
from types import FunctionType, MethodType

import flet as ft


class Note_card(ft.Card):
    def __init__(
        self,
        id: int,
        title: str,
        text: str,
        created: str,
        send_data: FunctionType,
        remove_cb: MethodType,
        render_cb: FunctionType,
        snack_cb: FunctionType,
    ):
        super().__init__()
        self.elevation = 5
        self.id = id
        self.title = title
        self.text = text
        self.render_cb = render_cb
        self.snack_cb = snack_cb
        self.send_data = send_data
        self.created = created
        self.content = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        textwrap.shorten(self.title, width=30),
                        size=12,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Divider(height=1),
                    ft.Text(
                        textwrap.shorten(self.text, width=270),
                        expand=True,
                        size=12,
                        color=ft.Colors.GREY_300,
                        italic=True,
                    ),
                    ft.Row(
                        [
                            ft.Button(
                                "Editar",
                                on_click=lambda _: send_data(
                                    self.id, self.title, self.text
                                ),
                            ),
                            ft.IconButton(
                                icon=ft.Icons.DELETE,
                                icon_size=20,
                                icon_color=ft.Colors.RED_800,
                                on_click=lambda _: remove_cb(
                                    self.id, self.render_cb, self.snack_cb
                                ),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                    ft.Text(
                        self.created,
                        color=ft.Colors.GREY_400,
                        italic=True,
                        size=10,
                    ),
                ],
                expand=True,
            ),
            padding=10,
        )
