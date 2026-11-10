import flet as ft

class Despesas(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()
        self.pagina = pagina

        

    

        self.route = "/despesas"
        self.bgcolor = "#DDCCDD"
        self.vertical_alignment="center"
        self.horizontal_alignment="center"

        # Textos

        bem_vindo = ft.Text(value="Cadastrar despesas",
                            size=35,
                            weight="BOLD",
                            font_family="georgia",
                            color="#8000a0"
                                                 )

        self.controls = [bem_vindo]