from types import FunctionType, MethodType

import flet as ft


class Add_dialog(ft.AlertDialog):
    def __init__(
        self,
        close_cb: FunctionType,
        save_cb: MethodType,
        render_cb: FunctionType,
        snack_cb: FunctionType,
    ):
        super().__init__()
        self.__close_cb = close_cb
        self.__save_cb = save_cb
        self.__render_cb = render_cb
        self.__snack_cb = snack_cb
        self.title = ft.Text("Agregar nota")
        self.__title = ft.TextField(label="Titulo", border_width=3)
        self.__text = ft.TextField(
            label="Contenido", border_width=3, multiline=True, expand=True
        )
        self.content = ft.Column([self.__title, self.__text])
        self.modal = True
        self.actions = [
            ft.TextButton("Cancelar", on_click=self.__close_cb),
            ft.TextButton(
                "Guardar",
                on_click=self.__save_todo,
            ),
        ]

    def __save_todo(self):
        if len(self.__title.value.strip()) == 0 or len(self.__text.value.strip()) == 0:
            return
        self.__close_cb()
        self.__save_cb(
            self.__title.value.strip(),
            self.__text.value.strip(),
            self.__render_cb,
            self.__snack_cb,
        )
        self.__title.value = ""
        self.__text.value = ""
