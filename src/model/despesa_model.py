from src.database.conexao import Conexao

class Despesa:
    def __init__(self):
        pass

    def incluir (login:str, descricao:str , valor:float, local:str,  id_categoria:int = None) -> int:
     
        conexao, cursor = Conexao().conectar()
                
        if conexao == None:
            print("Erro ao tentar criar despesa!")
            return None
        
        try:
            cursor.execute("""
                    INSERT INTO tb_despesas(login,  descricao, valor, local,id_categoria)
                    VALUES (%s, %s, %s, %s, %s);
                        """,
                [login, descricao, valor, local, id_categoria ])
        
            conexao.commit()
            conexao.close()
        
            return True
        except Exception as erro:
            print(f'ERRO AO INSERIR: {erro}')
            return False
        
    def recuperar (login:str) -> list:

        conexao, cursor = Conexao().conectar()
        
        if conexao == None:
            print("Erro ao tentar encontrar despesas!")
            return None
                
        cursor.execute("""
                        select login ,descricao, valor, local, id_categoria from tb_despesas
                        where login = %s;
        
                        """,
                    [login])
            
        resultado = cursor.fetchall() #fetchall : retorna mais de um valor
                    
        conexao.close()
        
        return resultado
    
    def recuperacao_especifica(login:int , id_categoria:int) -> list:

        conexao, cursor = Conexao().conectar()
        
        if conexao == None:
            print("Erro ao tentar encontrar despesas!")
            return None
                
        cursor.execute("""
                        select login ,descricao, valor, local, id_categoria from tb_despesas
                        where login = %s
                        and id_categoria = %s;
        
                        """,
                    [login])
            
        resultado = cursor.fetchall() #fetchall : retorna mais de um valor
                    
        conexao.close()
        
        return resultado  
    
    # def
        
