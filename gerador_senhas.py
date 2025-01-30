import tkinter as tk
from tkinter import messagebox, ttk
import random
import secrets
import math
import pyperclip

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Senhas Seguras")
        self.root.geometry("500x400")

        # Configuração da interface gráfica
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Comprimento da Senha:").grid(row=0, column=0, padx=5, pady=5)
        self.length_var = tk.IntVar(value=12)
        self.length_entry = tk.Entry(frame, textvariable=self.length_var, width=5)
        self.length_entry.grid(row=0, column=1, padx=5, pady=5)

        # Opções de caracteres
        self.include_upper = tk.BooleanVar(value=True)
        self.include_lower = tk.BooleanVar(value=True)
        self.include_numbers = tk.BooleanVar(value=True)
        self.include_symbols = tk.BooleanVar(value=True)

        tk.Checkbutton(frame, text="Letras Maiúsculas", variable=self.include_upper).grid(row=1, column=0, sticky="w")
        tk.Checkbutton(frame, text="Letras Minúsculas", variable=self.include_lower).grid(row=2, column=0, sticky="w")
        tk.Checkbutton(frame, text="Números", variable=self.include_numbers).grid(row=3, column=0, sticky="w")
        tk.Checkbutton(frame, text="Símbolos", variable=self.include_symbols).grid(row=4, column=0, sticky="w")

        # Botão para gerar senha
        self.btn_generate = tk.Button(frame, text="Gerar Senha", command=self.generate_password)
        self.btn_generate.grid(row=5, column=0, columnspan=2, pady=10)

        # Exibição da senha gerada
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(self.root, textvariable=self.password_var, font=("Arial", 14), justify="center", width=30)
        self.password_entry.pack(pady=10)

        # Botões adicionais
        btn_copy = tk.Button(self.root, text="Copiar Senha", command=self.copy_to_clipboard)
        btn_copy.pack(pady=5)

        btn_entropy = tk.Button(self.root, text="Calcular Entropia", command=self.calculate_entropy)
        btn_entropy.pack(pady=5)

        # Exibição da entropia
        self.entropy_label = tk.Label(self.root, text="Entropia: -", font=("Arial", 12))
        self.entropy_label.pack(pady=10)

    def generate_password(self):
        length = self.length_var.get()
        if length < 6:
            messagebox.showerror("Erro", "O comprimento mínimo da senha é 6 caracteres.")
            return
        
        char_sets = ""
        if self.include_upper.get():
            char_sets += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if self.include_lower.get():
            char_sets += "abcdefghijklmnopqrstuvwxyz"
        if self.include_numbers.get():
            char_sets += "0123456789"
        if self.include_symbols.get():
            char_sets += "!@#$%^&*()-_=+[]{}|;:,.<>?/"

        if not char_sets:
            messagebox.showerror("Erro", "Selecione ao menos um tipo de caractere.")
            return

        password = "".join(secrets.choice(char_sets) for _ in range(length))
        self.password_var.set(password)

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copiado", "Senha copiada para a área de transferência!")

    def calculate_entropy(self):
        password = self.password_var.get()
        if not password:
            messagebox.showerror("Erro", "Gere uma senha primeiro!")
            return

        char_set_size = 0
        if self.include_upper.get():
            char_set_size += 26
        if self.include_lower.get():
            char_set_size += 26
        if self.include_numbers.get():
            char_set_size += 10
        if self.include_symbols.get():
            char_set_size += 30  # Aproximadamente

        entropy = len(password) * math.log2(char_set_size)
        self.entropy_label.config(text=f"Entropia: {entropy:.2f} bits")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
