from src.database.conexao import Conexao

class Categoria:
    def __init__(self):
        pass

    def adicionar (categoria:str, id_usuario:int) -> int:

        conexao, cursor = Conexao().conectar()
                
        if conexao == None:
            print("Erro ao tentar conectar!")
            return None

        try:
            cursor.execute("""
                    INSERT INTO tb_categorias(tipo, id_usuario)
                    VALUES (%s, %s);
                        """,
                [categoria, id_usuario])
        
            conexao.commit()
            last_id= cursor.lastrowid() # Ultimo id cadastrado nas categorias
            conexao.close()
        
            return last_id
        except Exception as erro:
            print(f'ERRO AO INSERIR: {erro}')
            return None


    def recuperar(login:str) -> list:

        conexao, cursor = Conexao().conectar()
        
        if conexao == None:
            print("Erro ao tentar conectar!")
            return None
                
        cursor.execute("""
                        select tipo, id_categoria from tb_categorias
                        where tipo = %s;
        
                        """,
                    [login])
            
        resultado = cursor.fetchall() #fetchall : retorna mais de um valor
                    
        conexao.close()
        
        return resultado

    def excluir (id_categoria:int) -> bool:

        conexao, cursor = Conexao().conectar()

        if conexao == None: # None = NADA
            print("Erro ao tentar conectar!")
            return None
        try:                
            cursor.execute("""
                        DELETE FROM tb_categorias 
                        WHERE id_categoria = %s;
                            ;
                
                        """,
                        [id_categoria])
                
            conexao.commit()
                            
            conexao.close()
                
            return True         #Retorna um True ou False , True : a tabela foi excluída com sucesso, já False: é o oposto
        except Exception as e:
            print(f'ERRO AO INSERIR: {e}')
            return False