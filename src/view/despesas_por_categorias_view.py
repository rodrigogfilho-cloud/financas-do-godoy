import flet as ft

class DespesaPorCategoria(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()
        self.pagina = pagina

        

    

        self.route = "/desp_por_cat"
        self.bgcolor = "#cc9d9d"
        self.vertical_alignment="center"
        self.horizontal_alignment="center"

        # Textos

        bem_vindo = ft.Text(value="DESPESAS POR CATEGORIAS",
                            size=35,
                            weight="BOLD",
                            font_family="georgia",
                            color="#EE0808"
                                                 )

        self.controls = [bem_vindo]