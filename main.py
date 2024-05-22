menu = """

[d] Depositar 
[s] Sacar
[e] Extrato
[c] Cadastrar Usúario
[cc] Cadastrar Conta
[l] Listar
[lc] Listar Contas
[q] Sair

"""

saldo = 0
valor = 0
limite = 500
extrato = []
numero_de_saques = 0
usuarios = list()
contas = list()
LIMITE_DE_SAQUES = 3

def saque(*, numero_de_saques, saldo, extrato, limite_de_saques): 

    if numero_de_saques == limite_de_saques:
            
        print("Você atingiu seu limite de saques.\n")
    
    else:
        while True:
            valor = float(input("Digite o valor que deseja sacar\n"))

            if valor > 500:
                print("Só é possível sacar no maximo R$500,00. Por favor, escolha outro valor.\n")

            elif valor == 0:
                print("Não é possível sacar R$0,00. Escolha outro valor.\n")
            
            elif valor < 0:
                print("Não é possível sacar um valor negativo. Escolha outro valor.\n")
            
            elif valor > saldo:
                print("você não tem saldo suficiente.\n")
                
            else:
                saldo -= valor 
                numero_de_saques += 1 
                extrato.append(f"Valor sacado de R${valor}")  
                return saldo, extrato, numero_de_saques

def deposito(saldo, extrato, /): 
    while True:
        valor = float(input("Digite o valor que deseja inserir\n"))
        
        if valor < 0:
            print("O valor não pode ser negativo, digite outro valor.\n")
        
        elif valor == 0:
            print("Não tem como adicionar R$0,00. Por vaor, escolha outro valor.\n")

        else:
            saldo += valor
            extrato.append(f"Valor depositado de R${valor}")
            return saldo, extrato
   
def mostrar_extrato(saldo ,/, *, extrato):
    print(*extrato, sep="\n")
    print("saldo total:", saldo)

def criar_usuario():

    nome = input("Diga o nome do usuário: ")
    data_de_nascimento = input("Diga a sua data de nascimento[xx/xx/xxxx]: ")
    logradouro = input("Diga o seu logradouro: ")
    numero_da_casa = input("Diga o número da casa: ")
    bairro = input("Diga o bairro: ")
    cidade = input("Diga a cidade/sigla: ")
    cpf = input("Digite os números do cpf: ")
    if cpf.isnumeric():
        dicionario = {"Nome": nome, "Data de Nascimento": data_de_nascimento, "Logradouro": logradouro, "Numero": numero_da_casa, "Bairro": bairro, "Cidade": cidade}
        return dicionario, cpf 
    else:
        return print("CPF invalido.")

def criar_conta(contas, usuarios):
    agencia = "0001"
    numero_da_conta = len(contas)+1
    cpf = input("Diga seu cpf: ")
    usuario = usuarios[usuarios.index(cpf)+1] if cpf in usuarios else print("O usuario não existe")
    if usuario: 
         return agencia, numero_da_conta, cpf, usuario


def main():
    while True:
        escolha = input(menu)
        if escolha == "d":
            tupla_saldo_extrato = deposito(saldo, extrato)
            saldo, extrato = tupla_saldo_extrato[0], tupla_saldo_extrato[1]
            

        elif escolha == "s":
            tupla_saldo_extrato_numero_de_saques = saque(numero_de_saques=numero_de_saques, saldo=saldo, extrato=extrato, limite_de_saques=LIMITE_DE_SAQUES)
            saldo, extrato, numero_de_saques = tupla_saldo_extrato_numero_de_saques[0], tupla_saldo_extrato_numero_de_saques[1], tupla_saldo_extrato_numero_de_saques[2]
            

        
        elif escolha == "e":
            mostrar_extrato(saldo, extrato=extrato)
        

        elif escolha == "c":
            user, cpf = criar_usuario()
            if cpf not in usuarios:
                usuarios.append(cpf)
                usuarios.append(user)
            else:
                print("O usúario já existe.")
        
        elif escolha == "cc":
            agencia, numero_da_conta, cpf, usuario = criar_conta(contas, usuarios)
            contas.append(f"Agencia: {agencia}, Numero: {numero_da_conta}, CPF: {cpf}, Usúario: {usuario}")
        

        elif escolha == "l":
            print(usuarios)
        
        elif escolha == "lc":
            print(contas)
        
        elif escolha == "q":
            break 
        
        else:
            print("opção invalida, escolha novamente.")

main()