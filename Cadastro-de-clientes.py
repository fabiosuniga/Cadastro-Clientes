#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
import sqlite3
import pandas as pd

# Definir nomes dos arquivos localmente
DB_PATH = "banco_clientes.db"
EXCEL_PATH = "banco_clientes.xlsx"

# Criar banco de dados e tabela
conexao = sqlite3.connect(DB_PATH)
c = conexao.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS clientes (
                nome text, 
                sobrenome text, 
                email text, 
                telefone text
             )''')
conexao.commit()
conexao.close()

# Cadastrar clientes
def cadastrar_cliente():
    conexao = sqlite3.connect(DB_PATH)
    c = conexao.cursor()
    c.execute("INSERT INTO clientes VALUES(:nome, :sobrenome, :email, :telefone)", 
             {
                 'nome': entry_nome.get(),
                 'sobrenome': entry_sobrenome.get(),
                 'email': entry_email.get(),
                 'telefone': entry_telefone.get()
             }) 

    # Deletar nomes do campo após serem inseridos
    entry_nome.delete(0, 'end')
    entry_sobrenome.delete(0, 'end')
    entry_email.delete(0, 'end')
    entry_telefone.delete(0, 'end')

    conexao.commit()
    conexao.close()

# Exportar clientes para o Excel
def exporta_clientes():
    conexao = sqlite3.connect(DB_PATH)
    c = conexao.cursor()
    c.execute("SELECT *, oid FROM clientes")

    clientes_cadastrados = c.fetchall()

    # Criar DataFrame com os dados extraídos
    df_clientes = pd.DataFrame(clientes_cadastrados, columns=['nome', 'sobrenome', 'email', 'telefone', 'id_banco'])

    # Exportar para Excel
    df_clientes.to_excel(EXCEL_PATH, index=False)

    print("Exportação concluída com sucesso!")
    print(df_clientes)

    conexao.commit()
    conexao.close()

# Configuração da Interface Gráfica

# Criar o título da janela
janela = tk.Tk()
janela.title('Ferramenta de Cadastro de Clientes')

# Criar etiquetas
label_nome = tk.Label(janela, text='Nome', width=30)
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_sobrenome = tk.Label(janela, text='Sobrenome', width=30)
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text='E-mail', width=30)
label_email.grid(row=2, column=0, padx=10, pady=10)

label_telefone = tk.Label(janela, text='Telefone', width=30)
label_telefone.grid(row=3, column=0, padx=10, pady=10)

# Criar campos de entrada (widgets)
entry_nome = tk.Entry(janela, width=30)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

entry_sobrenome = tk.Entry(janela, width=30)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

entry_email = tk.Entry(janela, width=30)
entry_email.grid(row=2, column=1, padx=10, pady=10)

entry_telefone = tk.Entry(janela, width=30)
entry_telefone.grid(row=3, column=1, padx=10, pady=10)

# Criar os botões de ação
botao_cadastrar = tk.Button(janela, text='Cadastrar cliente', command=cadastrar_cliente)
botao_cadastrar.grid(row=4, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

botao_exportar = tk.Button(janela, text='Exportar Base de clientes', command=exporta_clientes)
botao_exportar.grid(row=5, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

# Iniciar o loop da aplicação
janela.mainloop()


# In[ ]:




