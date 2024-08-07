-- Criando a base de dados
CREATE DATABASE clientes;
USE clientes;

-- Criando tabelas USUARIO, ENDERECO E TELEFONE
CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
);

CREATE TABLE endereco (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    rua VARCHAR(50) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    estado VARCHAR(50) NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);

CREATE TABLE telefone (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    numero VARCHAR(255) NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);

-- Inserindo dados
INSERT INTO usuario (nome, email) VALUES 
('João Silva', 'joao@example.com'),
('Maria Oliveira', 'maria@example.com'),
('Pedro Santos', 'pedro@example.com'),
('Ana Costa', 'ana@example.com'),
('Lucas Almeida', 'lucas@example.com');

INSERT INTO endereco (usuario_id, rua, cidade, estado) VALUES
(1, 'Rua A', 'Cidade A', 'Estado A'),
(2, 'Rua B', 'Cidade B', 'Estado B'),
(3, 'Rua C', 'Cidade C', 'Estado C'),
(4, 'Rua D', 'Cidade D', 'Estado D'),
(5, 'Rua E', 'Cidade E', 'Estado E');

INSERT INTO telefone (usuario_id, numero) VALUES
(1, '1111-1111'),
(2, '2222-2222'),
(3, '3333-3333'),
(4, '4444-4444'),
(5, '5555-5555');