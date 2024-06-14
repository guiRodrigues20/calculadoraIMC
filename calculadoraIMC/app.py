import tkinter as tk
from tkinter import messagebox


class BMICalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora de IMC")

        self.label_height = tk.Label(self.root, text="Altura (m):")
        self.label_height.pack()

        self.entry_height = tk.Entry(self.root)
        self.entry_height.pack()

        self.label_weight = tk.Label(self.root, text="Peso (kg):")
        self.label_weight.pack()

        self.entry_weight = tk.Entry(self.root)
        self.entry_weight.pack()

        self.calculate_button = tk.Button(
            self.root, text="Calcular IMC", command=self.calculate_bmi)
        self.calculate_button.pack()

        self.result_label = tk.Label(self.root, text="IMC: ")
        self.result_label.pack()

    def calculate_bmi(self):
        try:
            height = float(self.entry_height.get())
            weight = float(self.entry_weight.get())
            if height <= 0 or weight <= 0:
                raise ValueError("Altura e peso devem ser valores positivos.")

            bmi = weight / (height ** 2)
            self.result_label.config(text=f"IMC: {bmi:.2f}")
            self.show_bmi_category(bmi)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def show_bmi_category(self, bmi):
        if bmi < 18.5:
            category = "Abaixo do peso"
        elif bmi < 24.9:
            category = "Peso normal"
        elif bmi < 29.9:
            category = "Sobrepeso"
        else:
            category = "Obesidade"

        messagebox.showinfo("Categoria do IMC", f"Seu IMC é {
                            bmi:.2f}, que é considerado '{category}'")


def main():
    calculator = BMICalculator()
    calculator.root.mainloop()


if __name__ == "_main_":
    main()
