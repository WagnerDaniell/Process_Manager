import tkinter as tk
from tkinter import simpledialog, Toplevel, Text, messagebox

#Mostrar os resultados personalizado!

#esse frame resumidamente são uma div kk
def show_result(title, lines):
    result_win = Toplevel(root)
    result_win.title(title)
    result_win.configure(bg="#f0f2f5")
    result_win.geometry("700x500")
    
    main_frame = tk.Frame(result_win, bg="#f0f2f5")
    main_frame.pack(fill='both', expand=True, padx=20, pady=20)
    
    header = tk.Label(main_frame, 
                     text=title, 
                     font=("Segoe UI", 18, "bold"), 
                     bg="#f0f2f5", 
                     fg="#2c3e50")
    header.pack(pady=(0, 15))
    
    content_frame = tk.Frame(main_frame, 
                           bg="white", 
                           bd=1, 
                           relief="solid")
    content_frame.pack(fill='both', expand=True)
    
    text_frame = tk.Frame(content_frame, bg="white")
    text_frame.pack(fill='both', expand=True, padx=5, pady=5)
    
    scrollbar = tk.Scrollbar(text_frame)
    scrollbar.pack(side='right', fill='y')
    
    text = Text(text_frame, 
               width=80, 
               height=25, 
               wrap='word', 
               yscrollcommand=scrollbar.set,
               bg='white', 
               fg="#34495e", 
               font=("Consolas", 10),
               bd=0, 
               padx=10, 
               pady=10)
    text.pack(fill='both', expand=True)
    scrollbar.config(command=text.yview)
    
    text.config(state='normal')
    
    # spinner
    spinners = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    
    def animar_spinner(base_text, frame_count, line_index):
        spinner_index = frame_count % len(spinners)
        
        if frame_count < 10:
            text.delete("end-2l", "end-1l")
            text.insert(tk.END, f"{spinners[spinner_index]} {base_text}\n")
            text.see(tk.END)
            text.tag_add('spinner', 'end-2l linestart', 'end-2l lineend')
            text.tag_config('spinner', foreground="#3498db")
            result_win.after(80, animar_spinner, base_text, frame_count + 1, line_index)
        else:
            text.delete("end-2l", "end-1l")
            text.insert(tk.END, f"✓ {lines[line_index]}\n")
            text.tag_add('done', 'end-2l linestart', 'end-2l lineend')
            text.tag_config('done', foreground="#2ecc71")
            result_win.after(200, mostrar_linhas, line_index + 1)
    
    def mostrar_linhas(index=0):
        if index < len(lines):
            nome_proc = lines[index].split(":")[0] if ":" in lines[index] else lines[index]
            base = f"Processando {nome_proc}" if "-----" not in lines[index] else lines[index]
            
            if "-----" in lines[index]:
                text.insert(tk.END, f"\n{lines[index]}\n")
                text.tag_add('header', 'end-2l linestart', 'end-2l lineend')
                text.tag_config('header', 
                              foreground="#2c3e50", 
                              font=("Segoe UI", 11, "bold"))
                result_win.after(100, mostrar_linhas, index + 1)
            else:
                text.insert(tk.END, "\n")
                animar_spinner(base, 0, index)
        else:
            text.config(state='disabled')
            # processamento concluido
            text.insert(tk.END, "\n\nProcessamento concluído ✓", 'footer')
            text.tag_config('footer', 
                          foreground="#2ecc71", 
                          font=("Segoe UI", 10, "bold"),
                          justify='center')
    
    mostrar_linhas()

def calcular_quantum_automatico(processos):
    tempos = [p[1] for p in processos]
    media = sum(tempos) / len(tempos)
    return max(1, round(media))

def rr_gui():
    processos = []
    quant = simpledialog.askinteger("RR", "Quantidade de processos:")
    if quant is None or quant <= 0:
        return #Fecha a caixinha

    for i in range(quant):
        nome = simpledialog.askstring("RR", f"Nome do processo {i + 1}:")
        if nome is None or nome.strip() == "":
            return
        tempo = simpledialog.askinteger("RR", f"Tempo de execução de {nome}:")
        if tempo is None or tempo <= 0:
            return
        processos.append([nome.strip(), tempo])

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
    resultado = ["----- ORDEM DE PROCESSO /RR/ -----",
                f"Quantum utilizado: {quantum}",
                "--------------------------------"]

    while fila:
        nome, tempo = fila.pop(0)
        if tempo > quantum:
            resultado.append(f"🔄 Tempo {tempo_total}: {nome} executa {quantum} (restam {tempo-quantum})")
            fila.append([nome, tempo - quantum])
            tempo_total += quantum
        else:
            resultado.append(f"✅ Tempo {tempo_total}: {nome} executa {tempo} (finalizado)")
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

    resposta = messagebox.askyesno("MULTIFILA", "Deseja definir o quantum manualmente? (Não para calcular automaticamente)")
    
    if resposta:
        quantum = simpledialog.askinteger("MULTIFILA", "Quantum para Round Robin:")
        if quantum is None or quantum <= 0:
            return
    else:
        quantum = calcular_quantum_automatico(fila1) if fila1 else 1
        messagebox.showinfo("MULTIFILA", f"Quantum calculado: {quantum}")

    tempo_total = 0
    resultado = ["----- MÚLTIPLAS FILAS -----",
                f"Quantum Fila 1: {quantum}",
                "--------------------------"]

    resultado.append("\n⭐ FILA 1 - ROUND ROBIN")
    fila = fila1.copy()
    while fila:
        nome, tempo_exec = fila.pop(0)
        if tempo_exec > quantum:
            resultado.append(f"🔄 Tempo {tempo_total}: {nome} executa {quantum} (restam {tempo_exec-quantum})")
            fila.append([nome, tempo_exec - quantum])
            tempo_total += quantum
        else:
            resultado.append(f"✅ Tempo {tempo_total}: {nome} executa {tempo_exec} (finalizado)")
            tempo_total += tempo_exec

    resultado.append("\n🔹 FILA 2 - SJF")
    fila2.sort(key=lambda x: x[1])
    for nome, tempo_exec in fila2:
        resultado.append(f"✅ Tempo {tempo_total}: {nome} executa {tempo_exec} (finalizado)")
        tempo_total += tempo_exec

    resultado.append("\n📌 FILA 3 - FCFS")
    for nome, tempo_exec in fila3:
        resultado.append(f"✅ Tempo {tempo_total}: {nome} executa {tempo_exec} (finalizado)")
        tempo_total += tempo_exec

    show_result("Múltiplas Filas", resultado)


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

    resultado = ["----- ORDEM DE PROCESSO /FCFS/ -----", 
                "Obs: O 1° processo acima foi o primeiro a ser processado!"]
    resultado.extend(processos)
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

# menu
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