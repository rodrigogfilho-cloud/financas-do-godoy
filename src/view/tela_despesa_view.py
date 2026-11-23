import flet as ft
from src.model.despesa_model import Despesa

class TodasDespesas(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()
        self.pagina = pagina

        dados_usuario = pagina.session.store.get("usuario_logado")
                               
        self.id_usuario = dados_usuario.get("id_usuario")

        
        todas_as_despesas = []
    

        self.route = "/all_despesas"
        self.bgcolor = "#ceb095"
        self.vertical_alignment="center"
        self.horizontal_alignment="center"

        # Textos

        txt = ft.Text(value="TODAS DESPESAS",
                            size=30,
                            weight="BOLD",
                            font_family="georgia",
                            color="#E67E08"
                                                 )

        # Historico

        tabela_despesas = ft.DataTable(columns=[ft.DataColumn(label="ID DAS DESPESAS"),
                                                ft.DataColumn(label="DESCRIÇÃO"),
                                                ft.DataColumn(label="CATEGORIA"),
                                                ft.DataColumn(label="VALOR"),
                                                ft.DataColumn(label="DATA"),],
                                                rows=[
                                                    ft.DataRow(cells=[

                                                    ])
                                                ])



        # Botões

        botao_excluir_despesa = ft.FloatingActionButton(icon=ft.Icons.DELETE,
                                                        bgcolor="#F7BD7B",
                                                        hover_color="#D16500",
                                                        width=50,
                                                        height=50,)

        

        self.controls = [txt,
                         tabela_despesas
                         ]