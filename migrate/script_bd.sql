CREATE DATABASE IF NOT EXISTS godoy_financas;

USE godoy_financas;

CREATE TABLE IF NOT EXISTS tb_usuarios (
 id_usuario INT PRIMARY KEY auto_increment,
 login VARCHAR(100) NOT NULL,
 senha VARCHAR(255)
);


CREATE TABLE IF NOT EXISTS tb_categorias (
 id_categoria INT PRIMARY KEY auto_increment,
 tipo VARCHAR(100),
 id_usuario INT NOT NULL
);


CREATE TABLE IF NOT EXISTS tb_despesas (
 id_despesa INT PRIMARY KEY auto_increment,
 descricao VARCHAR(255),
 id_usuario INT NOT NULL,
 valor FLOAT(10),
 data DATE,
 hora TIME(6),
 id_categoria INT
);



ALTER TABLE tb_categorias ADD CONSTRAINT FK_tb_categorias_0 FOREIGN KEY (id_usuario) REFERENCES tb_usuarios (id_usuario);
ALTER TABLE tb_despesas ADD CONSTRAINT FK_tb_despesas_0 FOREIGN KEY (id_usuario) REFERENCES tb_usuarios (id_usuario);
ALTER TABLE tb_despesas ADD CONSTRAINT FK_tb_despesas_1 FOREIGN KEY (id_categoria) REFERENCES tb_categorias (id_categoria);