from src.database.conexao import Conexao

class Usuario:

    def __init__(self):
        pass

    @staticmethod    
    def cadastrar(login:str, senha:str) -> bool:

        conexao, cursor = Conexao().conectar()
        
        if conexao == None:
            print("Erro ao tentar conectar!")
            return False
        try:
            cursor.execute("""
                        INSERT INTO tb_usuarios(login, senha)
                        VALUES (%s, %s);
                        """,
                        [login, senha])

            conexao.commit()
            conexao.close()

            return True
        except Exception as erro:
            print(f'ERRO AO INSERIR: {erro}')
            return False 


    @staticmethod    
    def verificar(login:str, senha:str) -> dict:

        conexao, cursor = Conexao().conectar()

        if conexao == None:
                    print("Erro ao tentar conectar!")
                    return None
        
        cursor.execute("""
                       select id_usuario, login, senha from tb_usuarios
                        where login = %s
                        and senha = %s;

                       """,
                    [login, senha])
    
        resultado = cursor.fetchone()
            
        conexao.close()

        return resultado
            
        

        