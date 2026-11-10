import flet as ft
from src.view.cadastro_usuario_view import CadastroUsuarioView
from src.view.login_usuario_view import LoginUsuarioView
from src.view.cadastro_categoria_view import Home
from src.view.tela_home import Principal
from src.view.cadastro_despesa_view import Despesas
from src.view.despesas_por_categorias_view import DespesaPorCategoria
from src.view.todas_despesas_view import TodasDespesas
def main(pagina:ft.Page):

    def navegacao(componente = None):
        item_clicado = componente.control.selected_index
        if item_clicado == 0:
            pagina.navigate('/home')
        elif item_clicado == 1:
            pagina.navigate('/despesas')
        elif item_clicado == 2:
            pagina.navigate('/all_despesas')
        elif item_clicado == 3:
            pagina.navigate('/desp_por_cat')
        elif item_clicado == 4:
            pagina.navigate('/login')
            
    # Barras de navegações

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

    barra_navegacao_principal = ft.NavigationBar(destinations=[ ft.NavigationBarDestination(icon=ft.Icons.CATEGORY_ROUNDED, 
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
                                                    bgcolor= "#8de995",
                                                
           
        )

    barra_navegacao_add_despesa = ft.NavigationBar(destinations=[ ft.NavigationBarDestination(icon=ft.Icons.CATEGORY_ROUNDED, 
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
                                                        bgcolor= "#8000a0",
                                                    
               
            )

    barra_todas_desp = ft.NavigationBar(destinations=[ ft.NavigationBarDestination(icon=ft.Icons.CATEGORY_ROUNDED, 
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
                                                        bgcolor= "#EE0808",
                                                    
               
            )

    barra_despesa_por_cat = ft.NavigationBar(destinations=[ ft.NavigationBarDestination(icon=ft.Icons.CATEGORY_ROUNDED, 
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
                                                        bgcolor= "#E67E08",
                                                    
               
            )

    

    def roteamento(e= None): 
        pagina.views.clear()
        

        if pagina.route == "/cadastro":
            tela_cadastro_usuario = CadastroUsuarioView(pagina)
            pagina.navigate(tela_cadastro_usuario)
        elif pagina.route == "/login":
            tela_login_usuario = LoginUsuarioView(pagina)
            pagina.navigate(tela_login_usuario)
        elif pagina.route == "/home":
            tela_home = Home(pagina)
            tela_home.navigation_bar = barra_navegacao_home
            pagina.navigate(tela_home)
        elif pagina.route == "/principal":
            tela_principal = Principal(pagina)
            tela_principal.navigation_bar = barra_navegacao_principal
            pagina.navigate(tela_principal)
        elif pagina.route == "/despesas":
            tela_add_despesa = Despesas(pagina)
            tela_add_despesa.navigation_bar = barra_navegacao_add_despesa
            pagina.navigate(tela_add_despesa)
        elif pagina.route == "/desp_por_cat":
            tela_desp_p_cat = TodasDespesas(pagina)
            tela_desp_p_cat.navigation_bar = barra_despesa_por_cat
            pagina.navigate(tela_rec_despesas)
        elif pagina.route == "/all_despesas":
            tela_rec_despesas = DespesaPorCategoria(pagina)
            tela_rec_despesas.navigation_bar = barra_todas_desp
            pagina.navigate(tela_desp_p_cat)
        

        pagina.update()
    
    pagina.on_route_change = roteamento
    roteamento()

    pagina.views.append("/login")


ft.run(main)