import flet as ft

class CadastroUsuarioView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.bgcolor = "#eeeeee"
        self.vertical_alignment="center"
        self.horizontal_alignment="center"

        title = ft.Text(value="CADASTRE SEU USUÁRIO",
                        size=35,
                        margin=50,
                        weight="BOLD"
                     
                        )

        # CAMPOS

        campo_login = ft.TextField(label='Usuário',
                                    value='',
                                   bgcolor="#fdfdfdff", 
                                    color="#000000",
                              )

        campo_senha = ft.TextField(label='Senha',
                                   value='',
                                   bgcolor="#fdfdfdff", 
                                    color="#000000",
                                    password=True,
                                    can_reveal_password=True
                              )

        coluna_de_campos = ft.Column(controls=[campo_login, campo_senha],
                                     )

        # BOTÕES

        botao_de_cadastrar = ft.Button(content="Cadastrar-se",
                                       bgcolor="#fdfdfdff", 
                                       color="#000000",
                                       width=200,
                                       height=40,
                                       
                                      )

        botao_de_login = ft.Button(content="Fazer Login",
                                   bgcolor="#fdfdfdff", 
                                    color="#000000",
                                    width=200,
                                    height=40,
                                    )

        coluna_de_botoes = ft.Column(controls=[botao_de_cadastrar, botao_de_login],
                                     margin=50)

        # CONTROLS

        self.controls = [title,
                         coluna_de_campos,
                         coluna_de_botoes]

   