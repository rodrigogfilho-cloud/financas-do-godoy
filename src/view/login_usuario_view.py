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
                        margin=40,
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

    

        botao_de_login = ft.Button(content=ft.Text("Fazer Login",weight="BOLD"),
                                   bgcolor="#fce51c", 
                                    color="#302F2F",
                                    width=250,
                                    height=40,
                                    margin=50
                                    
                                    )

      

        # CONTROLS

        self.controls = [title,
                         coluna_de_campos,
                         botao_de_login]