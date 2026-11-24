
import flet as ft
from src.model.despesa_model import Despesa
from src.model.categoria_model import Categoria


class DespesaPorCategoria(ft.View):
    def __init__(self, pagina: ft.Page):
        super().__init__()

        self.pagina = pagina

        dados_usuario = pagina.session.store.get("usuario_logado")
        self.id_usuario = dados_usuario.get("id_usuario")

        self.route = "/desp_por_cat"
        self.bgcolor = "#fdcbcb"
        self.horizontal_alignment = "center"

        txt = ft.Text(
            value="DESPESAS POR CATEGORIA",
            size=30,
            weight="BOLD",
            font_family="georgia",
            color="#F30202"
        )

        opcoes_categoria = []

        categorias = Categoria().recuperar(self.id_usuario)

        for categoria in categorias:
            opcao = ft.DropdownOption(
                key=str(categoria.get("id_categoria")),
                text=categoria.get("tipo")
            )
            opcoes_categoria.append(opcao)

        self.lista_despesas = []

        self.campo_categorias = ft.Dropdown(
            options=opcoes_categoria,
            on_select=self.atualizar_despesas
        )

        self.tabela_despesas = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID DAS DESPESAS",color="#ffffff",
                        weight="BOLD",
                        size=20)),
                ft.DataColumn(ft.Text("DESCRIÇÃO",color="#ffffff",
                        weight="BOLD",
                        size=20)),
                ft.DataColumn(ft.Text("CATEGORIA",color="#ffffff",
        weight="BOLD",
        size=20)),
                ft.DataColumn(ft.Text("VALOR",color="#ffffff",
        weight="BOLD",
        size=20)),
                ft.DataColumn(ft.Text("DATA",color="#ffffff",
        weight="BOLD",
        size=20)),
                ft.DataColumn(ft.Text("AÇÃO",color="#ffffff",
        weight="BOLD",
        size=20))
            ],
            rows=self.lista_despesas
        )

        self.controls = [
            txt,
            self.campo_categorias,
            self.tabela_despesas
        ]

        self.atualizar_despesas()

    def atualizar_despesas(self, e=None):

        self.lista_despesas.clear()

        id_categoria = self.campo_categorias.value

        if id_categoria is None:
            self.tabela_despesas.rows = []
            self.pagina.update()
            return

        despesas = Despesa().recuperacao_especifica(
            self.id_usuario,
            id_categoria
        )

        for despesa in despesas:

            linha = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(despesa.get("id_despesa",
                                        )),text_align="center", color="#FFFFFF", weight="BOLD")),
                    ft.DataCell(ft.Text(despesa.get("descricao",
                                        ),text_align="center", color="#FFFFFF", weight="BOLD")),
                    ft.DataCell(ft.Text(despesa.get("tipo",
                                        ),text_align="center", color="#FFFFFF", weight="BOLD")),
                    ft.DataCell(ft.Text(str(despesa.get("valor",
                                        )),text_align="center", color="#FFFFFF", weight="BOLD")),
                    ft.DataCell(ft.Text(str(despesa.get("data",
                                        )),text_align="center", color="#FFFFFF", weight="BOLD")),

                    ft.DataCell(
                        ft.IconButton(
                            icon=ft.Icons.DELETE,
                            key=despesa.get("id_despesa"),
                            on_click=self.excluir_despesa
                        ))
                ]
            )

            self.lista_despesas.append(linha)

        self.tabela_despesas.rows = self.lista_despesas
        self.pagina.update()

    def excluir_despesa(self, botao):

        id_despesa = botao.control.key

        Despesa().excluir(id_despesa)

        self.atualizar_despesas()
