import flet as ft

class CadastroUsuarioView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        title = ft.Text(value="Cadastre seu usuário")

        pagina.controls = [title]

   