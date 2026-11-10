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

        title = ft.Text(value="ENTRE AGORA !!!",
                        size=35,
                        margin=30,
                        weight="BOLD",
                         font_family="georgia"
                     
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

        botao_login = ft.Button(content=ft.Text("Entrar",weight="BOLD"),
                                   bgcolor="#fce51c", 
                                   elevation=0,
                                    color="#302F2F",
                                    height=40,
                                    width=200,
                                    margin=10,
                                    on_click=self.fazer_login
                                    
                                    )

        txt_cadastro = ft.Text(value="Não tem uma conta?",
                            weight="BOLD",
                            bgcolor="transparent",
                            color="#302F2F")
        
        botao_para_cadastrar = ft.Button(content=ft.Text("Cadastre-se",weight="BOLD"),
                                   bgcolor="transparent", 
                                   elevation=0,
                                    color="#302F2F",
                                    height=40,
                                    on_click=self.ir_para_cadastro
                                    
                                 
                                                                        )

        linha_botoes = ft.Row(controls=[txt_cadastro, botao_para_cadastrar],
                              alignment="center",
                              margin=10)

        # CONTROLS
        
        self.controls = [title,
        coluna_de_campos,
            botao_login,
            linha_botoes]

       

        # DEF´s
   

    async def ir_para_cadastro (self):
            await self.pagina.push_route("/cadastro")

    async def fazer_login(self):
                

                usuario = self.campo_login.value
                senha = self.campo_senha.value
                            
                if usuario == "" or senha == "":
                    self.pagina.show_dialog(ft.SnackBar(content=ft.Text(value="Preencha os campos",
                    color="#FFFFFF",
                    weight="BOLD", 
                    text_align="center"),bgcolor="#fce51c",
                        ))
                    return

                resultado = Usuario().verificar(usuario,senha)

                if resultado:
                      self.campo_login.value = ""
                      self.campo_senha.value = ""
                      self.pagina.session.store.set("usuario_logado",resultado)
                      await self.pagina.push_route("/principal")

                else:
                    self.campo_login.value = ""
                    self.campo_senha.value = ""
                    self.pagina.show_dialog(ft.SnackBar(content=ft.Text(value="LOGIN OU SENHA INCORRETO",
                                          color="#FFFFFF",
                                          weight="BOLD", 
                                          text_align="center"),bgcolor="#d41e1e",
                                              ))
