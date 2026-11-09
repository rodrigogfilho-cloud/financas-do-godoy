import flet as ft
from src.model.usuario_model import Usuario


class CadastroUsuarioView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()
        self.pagina = pagina

        self.route = "/cadastro"

        self.bgcolor = "#b0e2ff"
        self.vertical_alignment="center"
        self.horizontal_alignment="center"

        title = ft.Text(value="CADASTRE SEU USUÁRIO",
                        size=35,
                        margin=50,
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

        botao_de_cadastrar = ft.Button(content=ft.Text("Cadastrar-se", weight="BOLD"),
                                       bgcolor="#379bdd", 
                                       color="#FFFFFF",
                                       width=250,
                                       height=40,
                                       on_click=self.cadastrar
                                       
                                       
                                      )

        botao_de_login = ft.Button(content=ft.Text("Fazer Login",weight="BOLD"),
                                   bgcolor="#379bdd", 
                                    color="#FFFEFE",
                                    width=250,
                                    height=40,
                                    on_click=self.ir_para_login
                                    
                                    )

        coluna_de_botoes = ft.Column(controls=[botao_de_cadastrar, botao_de_login],
                                     margin=20)

        # CONTROLS

        self.controls = [title,
                         coluna_de_campos,
                         coluna_de_botoes]
        
    def cadastrar(self):

        usuario = self.campo_login.value
        senha = self.campo_senha.value

        if usuario == "" or senha == "":
            self.pagina.show_dialog(ft.SnackBar(content=ft.Text(value="Preencha os campos",
                                                                            color="#FFFFFF",
                                                                             weight="BOLD", 
                                                                             text_align="center"),bgcolor="#fce51c",
                                                                             ))
            return

        # SNACKBAR MOSTRANDO QUE DEU CERTO
        if Usuario().cadastrar(usuario,senha):
            self.pagina.show_dialog(ft.SnackBar(content=ft.Text(value="Cadastrado efetuado com sucesso",
                                                                color="#FFFFFF",
                                                                 weight="BOLD", 
                                                                 text_align="center"),bgcolor="#158000",
                                                                 ))
        else: 
            self.pagina.show_dialog(ft.SnackBar(content=ft.Text(value="ERRO AO CADASTRAR",
                                                                color="#FFFFFF",
                                                                weight="BOLD",
                                                                text_align="center"), bgcolor="#fa5151"))
           
    async def ir_para_login(self):
        await self.pagina.push_route("/login")
