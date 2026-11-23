import flet as ft
from src.model.categoria_model import Categoria


class Home(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()
        self.pagina = pagina

        dados_usuario = pagina.session.store.get("usuario_logado")
                
        self.id_usuario = dados_usuario.get("id_usuario")

        # Lista 
        
        self.lista_categorias = []

        self.route = "/home"
        self.bgcolor = "#eb9feb"
        self.vertical_alignment="center"
        self.horizontal_alignment="center"

        

        # Textos

     

        self.title = ft.Text(value="CADASTRE SUAS CATEGORIAS",
                        size=35,
                        margin=5,
                        weight="BOLD",
                         font_family="georgia",
                         color="#fa1fca"
                     
                        )

       

        

        self.texto_de_nao_cadastrar_categoria = ft.Text(value="Não deseja cadastrar uma categoria?",
                                                   weight="BOLD",
                                                    bgcolor="transparent",
                                                    color="#302F2F",
                                                   )

        self.textinho_id = ft.Text(value=f"Seu ID Usuário é : {self.id_usuario}. ",
                                           size=20,
                                            weight="BOLD",
                                            font_family="georgia",
                                            color="#FFFFFF",
                                            margin= 10,
                                            )

        self.title_historico = ft.Text(value="Categorias Registradas:",
                                           size=20,
                                            weight="BOLD",
                                            font_family="georgia",
                                            color="#FFFFFF",
                                           )

        # CAMPOS

      

        self.campo_adicionar_categoria = ft.TextField(label='Categoria',
                                    value='',
                                   bgcolor="#fdfdfdff", 
                                    color="#000000",
                                )

        self.campo_excluir_categoria = ft.TextField(label='Categoria que deseja excluir',
                                    value='',
                                   bgcolor="#fdfdfdff", 
                                    color="#000000",
                                )

        

       
        # BOTÕES

        botao_add = ft.FloatingActionButton(icon=ft.Icons.ADD,
                                            bgcolor="#E765DC",
                                           hover_color="#C202B8",
                                            width=50,
                                            height=50,
                                            on_click=self.adicionar,)

        

        

        botao_nao_cadastrar = ft.Button(content=ft.Text(value='Pular etapa', weight="BOLD"),
                                        bgcolor="transparent", 
                                        elevation=0,
                                        color="#030303",
                                        height=40,
                                        on_click=self.ir_para_despesas)

        # Linhas e colunas

        self.coluna_add = ft.Row(controls=[self.campo_adicionar_categoria, botao_add],alignment="center",
                               )

        # Histórico

        coluna_lista_categorias= ft.Column(controls=self.lista_categorias,
                                           alignment="center",
                                           height=540,
                                           scroll=ft.ScrollMode.ADAPTIVE)

      
        # Linha para pular etapa

        self.linha_pular_etapa =ft.Row(controls=[self.texto_de_nao_cadastrar_categoria, botao_nao_cadastrar],alignment="center")

        # 

        self.atualizar_lista_categorias()

        self.controls = [
           
            self.title,
            self.textinho_id,
           self.coluna_add,self.title_historico,coluna_lista_categorias,
            self.linha_pular_etapa,
        ]

        # DEF´S

        # Criação da def para ir para despesas, fazer isso depois > Feito

    async def ir_para_despesas (self):
            await self.pagina.push_route("/despesas")

    def adicionar (self):

           
            categoria = self.campo_adicionar_categoria.value
            
           

            if categoria == "":
                self.pagina.show_dialog(ft.SnackBar(content=ft.Text(value="Preencha os campos",
                               color="#FFFFFF",
                               weight="BOLD", 
                               text_align="center"),bgcolor="#fce51c",
                                   ))

                
                return


            if Categoria().adicionar(categoria,self.id_usuario):
                self.pagina.show_dialog(ft.SnackBar(content=ft.Text(value="CATEGORIA CRIADA 👍",
                                                                                                      color="#FFFFFF",
                                                                                                      weight="BOLD", 
                                                                                                      text_align="center"),bgcolor="#158000",
                                                                                                          ))
                self.pagina.update()
                self.lista_categorias.clear()

                                                                                                          
            self.atualizar_lista_categorias()


    def atualizar_lista_categorias(self):
        categorias = Categoria().recuperar(self.id_usuario)

        for categoria in categorias:
            nome_categoria = categoria.get("tipo")
            texto = ft.Text(value=nome_categoria)
            id_categoria = categoria.get('id_categoria')
            botao_delete = ft.FloatingActionButton(icon=ft.Icons.DELETE,
                                                                    bgcolor="#E765DC",
                                                                   hover_color="#C202B8",
                                                                    width=50,
                                                                    height=50,
                                                                    on_click=lambda e, id_cat=id_categoria: self.excluir_categoria(id_cat), key=id_categoria, # o key é uma variavel para o pegar o id_categoria, para quando eu for excluir, excluir a categoria que desejo excluir
                                            tooltip='Excluir Categoria'
                                                                    )
            linha = ft.Row(controls=[texto,botao_delete],
                           alignment="CENTER",
                         )
            
            
            self.lista_categorias.append(linha)

            

        self.pagina.update()




    def excluir_categoria(self,excluir): # O parâmetro excluir serve para receber o identificador (ID) da categoria que você deseja apagar.
        Categoria().excluir(id_categoria=excluir) #Excluo a categoria
        self.lista_categorias.clear() # Limpo lista
        self.atualizar_lista_categorias() # E chamo/atualizo a lista para chamar ela sem a categoria que eu removi
            