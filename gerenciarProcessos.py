def menu():
    print("----- MENU Gerenciador de Processos -----")
    print("Escolha um tipo de processo:")
    print("0. Sair")
    print("1. FCFS")
    print("2. SJF")
    print("3. PRIORIDADE")
    print("4. RR")
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


#Chama o menu para inicar o codigo
menu()

    
