import flet as ft
from src.model.categoria_model import Categoria


class Home(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()
        self.pagina = pagina

        dados_usuario = pagina.session.store.get("usuario_logado")
                
        self.id_usuario = dados_usuario.get("id_usuario")

    

        self.route = "/home"
        self.bgcolor = "#eb9feb"
        self.vertical_alignment="center"
        self.horizontal_alignment="center"

        # Lista 

        categorias = []

        # Textos

     

        title = ft.Text(value="CADASTRE SUAS CATEGORIAS",
                        size=35,
                        margin=5,
                        weight="BOLD",
                         font_family="georgia",
                         color="#fa1fca"
                     
                        )

        texto_de_nao_cadastrar_categoria = ft.Text(value="Não deseja cadastrar uma categoria?",
                                                   weight="BOLD",
                                                    bgcolor="transparent",
                                                    color="#302F2F",
                                                   )

        textinho_id = ft.Text(value=f"Seu ID Usuário é : {self.id_usuario}. ",
                                           size=20,
                                            weight="BOLD",
                                            font_family="georgia",
                                            color="#FFFFFF",
                                            margin= 50,
                                            )

        # CAMPOS

        self.campo_nome_usuario = ft.TextField(label='ID DO USUÁRIO',
                                            value=self.id_usuario,
                                           bgcolor="#fdfdfdff", 
                                            color="#000000",
                                        )

        self.campo_adicionar_categoria = ft.TextField(label='Categoria',
                                    value='',
                                   bgcolor="#fdfdfdff", 
                                    color="#000000",
                                )

       
        # BOTÕES

        botao_add = ft.FloatingActionButton(icon=ft.Icons.ADD,
                                            bgcolor="#E765DC",
                                           hover_color="#C202B8",
                                            width=50,
                                            height=50,
                                            on_click=self.adicionar,)

        

        botao_nao_cadastrar = ft.Button(content=ft.Text(value='Pular etapa', weight="BOLD"),
                                        bgcolor="transparent", 
                                        elevation=0,
                                        color="#030303",
                                        height=40,
                                        on_click=self.ir_para_despesas)

        # Linhas e colunas

        coluna_add = ft.Column(controls=[self.campo_adicionar_categoria, botao_add],alignment="center",
                               horizontal_alignment=ft.CrossAxisAlignment.CENTER)

        # Histórico



      
        # Linha para pular

        linha_pular_etapa =ft.Row(controls=[texto_de_nao_cadastrar_categoria, botao_nao_cadastrar],alignment="center")
        

        self.controls = [
           
            title,
            textinho_id,
            self.campo_nome_usuario,
           coluna_add,
            linha_pular_etapa
        ]

        # DEF´S

        # Criação da def para ir para despesas, fazer isso depois

    async def ir_para_despesas (self):
                await self.pagina.push_route("/despesas")

    async def adicionar (self):
           categoria = self.campo_adicionar_categoria.value
           usuario = self.campo_nome_usuario.value
           id_usuario = int(usuario)
           

           if categoria == "" or usuario == "":
            self.pagina.show_dialog(ft.SnackBar(content=ft.Text(value="Preencha os campos",
                               color="#FFFFFF",
                               weight="BOLD", 
                               text_align="center"),bgcolor="#fce51c",
                                   ))
            return


           if Categoria().adicionar(categoria,id_usuario):
                 self.pagina.show_dialog(ft.SnackBar(content=ft.Text(value="CATEGORIA CRIADA 👍",
                                                                                                      color="#FFFFFF",
                                                                                                      weight="BOLD", 
                                                                                                      text_align="center"),bgcolor="#158000",
                                                                                                          ))
                 
                 
           else:
                 self.pagina.show_dialog(ft.SnackBar(content=ft.Text(value="CATEGORIA JÁ EXISTENTE ❌",
                                                                                       color="#FFFFFF",
                                                                                       weight="BOLD", 
                                                                                       text_align="center"),bgcolor="#d41e1e",
                                                                                           ))

   