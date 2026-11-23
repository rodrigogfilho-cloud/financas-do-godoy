import flet as ft
from src.model.categoria_model import Categoria
from src.model.despesa_model import Despesa
from datetime import datetime

class Despesas(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()
        self.pagina = pagina

        dados_usuario = pagina.session.store.get("usuario_logado")
                       
        self.id_usuario = dados_usuario.get("id_usuario")


        self.route = "/despesas"
        self.bgcolor = "#DDCCDD"
        self.vertical_alignment="center"
        self.horizontal_alignment="center"

        # Textos

        text= ft.Text(value="Cadastre suas Despesas 🆒🆒🆒",
                      color="black",
                      size=30,
                      margin=20,
                      weight="BOLD",
                    
                      text_align="center")
        # CAMPOS

        self.descricao = ft.TextField (label='Descrição',
                                    value='',
                                   bgcolor="#fdfdfdff", 
                                    color="#000000",
                                )

        self.valor = ft.TextField (label='Valor',
                                            value='',
                                           bgcolor="#fdfdfdff", 
                                            color="#000000",
                                        )

        self.data = ft.TextField (label='Data',
                                            value='',
                                           bgcolor="#fdfdfdff", 
                                            color="#000000",
                                        )

        opcoes_categoria = []
        categorias = Categoria().recuperar(self.id_usuario)


        for categoria in categorias:
            opcao = ft.DropdownOption(key=categoria.get("id_categoria"),
                              text=categoria.get("tipo"))
            opcoes_categoria.append(opcao)

        self.campo_categorias = ft.Dropdown (options=opcoes_categoria)

        

        # Botões

        botao_cadastrar = ft.Button(content=ft.Text(value="Cadastrar 💜",
                                                    color="#840296"),
                                                    bgcolor="#db96fc",
                                                    on_click=self.incluir)

        self.controls =[
            text,
            self.descricao,
            self.valor,
            self.data, 
            self.campo_categorias,
            botao_cadastrar
        ]

        # ---------------------------------------------------------------------- #

        # DEF´s

    def incluir (self):

        # Pegar os valores dos campos

        descricao = self.descricao.value
        valor = self.valor.value
        data = self.data.value
        id_categoria = self.campo_categorias.value

        data_convertida = datetime.strptime(data, "%d/%m/%Y").date()

        valor1 = float(valor)

        # ---------------------------------------------------------------------- #

        # Envio para meu model para inserir no banco de dados

        Despesa().incluir(self.id_usuario,id_categoria,descricao,valor1,data_convertida)