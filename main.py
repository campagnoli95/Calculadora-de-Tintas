import tkinter as tk
from tkinter import ttk

def calcular_tinta():
    """Calcula a quantidade de tinta necessária para pintar uma parede."""
    try:
        # Captura os valores inseridos pelo usuário
        nome_cliente = nome_cliente_entry.get()
        largura_parede = float(largura_parede_entry.get())
        altura_parede = float(altura_parede_entry.get())

        # Valida as entradas
        if largura_parede <= 0 or altura_parede <= 0:
            raise ValueError("Largura e altura devem ser maiores que zero.")

        # Calcula a área da parede e a quantidade de tinta necessária
        area_parede = largura_parede * altura_parede
        litros_tinta = area_parede / 2  # 1 litro de tinta cobre 2m²

        # Exibe o resultado
        resultado_label.config(text=f"Cliente: {nome_cliente}\n"
                                   f"Área da parede: {area_parede:.2f} m²\n"
                                   f"Quantidade de tinta necessária: {litros_tinta:.2f} litros")

    except ValueError as e:
        resultado_label.config(text=f"Erro: {e}")

# Cria a janela principal
root = tk.Tk()
root.title("Calculadora de Tinta")
root.configure(bg="#FFEB3B")
# Labels e entradas para nome, largura e altura
ttk.Label(root, text="Nome do Cliente:", background="#FFEB3B", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
nome_cliente_entry = ttk.Entry(root, font=("Helvetica", 12))
nome_cliente_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

ttk.Label(root, text="Largura da Parede (m):", background="#FFEB3B", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
largura_parede_entry = ttk.Entry(root, font=("Helvetica", 12))
largura_parede_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

ttk.Label(root, text="Altura da Parede (m):", background="#FFEB3B", font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
altura_parede_entry = ttk.Entry(root, font=("Helvetica", 12))
altura_parede_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

# Botão de calcular
calcular_button = ttk.Button(root, text="Calcular", command=calcular_tinta)
calcular_button.grid(row=3, column=0, columnspan=2, padx=10, pady=20)
calcular_button.configure(style="TButton")

# Estilo para o botão
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12, "bold"), background="#4CAF50", foreground="black")  # Verde vibrante com texto branco

# Label para exibir o resultado
resultado_label = ttk.Label(root, text="", background="#FFEB3B", font=("Helvetica", 12))  # Aplica o estilo ao resultado
resultado_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.grid_columnconfigure(1, weight=1)
root.minsize(400, 300)
root.mainloop()