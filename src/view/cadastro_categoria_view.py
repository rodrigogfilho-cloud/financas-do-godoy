import flet as ft
from src.model.categoria_model import Categoria


class Home(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()
        self.pagina = pagina

        

    

        self.route = "/home"
        self.bgcolor = "#eb9feb"
        self.vertical_alignment="center"
        self.horizontal_alignment="center"

        # Textos

        bem_vindo = ft.Text(value="BEM VINDO!!!",
                            size=35,
                            weight="BOLD",
                            font_family="georgia",
                            color="#fa1fca"
                                                 )

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

        self.campo_nome_usuario = ft.TextField(label='Usuário | Login',
                                            value='',
                                           bgcolor="#fdfdfdff", 
                                            color="#000000",
                                        )

        self.campo_adicionar_categoria = ft.TextField(label='Categoria',
                                    value='',
                                   bgcolor="#fdfdfdff", 
                                    color="#000000",
                                )

        self.campo_recuperar_categorias = ft.TextField(label='Recuperar categorias',
                                                  value='',
                                                  bgcolor="#fdfdfdff", 
                                                  color="#000000",
                                                  )

        self.campo_excluir_categoria = ft.TextField(label='Qual Categoria você deseja excluir?',
                                               value='',
                                                bgcolor="#fdfdfdff", 
                                                color="#000000",)

        # BOTÕES

        botao_add = ft.FloatingActionButton(icon=ft.Icons.ADD,
                                            bgcolor="#E765DC",
                                           hover_color="#C202B8",
                                            width=50,
                                            height=50,
                                            on_click=self.adicionar,)

        botao_recuperar = ft.FloatingActionButton(icon=ft.Icons.SEARCH,
                                                   bgcolor="#E765DC",
                                                    hover_color="#C202B8",
                                                    width=50,
                                                    height=50)

        botao_excluir = ft.FloatingActionButton(icon=ft.Icons.DELETE,
                                                 bgcolor="#E765DC",
                                                  hover_color="#C202B8",
                                                width=50,
                                                height=50)

        botao_nao_cadastrar = ft.Button(content=ft.Text(value='Pular etapa', weight="BOLD"),
                                        bgcolor="transparent", 
                                        elevation=0,
                                        color="#030303",
                                        height=40,
                                        on_click=self.ir_para_despesas)

        # Linhas e colunas

        linha_add = ft.Row(controls=[self.campo_adicionar_categoria, botao_add],alignment="center")

        linha_rec = ft.Row(controls=[self.campo_recuperar_categorias, botao_recuperar],alignment="center")

        linha_delete = ft.Row(controls=[self.campo_excluir_categoria, botao_excluir],alignment="center")

        linha_pular_etapa =ft.Row(controls=[texto_de_nao_cadastrar_categoria, botao_nao_cadastrar],alignment="center")
        

        self.controls = [
            bem_vindo,
            title,
            self.campo_nome_usuario,
            linha_add,
            linha_rec,
            linha_delete,
            linha_pular_etapa
        ]

        # DEF´S

        # Criação da def para ir para despesas, fazer isso depois

    async def ir_para_despesas (self):
                await self.pagina.push_route("/despesas")

    async def adicionar (self):
           categoria = self.campo_adicionar_categoria.value
           usuario = self.campo_nome_usuario.value

           if categoria == "" or usuario == "":
            self.pagina.show_dialog(ft.SnackBar(content=ft.Text(value="Preencha os campos",
                               color="#FFFFFF",
                               weight="BOLD", 
                               text_align="center"),bgcolor="#fce51c",
                                   ))
            return


           if Categoria().adicionar(categoria,usuario):
                 self.pagina.show_dialog(ft.SnackBar(content=ft.Text(value="CATEGORIA JÁ EXISTENTE ❌",
                                                                      color="#FFFFFF",
                                                                      weight="BOLD", 
                                                                      text_align="center"),bgcolor="#d41e1e",
                                                                          ))
                
           else:
                self.pagina.show_dialog(ft.SnackBar(content=ft.Text(value="CATEGORIA CRIADA 👍",
                                                                                     color="#FFFFFF",
                                                                                     weight="BOLD", 
                                                                                     text_align="center"),bgcolor="#158000",
                                                                                         ))
                
           

        

        