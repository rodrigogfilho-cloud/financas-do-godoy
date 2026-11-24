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



        tabela_despesas = ft.DataTable(
        columns=[ft.DataColumn(ft.Text(value="ID DAS DESPESAS",
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
        size=20)),
        ft.DataColumn(ft.Text(value="AÇÃO",
                color="#ffffff",
                weight="BOLD",
                size=20)),

    
        
        ],
        rows=self.lista_despesas,

         )

        

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
                    ft.DataCell(ft.Text(despesa.get("tipo"),
                                        text_align="center", color="#FFFFFF",weight="BOLD")),
                    ft.DataCell(ft.Text(despesa.get("valor"),
                                        text_align="center", color="#FFFFFF",weight="BOLD")),
                    ft.DataCell(ft.Text(str(despesa.get("data")),
                                        text_align="center", color="#FFFFFF", weight="BOLD")),

                    ft.DataCell(ft.FloatingActionButton(icon=ft.Icons.DELETE,
                                                             height=40,
                                                             width=40,
                                                             bgcolor="#F7BD7B",
                                                             hover_color='#D16500',
                                                             on_click=self.excluir_despesa))
                    
                ],
                
            )
            self.lista_despesas.append(linha)
            
        self.pagina.update()

    def excluir_despesa(self):
           
                  

            

    