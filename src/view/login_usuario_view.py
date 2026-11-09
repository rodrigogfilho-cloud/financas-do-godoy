import flet as ft
from src.model.usuario_model import Usuario

class LoginUsuarioView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()
        self.pagina = pagina

        self.route = "/login"
        self.bgcolor = "#fcf373"
        self.vertical_alignment="center"
        self.horizontal_alignment="center"

        title = ft.Text(value="FAÇA O LOGIN",
                        size=35,
                        margin=30,
                        weight="BOLD",
                     
                        )

        # CAMPOS

        self.campo_login = ft.TextField(label='Usuário | LOGIN',
                                    value='',
                                   bgcolor="#fdfdfdff", 
                                    color="#000000",
                              )

        self.campo_senha = ft.TextField(label='Senha',
                                   value='',
                                   bgcolor="#fdfdfdff", 
                                    color="#000000",
                                    password=True,
                                    can_reveal_password=True
                              )

        coluna_de_campos = ft.Column(controls=[self.campo_login, self.campo_senha],
                                     )

        # BOTÕES

    

        botao_de_login = ft.Text(weight="BOLD",
                                   bgcolor="transparent",
                                   color="#302F2F")
        
        botao_para_cadastrar = ft.Button(content=ft.Text("Cadastre-se",weight="BOLD"),
                                   bgcolor="transparent", 
                                   elevation=0,
                                    color="#302F2F",
                                    height=40,
                                 
                                                                        )

        linha_botoes = ft.Row(controls=[botao_de_login, botao_para_cadastrar],
                              alignment="center",
                              margin=40)

      

        # CONTROLS

        self.controls = [title,
                         coluna_de_campos,
                         linha_botoes]