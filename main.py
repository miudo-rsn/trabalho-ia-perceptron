#entradas (inputs)
input1 = 1.0
input2 = 0.5

#pesos (weights)
peso1 = 0.7
peso2 = 0.3

#bias (viés)
bias = -0.5

print("--- Dados Iniciais ---")
print(f"Entrada 1: {input1}")
print(f"Entrada 2: {input2}")
print(f"Peso 1: {peso1}")
print(f"Peso 2: {peso2}")
print(f"Bias: {bias}")
print("----------------------\n")



#Calcular a soma ponderada
# A fórmula é: (input1 * peso1) + (input2 * peso2)
soma_ponderada = (input1 * peso1) + (input2 * peso2)

print("--- Calculando ---")
print(f"Cálculo da soma: ({input1} * {peso1}) + ({input2} * {peso2})")
print(f"Resultado da soma ponderada: {soma_ponderada}\n")


#Adicionar o bias
soma_total = soma_ponderada + bias

print(f"Adicionando o bias: {soma_ponderada} + ({bias})")
print(f"Resultado final da soma: {soma_total}\n")


#Função de Ativação (A Decisão Final)
# Se o resultado final for positivo ou zero, o Perceptron "ativa" (saída 1).
# Se for negativo, ele "não ativa" (saída 0).
print("--- Tomando a Decisão ---")
print(f"O resultado final ({soma_total}) é maior ou igual a 0?")

# Variável para guardar o resultado final
resultado_final = 0

if soma_total >= 0:
    # Se a condição for verdadeira, a saída é 1
    resultado_final = 1
    print("Sim, é maior ou igual a 0. O Perceptron ativou!")
else:
    # Se a condição for falsa, a saída é 0
    resultado_final = 0
    print("Não, é menor que 0. O Perceptron não ativou.")

print("\n=========================")
print(f"SAÍDA DO PERCEPTRON: {resultado_final}")
print("=========================")

