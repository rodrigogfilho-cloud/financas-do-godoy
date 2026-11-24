import flet as ft
from src.model.despesa_model import Despesa


class TodasDespesas(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()
        self.pagina = pagina

        dados_usuario = pagina.session.store.get("usuario_logado")
                               
        self.id_usuario = dados_usuario.get("id_usuario")

        
        self.lista_despesas = []

        
            
    

        self.route = "/all_despesas"
        self.bgcolor = "#ceb095"
        # self.vertical_alignment="center"
        self.horizontal_alignment="center"

        # Textos

        txt = ft.Text(value="TODAS DESPESAS",
                            size=30,
                            weight="BOLD",
                            font_family="georgia",
                            color="#E67E08"
                                                 )

        # Historico



        tabela_despesas = ft.DataTable(columns=[ft.DataColumn(ft.Text(value="ID DAS DESPESAS",
        color="#ffffff",
        weight="BOLD",
        size=20)),
                                                ft.DataColumn(ft.Text(value="DESCRIÇÃO",
                                                color="#ffffff",
                                                weight="BOLD",
                                                size=20)),
                                                ft.DataColumn(ft.Text(value="CATEGORIA",
                                                color="#ffffff",
                                                weight="BOLD",
                                                size=20)),
                                                ft.DataColumn(ft.Text(value="VALOR",
                                                color="#ffffff",
                                                weight="BOLD",
                                                size=20)),
                                                ft.DataColumn(ft.Text(value="DATA",
                                                color="#ffffff",
                                                weight="BOLD",
                                                size=20)),],
                                                rows=self.lista_despesas,

                                              
                                                
                                                    )


        despesas = Despesa().recuperar(self.id_usuario)
        
                # for x in despesas:



        # Botões

        botao_excluir_despesa = ft.FloatingActionButton(icon=ft.Icons.DELETE,
                                                        bgcolor="#F7BD7B",
                                                        hover_color="#D16500",
                                                        width=50,
                                                        height=50,)

        self.atualizar_despesas()

        self.controls = [txt,
                         tabela_despesas
                         ]

    def atualizar_despesas(self):
        despesas = Despesa().recuperar(self.id_usuario)

        for despesa in despesas:
            linha = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(despesa.get("id_despesa",),
                                        text_align="center", color="#FFFFFF", weight="BOLD")),
                    ft.DataCell(ft.Text(despesa.get("descricao"),
                                        text_align="center", color="#FFFFFF",weight="BOLD")),
                    ft.DataCell(ft.Text(despesa.get("id_categoria"),
                                        text_align="center", color="#FFFFFF",weight="BOLD")),
                    ft.DataCell(ft.Text(despesa.get("valor"),
                                        text_align="center", color="#FFFFFF",weight="BOLD")),
                    ft.DataCell(ft.Text(despesa.get("data"),
                                        text_align="center", color="#FFFFFF", weight="BOLD")),
                ]
            )

            self.lista_despesas.append(linha)

        self.pagina.update()

    