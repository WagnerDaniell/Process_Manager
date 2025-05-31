import tkinter as tk
from tkinter import simpledialog, Toplevel, Text, messagebox

def show_result(title, lines):
    result_win = Toplevel(root)
    result_win.title(title)
    result_win.configure(bg="#f0f2f5")
    result_win.geometry("600x400")
    result_win.resizable(False, False)

    header = tk.Label(result_win, text=title, font=("Segoe UI", 18, "bold"), bg="#f0f2f5", fg="#2c3e50")
    header.pack(pady=(15, 5))

    frame = tk.Frame(result_win, bg="white", bd=2, relief="groove")
    frame.pack(padx=20, pady=10, fill="both", expand=True)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    text = Text(frame, width=60, height=20, wrap="word", yscrollcommand=scrollbar.set,
                bg="white", fg="#333", font=("Segoe UI", 12), bd=0, padx=10, pady=10)
    text.pack(fill="both", expand=True)
    scrollbar.config(command=text.yview)

    text.config(state='normal')

    spinners = ['|', '/', '-', '\\']

    def animar_spinner(base_text, frame_count, line_index):
        spinner_index = frame_count % len(spinners)

        if frame_count < 8:
            # Remove linha anterior e mostra nova animação
            text.delete("end-2l", "end-1l")
            text.insert(tk.END, f"{base_text} {spinners[spinner_index]}\n")
            text.see(tk.END)
            result_win.after(100, animar_spinner, base_text, frame_count + 1, line_index)
        else:
            # Exibe o resultado final
            text.delete("end-2l", "end-1l")
            text.insert(tk.END, f"{lines[line_index]}\n")
            result_win.after(300, mostrar_linhas, line_index + 1)

    def mostrar_linhas(index=0):
        if index < len(lines):
            nome_proc = lines[index].split(":")[0] if ":" in lines[index] else lines[index]
            base = f"Processando {nome_proc}"
            text.insert(tk.END, "\n")  # espaço para a animação
            animar_spinner(base, 0, index)
        else:
            text.config(state='disabled')

    mostrar_linhas()

def calcular_quantum_automatico(processos):
    tempos = [p[1] for p in processos]
    media = sum(tempos) / len(tempos)
    return max(1, round(media))

def rr_gui():
    processos = []
    quant = simpledialog.askinteger("RR", "Quantidade de processos:")
    if quant is None or quant <= 0:
        return

    for i in range(quant):
        nome = simpledialog.askstring("RR", f"Nome do processo {i + 1}:")
        if nome is None or nome.strip() == "":
            return
        tempo = simpledialog.askinteger("RR", f"Tempo de execução de {nome}:")
        if tempo is None or tempo <= 0:
            return
        processos.append([nome.strip(), tempo])

    # Perguntar se quer definir quantum manualmente ou automaticamente
    resposta = messagebox.askyesno("RR", "Deseja definir o quantum manualmente? (Não para calcular automaticamente)")
    
    if resposta:
        quantum = simpledialog.askinteger("RR", "Tempo quantum:")
        if quantum is None or quantum <= 0:
            return
    else:
        quantum = calcular_quantum_automatico(processos)
        messagebox.showinfo("RR", f"Quantum calculado: {quantum}")

    fila = processos.copy()
    tempo_total = 0
    resultado = ["----- ORDEM DE PROCESSO /RR/ -----"]
    resultado.append(f"Quantum utilizado: {quantum}")

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
    if quant is None or quant <= 0:
        return

    fila1, fila2, fila3 = [], [], []
    for i in range(quant):
        nome = simpledialog.askstring("MULTIFILA", f"Nome do processo {i+1}:")
        if nome is None or nome.strip() == "":
            return
        tempo = simpledialog.askinteger("MULTIFILA", f"Tempo de execução de {nome}:")
        if tempo is None or tempo <= 0:
            return
        prioridade = simpledialog.askinteger("MULTIFILA", f"Prioridade de {nome} (1 = mais prioritário):")
        if prioridade is None or prioridade <= 0:
            return

        if prioridade <= 2:
            fila1.append([nome.strip(), tempo])
        elif prioridade <= 4:
            fila2.append([nome.strip(), tempo])
        else:
            fila3.append([nome.strip(), tempo])

    # Perguntar se quer definir quantum manualmente ou automaticamente
    resposta = messagebox.askyesno("MULTIFILA", "Deseja definir o quantum manualmente? (Não para calcular automaticamente)")
    
    if resposta:
        quantum = simpledialog.askinteger("MULTIFILA", "Quantum para Round Robin:")
        if quantum is None or quantum <= 0:
            return
    else:
        quantum = calcular_quantum_automatico(fila1) if fila1 else 1
        messagebox.showinfo("MULTIFILA", f"Quantum calculado: {quantum}")

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

# ----- Restante do código original permanece igual -----
def fcfs_gui():
    processos = []
    quant = simpledialog.askinteger("FCFS", "Quantidade de processos:")
    if quant is None or quant <= 0:
        return

    for i in range(quant):
        nome = simpledialog.askstring("FCFS", f"Nome do processo {i + 1}:")
        if nome is None or nome.strip() == "":
            return
        processos.append(nome.strip())

    resultado = ["----- ORDEM DE PROCESSO /FCFS/ -----", "Obs: O 1° processo acima foi o primeiro a ser processado!"]
    for p in processos:
        resultado.append(p)
    show_result("FCFS", resultado)

def sjf_gui():
    processos = []
    quant = simpledialog.askinteger("SJF", "Quantidade de processos:")
    if quant is None or quant <= 0:
        return

    for i in range(quant):
        nome = simpledialog.askstring("SJF", f"Nome do processo {i + 1}:")
        if nome is None or nome.strip() == "":
            return
        tempo = simpledialog.askinteger("SJF", f"Tempo de execução de {nome}:")
        if tempo is None or tempo <= 0:
            return
        processos.append([nome.strip(), tempo])

    processos.sort(key=lambda x: x[1])
    resultado = ["----- ORDEM DE PROCESSO /SJF/ -----"]
    for p in processos:
        resultado.append(f"{p[0]} - {p[1]}")
    show_result("SJF", resultado)

def prioridade_gui():
    processos = []
    quant = simpledialog.askinteger("PRIORIDADE", "Quantidade de processos:")
    if quant is None or quant <= 0:
        return

    for i in range(quant):
        nome = simpledialog.askstring("PRIORIDADE", f"Nome do processo {i + 1}:")
        if nome is None or nome.strip() == "":
            return
        prioridade = simpledialog.askinteger("PRIORIDADE", f"Prioridade (menor = mais prioritário) de {nome}:")
        if prioridade is None or prioridade < 0:
            return
        processos.append([nome.strip(), prioridade])

    processos.sort(key=lambda x: x[1])
    resultado = ["----- ORDEM DE PROCESSO /PRIORIDADE/ -----"]
    for p in processos:
        resultado.append(f"{p[0]} - Prioridade {p[1]}")
    show_result("PRIORIDADE", resultado)

# ----- Interface principal -----
root = tk.Tk()
root.title("Simulador de Escalonamento de Processos")

label = tk.Label(root, text="Escolha um tipo de escalonamento:", font=("Arial", 14))
label.pack(pady=10)

tk.Button(root, text="FCFS", width=30, command=fcfs_gui).pack(pady=5)
tk.Button(root, text="SJF", width=30, command=sjf_gui).pack(pady=5)
tk.Button(root, text="Prioridade", width=30, command=prioridade_gui).pack(pady=5)
tk.Button(root, text="Round Robin (RR)", width=30, command=rr_gui).pack(pady=5)
tk.Button(root, text="Múltiplas Filas (Híbrido)", width=30, command=multipla_gui).pack(pady=5)
tk.Button(root, text="Sair", width=30, command=root.destroy).pack(pady=20)

root.mainloop()