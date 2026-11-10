import flet as ft
from src.view.cadastro_usuario_view import CadastroUsuarioView
from src.view.login_usuario_view import LoginUsuarioView
from src.view.cadastro_categoria_view import Home

def main(pagina:ft.Page):

    def navegacao(componente = None):
        item_clicado = componente.control.selected_index
        if item_clicado == 0:
            pagina.navigate('/categoria')
        elif item_clicado == 1:
            pagina.navigate('/')
        elif item_clicado == 2:
            pagina.navigate('/')
        elif item_clicado == 3:
            pagina.navigate('/')
        elif item_clicado == 4:
            pagina.navigate('/login')
    # Barra de navegação

    barra_navegacao_home = ft.NavigationBar(destinations=[ ft.NavigationBarDestination(icon=ft.Icons.CATEGORY_ROUNDED, 
                                        label="CATEGORIAS"),
            ft.NavigationBarDestination(icon=ft.Icons.ADD, 
                                                label="ADICIONAR DESPESAS"),
            ft.NavigationBarDestination(icon=ft.Icons.ALL_INBOX, 
                                                label="TODAS DESPESAS"),
            ft.NavigationBarDestination(icon=ft.Icons.INBOX_OUTLINED, 
                                                label="DESPESAS POR CATEGORIAS"),
            ft.NavigationBarDestination(icon=ft.Icons.EXIT_TO_APP, 
                                                label="SAIR",
                                                ),
                                                
                                                ],on_change=navegacao,
                                                bgcolor= "#f3aec5",
                                            
       
    )

    tela_cadastro_usuario = CadastroUsuarioView(pagina)
    tela_login_usuario = LoginUsuarioView(pagina)
    tela_home = Home(pagina)
    tela_home.navigation_bar = barra_navegacao_home

    def roteamento(e= None): 
        pagina.views.clear()
        

        if pagina.route == "/cadastro":
            pagina.views.append(tela_cadastro_usuario)
        elif pagina.route == "/login":
            pagina.views.append(tela_login_usuario)
        elif pagina.route == "/home":
            pagina.views.append(tela_home)

        pagina.update()
    
    pagina.on_route_change = roteamento
    roteamento()

    pagina.views.append(tela_login_usuario)


ft.run(main)