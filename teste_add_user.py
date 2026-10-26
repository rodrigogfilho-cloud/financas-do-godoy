from src.model.usuario_model import Usuario


id_usuario = Usuario().cadastrar("bolsonaro", "1")
print(id_usuario)