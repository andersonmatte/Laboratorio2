from src import Cliente
from src import Conta

#Inicializa Objeto Cliente
Cliente.nome = 'Anderrson Matte Tamborim'
Cliente.telefone = 51985755987

#Inicializa Objeto Conta
Conta.cliente = Cliente
Conta.numero = "0001-1"
Conta.saldo = 0
Conta.limite = 900

#Operação Extrato completo da Conta Corrente
def extratoCompleto():
 print("------Extrato------")
 print('Conta: ', Conta.numero + '\n')
 print ("Deposito: "), Conta.saldo
 print ("Saque: "), 0
 print ("Saldo: "), Conta.saldo
 print ("Limite: "), Conta.limite
 print ("Disponivel: "), Conta.saldo + Conta.limite