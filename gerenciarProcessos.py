import tkinter as tk
from tkinter import simpledialog, messagebox

# Função auxiliar para mostrar resultado
def show_result(title, lines):
    result_win = tk.Toplevel(root)
    result_win.title(title)
    text = tk.Text(result_win, width=60, height=20)
    text.pack(padx=10, pady=10)
    for line in lines:
        text.insert(tk.END, line + '\n')
    text.config(state='disabled')


def fcfs_gui():
    processos = []
    #cria uma janela de diálogo para solicitar a quantidade de processos
    quant = simpledialog.askinteger("FCFS", "Quantidade de processos:")
    if not quant: return

    for i in range(quant):
        nome = simpledialog.askstring("FCFS", f"Nome do processo {i + 1}:")
        processos.append(nome)

    resultado = ["----- ORDEM DE PROCESSO /FCFS/ -----", "Obs: O 1° processo acima foi o primeiro a ser processado!"]
    for p in processos:
        resultado.append(p)
    show_result("FCFS", resultado)


def sjf_gui():
    processos = []
    quant = simpledialog.askinteger("SJF", "Quantidade de processos:")
    if not quant: return

    for i in range(quant):
        nome = simpledialog.askstring("SJF", f"Nome do processo {i + 1}:")
        tempo = simpledialog.askinteger("SJF", f"Tempo de execução de {nome}:")
        processos.append([nome, tempo])

    processos.sort(key=lambda x: x[1])
    resultado = ["----- ORDEM DE PROCESSO /SJF/ -----"]
    for p in processos:
        resultado.append(f"{p[0]} - {p[1]}")
    show_result("SJF", resultado)


def prioridade_gui():
    processos = []
    quant = simpledialog.askinteger("PRIORIDADE", "Quantidade de processos:")
    if not quant: return

    for i in range(quant):
        nome = simpledialog.askstring("PRIORIDADE", f"Nome do processo {i + 1}:")
        prioridade = simpledialog.askinteger("PRIORIDADE", f"Prioridade (menor = mais prioritário) de {nome}:")
        processos.append([nome, prioridade])

    processos.sort(key=lambda x: x[1])
    resultado = ["----- ORDEM DE PROCESSO /PRIORIDADE/ -----"]
    for p in processos:
        resultado.append(f"{p[0]} - Prioridade {p[1]}")
    show_result("PRIORIDADE", resultado)


def rr_gui():
    processos = []
    quant = simpledialog.askinteger("RR", "Quantidade de processos:")
    if not quant: return
    quantum = simpledialog.askinteger("RR", "Tempo quantum:")
    if not quantum: return

    for i in range(quant):
        nome = simpledialog.askstring("RR", f"Nome do processo {i + 1}:")
        tempo = simpledialog.askinteger("RR", f"Tempo de execução de {nome}:")
        processos.append([nome, tempo])

    fila = processos.copy()
    tempo_total = 0
    resultado = ["----- ORDEM DE PROCESSO /RR/ -----"]

    while fila:
        nome, tempo = fila.pop(0)
        if tempo > quantum:
            resultado.append(f"Tempo {tempo_total}: {nome} executa {quantum}")
            fila.append([nome, tempo - quantum])
            tempo_total += quantum
        else:
            resultado.append(f"Tempo {tempo_total}: {nome} executa {tempo} (finalizado)")
            tempo_total += tempo

    show_result("RR", resultado)


def multipla_gui():
    quant = simpledialog.askinteger("MULTIFILA", "Quantidade de processos:")
    if not quant: return

    fila1, fila2, fila3 = [], [], []
    for i in range(quant):
        nome = simpledialog.askstring("MULTIFILA", f"Nome do processo {i+1}:")
        tempo = simpledialog.askinteger("MULTIFILA", f"Tempo de execução de {nome}:")
        prioridade = simpledialog.askinteger("MULTIFILA", f"Prioridade de {nome} (1 = mais prioritário):")
        if prioridade <= 2:
            fila1.append([nome, tempo])
        elif prioridade <= 4:
            fila2.append([nome, tempo])
        else:
            fila3.append([nome, tempo])

    quantum = simpledialog.askinteger("MULTIFILA", "Quantum para Round Robin:")
    tempo_total = 0
    resultado = []

    resultado.append("----- Fila 1 (Round Robin) -----")
    fila = fila1.copy()
    while fila:
        nome, tempo_exec = fila.pop(0)
        if tempo_exec > quantum:
            resultado.append(f"Tempo {tempo_total}: {nome} executa {quantum}")
            fila.append([nome, tempo_exec - quantum])
            tempo_total += quantum
        else:
            resultado.append(f"Tempo {tempo_total}: {nome} executa {tempo_exec} (finalizado)")
            tempo_total += tempo_exec

    resultado.append("----- Fila 2 (SJF) -----")
    fila2.sort(key=lambda x: x[1])
    for nome, tempo_exec in fila2:
        resultado.append(f"Tempo {tempo_total}: {nome} executa {tempo_exec} (finalizado)")
        tempo_total += tempo_exec

    resultado.append("----- Fila 3 (FCFS) -----")
    for nome, tempo_exec in fila3:
        resultado.append(f"Tempo {tempo_total}: {nome} executa {tempo_exec} (finalizado)")
        tempo_total += tempo_exec

    show_result("Múltiplas Filas", resultado)


# ----- Interface principal -----
#iniciando a janela raiz do Tkinter
root = tk.Tk()
# Definindo o titulo da janela
root.title("Simulador de Processos")

# definindo label titulo da janela
label = tk.Label(root, text="Escolha um algoritmo de escalonamento:", font=("Arial", 14))
label.pack(pady=10)

tk.Button(root, text="FCFS", width=30, command=fcfs_gui).pack(pady=5)
tk.Button(root, text="SJF", width=30, command=sjf_gui).pack(pady=5)
tk.Button(root, text="Prioridade", width=30, command=prioridade_gui).pack(pady=5)
tk.Button(root, text="Round Robin (RR)", width=30, command=rr_gui).pack(pady=5)
tk.Button(root, text="Múltiplas Filas (Híbrido)", width=30, command=multipla_gui).pack(pady=5)
tk.Button(root, text="Sair", width=30, command=root.destroy).pack(pady=20)

root.mainloop()
