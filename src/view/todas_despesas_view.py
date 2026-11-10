import flet as ft

class TodasDespesas(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()
        self.pagina = pagina

        

    

        self.route = "/all_despesas"
        self.bgcolor = "#ceb095"
        self.vertical_alignment="center"
        self.horizontal_alignment="center"

        # Textos

        bem_vindo = ft.Text(value="TODAS DESPESAS",
                            size=35,
                            weight="BOLD",
                            font_family="georgia",
                            color="#E67E08"
                                                 )

        self.controls = [bem_vindo]