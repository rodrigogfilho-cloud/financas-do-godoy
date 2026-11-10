import flet as ft


class Home(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()
        self.pagina = pagina

    

        self.route = "/home"
        self.bgcolor = "#eb9feb"
        self.vertical_alignment="center"
        self.horizontal_alignment="center"

        title = ft.Text(value="Tela principal",
                        size=35,
                        margin=30,
                        weight="BOLD",
                         font_family="georgia",
                         color="#fa1fca"
                     
                        )

        self.controls = [
            title
        ]