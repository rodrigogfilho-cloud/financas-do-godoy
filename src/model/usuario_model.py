from src.database.conexao import Conexao

class Usuario:

    def __init__(self):
        pass

    @staticmethod    
    def cadastrar(login:str, senha:str) -> bool:
        try:
            conexao, cursor = Conexao().conectar()
            cursor.execute("""
                            INSERT INTO tb_usuarios(login, senha)
                            VALUES (%s, %s);
                            """,
                            [login, senha])

            conexao.commit()
            conexao.close()

            return True 
        except Exception as erro:
            print(f"ERRO: {erro}")
            return None, None

