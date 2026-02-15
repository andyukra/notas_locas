from types import FunctionType, MethodType

import flet as ft


class Edit_dialog(ft.AlertDialog):
    def __init__(
        self,
        id: int,
        title: str,
        text: str,
        close_cb: FunctionType,
        update_cb: MethodType,
        render_cb: FunctionType,
        snack_cb: FunctionType,
    ):
        super().__init__()
        self.__id = id
        self.__titulo = title
        self.__texto = text
        self.__close_cb = close_cb
        self.__update_cb = update_cb
        self.__render_cb = render_cb
        self.__snack_cb = snack_cb
        self.title = ft.Text("Editar nota")
        self.__title = ft.TextField(label="Titulo", border_width=3, value=self.__titulo)
        self.__text = ft.TextField(
            label="Contenido",
            border_width=3,
            multiline=True,
            expand=True,
            value=self.__texto,
        )
        self.content = ft.Column([self.__title, self.__text])
        self.modal = True
        self.actions = [
            ft.TextButton("Cancelar", on_click=self.__close_cb),
            ft.TextButton("Guardar", on_click=self.__update_todo),
        ]

    def __update_todo(self):
        if len(self.__title.value.strip()) == 0 or len(self.__text.value.strip()) == 0:
            return
        self.__close_cb()
        self.__update_cb(
            self.__id,
            self.__title.value.strip(),
            self.__text.value.strip(),
            self.__render_cb,
            self.__snack_cb,
        )
        self.__title.value = ""
        self.__text.value = ""
