import flet as ft

class Principal(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()
        self.pagina = pagina

        

    

        self.route = "/principal"
        self.bgcolor = "#2ed604"
        self.vertical_alignment="center"
        self.horizontal_alignment="center"

        # Textos

        bem_vindo = ft.Text(value="BEM VINDOS AO GODOY FINANÇAS 💚",
                            size=35,
                            weight="BOLD",
                            font_family="georgia",
                            color="#005504"
                                                 )

        textinho = ft.Text(value="Ficamos muito felizes em ter você aqui. Acreditamos que cuidar do seu dinheiro não precisa ser complicado nem estressante. Por isso, preparamos uma plataforma simples, intuitiva e feita sob medida para ajudar você a organizar suas despesas, ter clareza sobre seus gastos e conquistar a tranquilidade financeira que você merece. Explore à vontade, conecte sua rotina financeira conosco e dê o primeiro passo para realizar seus objetivos. Estamos ao seu lado em cada etapa dessa jornada!",
                           size=20,
                            weight="BOLD",
                            font_family="georgia",
                            color="#FFFFFF",
                            margin= 50)

        self.controls = [bem_vindo,
                         textinho]