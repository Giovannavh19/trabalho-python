import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
import openpyxl

def carregar_dados():
    dados = 'dadosvenda.csv'
    vendas = pd.read_csv(dados)
    coluna = vendas['produto']
    coluna1 = vendas['valor']
    mostrar = vendas.head()
    plt.bar(coluna, coluna1)
    plt.show()
    texto.config(text= mostrar)

def carregar_grafico():
    dados = 'dadosvenda.csv'
    vendas = pd.read_csv(dados)

 


root = tk.Tk()
root.title("dados de vendas de uma loja de roupa")
root.geometry("800x600")

btn_carregar = tk.Button(root, text="Carregar Dados", command=carregar_dados)
btn_carregar.pack()
btn_grafico= tk.Button(root, text="Carregar Gráfico", command=carregar_grafico)
btn_grafico.pack()
texto = tk.Label(root, text='')
texto.pack()

root.mainloop()
