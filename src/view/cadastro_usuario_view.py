import flet as ft
from src.model.usuario_model import Usuario

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

        botao_de_cadastrar = ft.Button(content=ft.Text("Cadastrar-se", weight="BOLD"),
                                       bgcolor="#fce51c", 
                                       color="#353535",
                                       width=250,
                                       height=40,
                                       on_click=self.cadastrar
                                       
                                       
                                      )

        botao_de_login = ft.Button(content=ft.Text("Fazer Login",weight="BOLD"),
                                   bgcolor="#fce51c", 
                                    color="#302F2F",
                                    width=250,
                                    height=40,
                                    
                                    )

        coluna_de_botoes = ft.Column(controls=[botao_de_cadastrar, botao_de_login],
                                     margin=50)

        # CONTROLS

        self.controls = [title,
                         coluna_de_campos,
                         coluna_de_botoes]
        
    def cadastrar(self):

        usuario = self.campo_login.value
        senha = self.campo_senha.value
        Usuario().cadastrar(usuario,senha)


   