agendamentos = []

def mostrar_agendamentos(lista):
    contador = 1
    for agendamento in lista:
        print(str(contador) + " - " + agendamento["nome"] + " - " + agendamento["servico"] + " - " + agendamento["horario"])
        contador = contador + 1

while True:
    nome = input("digite o nome ou sair")
    if nome == "sair":
        break
    servico = input("digite o sevico")
    horario = input("digite o horario")

novo_cliente = {"nome": nome, "servico": servico, "horario": horario}
agendamentos.append(novo_cliente)

mostrar_agendamentos(agendamentos)
       