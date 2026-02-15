from types import FunctionType
from typing import Any

import flet as ft

from components.Add_dialog import Add_dialog
from components.Edit_dialog import Edit_dialog
from components.My_snackbar import My_snackbar
from components.Note_Card import Note_card
from core.db.todos import Todos_manager


class Handlers:
    def __init__(self) -> None:
        self.__todos = Todos_manager()
        self.__current_todo = None

    def read_todos(self) -> list[Any]:
        res = self.__todos.read_all()
        if not res or len(res) == 0:
            print("No hay notas creadas")
            return []
        return res

    def create_todo(
        self, title: str, text: str, render_cb: FunctionType, snack_cb: FunctionType
    ) -> None:
        res = self.__todos.create(title, text)
        if not res:
            return
        snack_cb("La nota ha sido creada")
        render_cb()

    def update_todo(
        self,
        id: int,
        title: str,
        text: str,
        render_cb: FunctionType,
        snack_cb: FunctionType,
    ):
        res = self.__todos.update(id, title, text)
        if not res:
            return
        snack_cb("La nota ha sido actualizada")
        render_cb()

    def remove_todo(
        self,
        id: int,
        render_cb: FunctionType,
        snack_cb: FunctionType,
    ):
        res = self.__todos.delete(id)
        if not res:
            return
        snack_cb("La nota ha sido eliminada")
        render_cb()


def main(page: ft.Page):
    # -------------------INITIALIZATION---------------------------
    handlers = Handlers()
    todos: list[Any] = []

    # -------------------FUNCTIONS---------------------------
    def render():
        nonlocal todos
        todos = handlers.read_todos()
        page.clean()
        page.add(
            ft.SafeArea(
                expand=True,
                content=Content(),
            )
        )

    def close_dialog():
        page.pop_dialog()

    def open_dialog(dialog_name: ft.DialogControl):
        page.show_dialog(dialog_name)

    def render_snackbar(msg: str):
        my_snackbar = My_snackbar(msg, close_dialog)
        page.show_dialog(my_snackbar)

    def render_edit_dialog(id, title, text) -> None:
        edit_dialog = Edit_dialog(
            id, title, text, close_dialog, handlers.update_todo, render, render_snackbar
        )
        open_dialog(edit_dialog)

    def get_data_from_notecard(id: int, title: str, text: str) -> None:
        render_edit_dialog(id, title, text)

    # -------------------COMPONENTS---------------------------
    add_dialog = Add_dialog(close_dialog, handlers.create_todo, render, render_snackbar)
    page.window.width = 360
    page.padding = 4
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=lambda _: open_dialog(add_dialog), elevation=10
    )
    page.appbar = ft.AppBar(
        title="Notas Locas", bgcolor=ft.Colors.SURFACE_CONTAINER_LOW
    )

    @ft.observable
    @ft.control
    class Content(ft.Column):
        def init(self):
            self.expand = True
            self.scroll = ft.ScrollMode.AUTO
            self.controls = [
                ft.GridView(
                    [
                        Note_card(
                            i[0],
                            i[1],
                            i[2],
                            i[3],
                            get_data_from_notecard,
                            handlers.remove_todo,
                            render,
                            render_snackbar,
                        )
                        for i in todos
                    ],
                    max_extent=220,
                    expand=True,
                    spacing=1,
                    run_spacing=1,
                    child_aspect_ratio=0.5,
                )
            ]

    # -------------------I N I T  R E N D E R---------------------------
    render()


if __name__ == "__main__":
    ft.run(main)
