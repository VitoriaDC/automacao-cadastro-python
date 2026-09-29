import pyautogui
import time
import pandas as pd

# Pausa de segurança entre cada ação do pyautogui
pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema da empresa
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)

# Digita o endereço do sistema e entra
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

# Passo 2: Fazer Login
pyautogui.click(x=928, y=470)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("minhasenha123")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("enter")
time.sleep(3)

# Passo 3: Importar a base de dados
tabela = pd.read_csv("produtos.csv")

# Passo 4 e 5: Cadastrar todos os produtos
for linha in tabela.index:
    # 1. Clica no primeiro campo (Código do Produto)
    pyautogui.click(x=824, y=323)
    
    # Preenche o código
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    
    # Preenche a marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    
    # Preenche o tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    
    # Preenche a categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    
    # Preenche o preço unitário
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    
    # Preenche o custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    
    # Preenche a observação (se houver)
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    
    # Envia o formulário
    pyautogui.press("tab")
    pyautogui.press("enter")
    
    # Rola de volta para o topo da página
    pyautogui.scroll(5000)
    time.sleep(0.5)