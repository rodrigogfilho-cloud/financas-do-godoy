from src.database.conexao import Conexao

class Despesa:
    def __init__(self):
        pass
    @staticmethod
    def incluir (login:int, descricao:str , valor:float,   id_categoria:int = None) -> int:
     
        conexao, cursor = Conexao().conectar()
                
        if conexao == None:
            print("Erro ao tentar criar despesa!")
            return None
        
        try:
            cursor.execute("""
                    INSERT INTO tb_despesas(id_usuario, descricao, valor ,id_categoria)
                    VALUES (%s, %s, %s, %s);
                        """,
                [login, descricao, valor, id_categoria ])
        
            conexao.commit()
            conexao.close()
        
            return True
        except Exception as erro:
            print(f'ERRO AO INSERIR: {erro}')
            return False
    @staticmethod    
    def recuperar (login:int) -> list:

        conexao, cursor = Conexao().conectar()
        
        if conexao == None:
            print("Erro ao tentar encontrar despesas!")
            return None
        try:        
            cursor.execute("""
                            select id_despesa, descricao, valor, data, hora, id_categoria from tb_despesas
                            where id_usuario = %s
            
                            """,
                        [login])
                
            resultado = cursor.fetchall() #fetchall : retorna mais de um valor
                        
            conexao.close()
            
            return resultado
        except Exception as e:
            print(f'ERRO AO INSERIR: {e}')
            return None
    @staticmethod
    def recuperacao_especifica(login:int , id_categoria:int) -> list:

        conexao, cursor = Conexao().conectar()
        
        if conexao == None:
            print("Erro ao tentar encontrar despesas!")
            return None
        try:        
            cursor.execute("""
                            select id_despesa ,descricao, id_usuario, valor, data, hora, id_categoria from tb_despesas
                            where id_usuario = %s
                            and id_categoria = %s;
            
                            """,
                        [login, id_categoria])
                
            resultado = cursor.fetchall() #fetchall : retorna mais de um valor
                        
            conexao.close()
            
            return resultado 
        except Exception as e:
            print(f'ERRO AO INSERIR: {e}')
            return None
    @staticmethod
    def excluir(id_despesa:int) -> bool:
    
        conexao, cursor = Conexao().conectar()

        if conexao == None: # None = NADA
            print("Erro ao tentar excluir!")
            return False
        try:                
            cursor.execute("""
                        DELETE FROM tb_despesas 
                        WHERE id_despesa = %s;
                            ;
                
                        """,
                        [id_despesa])
                
            conexao.commit()  
            conexao.close()
                
            return True         #Retorna um True ou False , True : a tabela foi excluída com sucesso, já False: é o oposto
        except Exception as e:
            print(f'ERRO AO INSERIR: {e}')
            return False
        
    @staticmethod
    def alterar (login:int, id_despesa:int, id_categoria:int, descricao:str, valor:float, data:str) -> bool    :

        conexao, cursor = Conexao().conectar()

        if conexao == None: # None = NADA
            print("Erro ao tentar alterar!")
            return False
        try:                
            cursor.execute("""
                        UPDATE tb_despesas 
                        SET id_categoria = %s, descricao = %s, valor = %s, data = %s
                        WHERE id_despesa = %s AND id_usuario = %s
                            
                
                        """,
                        [id_categoria, descricao, valor, data, id_despesa, login])
                
            conexao.commit()  
            conexao.close()
                
            return True         #Retorna um True ou False , True : a tabela foi excluída com sucesso, já False: é o oposto
        except Exception as e:
            print(f'ERRO AO INSERIR: {e}')
            return False
    
        
