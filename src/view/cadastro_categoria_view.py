import flet as ft
from src.view.login_usuario_view import LoginUsuarioView


class Home(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()
        self.pagina = pagina

        

    

        self.route = "/home"
        self.bgcolor = "#eb9feb"
        self.vertical_alignment="center"
        self.horizontal_alignment="center"

        # Textos

        bem_vindo = ft.Text(value=)

        title = ft.Text(value="CADASTRE SUAS CATEGORIAS",
                        size=35,
                        margin=30,
                        weight="BOLD",
                         font_family="georgia",
                         color="#fa1fca"
                     
                        )

        texto_de_nao_cadastrar_categoria = ft.Text(value="Não deseja cadastrar uma categoria?",
                                                   weight="BOLD",
                                                    bgcolor="transparent",
                                                    color="#302F2F",
                                                   )

        # CAMPOS

        campo_adicionar_categoria = ft.TextField(label='Categoria',
                                    value='',
                                   bgcolor="#fdfdfdff", 
                                    color="#000000",
                                )

        campo_recuperar_categorias = ft.TextField(label='Recuperar categorias',
                                                  value='',
                                                  bgcolor="#fdfdfdff", 
                                                  color="#000000",
                                                  )

        campo_excluir_categoria = ft.TextField(label='Qual Categoria você deseja excluir?',
                                               value='',
                                                bgcolor="#fdfdfdff", 
                                                color="#000000",)

        # BOTÕES

        botao_add = ft.FloatingActionButton(icon=ft.Icons.ADD,
                                            bgcolor="#E765DC",
                                           hover_color="#C202B8",
                                            width=80,
                                            height=80)

        botao_recuperar = ft.FloatingActionButton(icon=ft.Icons.SEARCH,
                                                   bgcolor="#E765DC",
                                                    hover_color="#C202B8",
                                                    width=80,
                                                    height=80)

        botao_excluir = ft.FloatingActionButton(icon=ft.Icons.DELETE,
                                                 bgcolor="#E765DC",
                                                  hover_color="#C202B8",
                                                width=80,
                                                height=80)

        botao_nao_cadastrar = ft.Button(content=ft.Text(value='Pular etapa', weight="BOLD"),
                                        bgcolor="transparent", 
                                        elevation=0,
                                        color="#030303",
                                        height=40,)

        # Linhas e colunas

        linha_add = ft.Row(controls=[campo_adicionar_categoria, botao_add],alignment="center")

        linha_rec = ft.Row(controls=[campo_recuperar_categorias, botao_recuperar],alignment="center")

        linha_delete = ft.Row(controls=[campo_excluir_categoria, botao_excluir],alignment="center")

        linha_pular_etapa =ft.Row(controls=[texto_de_nao_cadastrar_categoria, botao_nao_cadastrar],alignment="center")
        

        self.controls = [
            title,
            linha_add,
            linha_rec,
            linha_delete,
            linha_pular_etapa
        ]

        # DEF´S

        