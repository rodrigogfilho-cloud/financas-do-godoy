import flet as ft

class Despesas(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()
        self.pagina = pagina

        dados_usuario = pagina.session.store.get("usuario_logado")
        
        id_do_infeliz = dados_usuario.get("id_usuario")

    

        self.route = "/despesas"
        self.bgcolor = "#DDCCDD"
        self.vertical_alignment="center"
        self.horizontal_alignment="center"

        # Textos

        bem_vindo = ft.Text(value="Cadastre suas despesas",
                            size=35,
                            weight="BOLD",
                            font_family="georgia",
                            color="#8000a0"
                                                 )

        textinho_id = ft.Text(value=f"Cada usuario contém seu ID para fazer cadastros de categorias e despesas. Seu ID Usuário é : {id_do_infeliz}. ",
                                   size=20,
                                    weight="BOLD",
                                    font_family="georgia",
                                    color="#FFFFFF",
                                    margin= 50,
                                    )

        self.controls = [bem_vindo,
                         textinho_id,
                         ]