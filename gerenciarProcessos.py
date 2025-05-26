def menu():
    print("----- MENU Gerenciador de Processos -----")
    print("Escolha um tipo de processo:")
    print("0. Sair")
    print("1. FCFS")
    print("2. SJF")
    print("3. PRIORIDADE")
    print("4. RR")
    print("5. Múltiplas Filas (Híbrido)")

    option = int(input("Digite a opção desejada: "))

    if (option == 0):
        exit()
    elif (option == 1):
        fcfs()
    elif (option == 2):
        sjf()
    elif (option == 3):
        prioridade()
    elif (option == 4):
        rr()
    elif (option == 5):
        multipla_fila()


#FCFS o primeiro a chegar é o primeiro a sair

def fcfs():
    print("-----Modelo FCFS-----")
    quant_processo = int(input("Digite a quantidade de processos que serão criados: "))
    list_processos = []

    for i in range(quant_processo):
        processo = []
        nome_processo = str(input(f"Qual o nome do processo {i + 1}°: "))
        processo.append(nome_processo)
        list_processos.append(processo)

    print("----- ORDEM DE PROCESSO /FCFS/ -----")
    print("Obs: O 1° processo acima foi o primeiro a ser processado!")
    for x in range(len(list_processos)):
        print(list_processos[x])

    menu()

#SJF o que tem o tempo de execução mais curto e o primeiro a sair!

def sjf():
    print("-----Modelo SJF-----")
    quant_processo = int(input("Digite a quantidade de processos que serão criados: "))
    list_processos = []

    for i in range(quant_processo):
        processo = []
        nome_processo = str(input(f"Qual o nome do processo {i + 1}°: "))
        tempo_processo = int(input(f"Qual o tempo de serviço do processo {i + 1}°: "))
        processo.append(nome_processo)
        processo.append(tempo_processo)
        list_processos.append(processo)


    print("----- ORDEM DE PROCESSO /SJF/ -----")
    print("O 1° processo acima foi o primeiro a ser processado!")

    #infelizmente tive que me render a usar o .sort pq no hardcode ia ficar enorme
    list_processos.sort(key=lambda x: x[1]) 
    #mas resumindo ele ta usando o "lambda" que é uma função anonima a função ta pegando os valores do processo[1] é ordenando

    for x in range(len(list_processos)):
        print(list_processos[x])
                
    menu()

#PRIORIDADE a prioridade mais baixa é a primeira a sair!

def prioridade():
    print("-----Modelo PRIORIDADE-----")
    quant_processo = int(input("Digite a quantidade de processos que serão criados: "))
    list_processos = []

    for i in range(quant_processo):
        processo = []
        nome_processo = str(input(f"Qual o nome do processo {i + 1}°: "))
        prioridade_processo = int(input(f"Qual o tempo de serviço do processo {i + 1}°: "))
        processo.append(nome_processo)
        processo.append(prioridade_processo)
        list_processos.append(processo)

    print("----- ORDEM DE PROCESSO /PRIORIDADE/ -----")
    print("O 1° processo acima foi o primeiro a ser processado!")
    list_processos.sort(key=lambda x: x[1])
    for x in range(len(list_processos)):
        print(list_processos[x])

                
    menu()

#RR tempo media para executar o processo se o tempo para processar for menor que o tempo medio, vai processando de pedaço em pedaço até terminar

def rr():
    print("-----Modelo RR (Round Robin)-----")
    quant_processo = int(input("Digite a quantidade de processos que serão criados: "))
    list_processos = []
    quantum = int(input("Digite o tempo quantum para cada processo: "))

    for i in range(quant_processo):
        processo = []
        nome_processo = str(input(f"Qual o nome do processo {i + 1}°: "))
        tempo_processo = int(input(f"Qual o tempo de execução do processo {i + 1}°: "))
        processo.append(nome_processo)
        processo.append(tempo_processo)
        list_processos.append(processo)

    print("----- ORDEM DE PROCESSO /RR/ -----")

    tempo = 0
    fila = list_processos.copy()

    print

    while fila:
        processo = fila.pop(0) # 
        nome = processo[0]
        tempo_processo = processo[1]

        if tempo_processo > quantum:
            print(f"Tempo {tempo}: {nome} executando por {quantum}")
            tempo += quantum
            tempo_processo -= quantum
            fila.append([nome, tempo_processo])
        else:
            print(f"Tempo {tempo}: {nome} executando por {tempo_processo} (finalizado)")
            tempo += tempo_processo

    print("Todos os processos foram concluídos.")
    
    menu()
    
#Múltiplas Filas, usa várias filas de processos com diferentes níveis de prioridade
def multipla_fila():
    print("-----Modelo MÚLTIPLAS FILAS (HÍBRIDO)-----")
    quant_processo = int(input("Digite a quantidade de processos que serão criados: "))
    fila1 = []  # Round Robin (prioridade 1 a 2)
    fila2 = []  # SJF (prioridade 3 a 4)
    fila3 = []  # FCFS (prioridade 5+)

    for i in range(quant_processo):
        nome = str(input(f"Nome do processo {i+1}: "))
        tempo = int(input(f"Tempo de execução de {nome}: "))
        prioridade = int(input(f"Prioridade de {nome} (1 = mais prioritário): "))

        if prioridade <= 2:
            fila1.append([nome, tempo])
        elif prioridade <= 4:
            fila2.append([nome, tempo])
        else:
            fila3.append([nome, tempo])
    
    print("\n----- Executando Fila 1: Round Robin (prioridades 1-2) -----")
    quantum = int(input("Digite o quantum para Round Robin: "))
    tempo_total = 0
    fila = fila1.copy()
    while fila:
        processo = fila.pop(0)
        nome, tempo_exec = processo
        if tempo_exec > quantum:
            print(f"Tempo {tempo_total}: {nome} executa {quantum}")
            tempo_exec -= quantum
            tempo_total += quantum
            fila.append([nome, tempo_exec])
        else:
            print(f"Tempo {tempo_total}: {nome} executa {tempo_exec} (finalizado)")
            tempo_total += tempo_exec

    print("\n----- Executando Fila 2: SJF (prioridades 3-4) -----")
    fila2.sort(key=lambda x: x[1])
    for processo in fila2:
        nome, tempo_exec = processo
        print(f"Tempo {tempo_total}: {nome} executa {tempo_exec} (finalizado)")
        tempo_total += tempo_exec

    print("\n----- Executando Fila 3: FCFS (prioridades 5+) -----")
    for processo in fila3:
        nome, tempo_exec = processo
        print(f"Tempo {tempo_total}: {nome} executa {tempo_exec} (finalizado)")
        tempo_total += tempo_exec

    print("\nTodos os processos foram concluídos.\n")

    menu()
#Chama o menu para inicar o codigo
menu()

    
