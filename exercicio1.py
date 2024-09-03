import os

os.system("cls || clear") # limpa o terminal

class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento:str, cep: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

def __str__(self) -> str:
    return {
        f"\nLogradouro: {self.logradouro}"
        f"\nNumero: {self.numero}"
        f"\nComplemento: {self.complemento}"
        f"\nCEP: {self.cidade}"
            }

class Funcionario:
    def __init__(self, nome: str, telefone: str, email: str, endereco: str) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco