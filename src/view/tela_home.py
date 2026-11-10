import flet as ft

class Principal(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()
        self.pagina = pagina

        

    

        self.route = "/principal"
        self.bgcolor = "#eb9feb"
        self.vertical_alignment="center"
        self.horizontal_alignment="center"

        # Textos

        bem_vindo = ft.Text(value="PRINCIPAL",
                            size=35,
                            weight="BOLD",
                            font_family="georgia",
                            color="#fa1fca"
                                                 )

        self.controls = [bem_vindo]