# 01. ENTRAR NO SISTEMA

# - Instalar Bibliotecas
# %pip install pyautogui time

# - Importar Bibliotecas
import time
import pyautogui

# - Comandos
# press-win > write-chrome > press-enter > write-link > press-enter
# time.sleep(3) [SEMPRE QUE A SCREEN FOR MUDAR, ADICIONAR TIME.SLEEP PARA TEMPO DE CARREGAMENTO]
pyautogui.press("win")
time.sleep(1)

pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(2)

pyautogui.click(x=848, y=443)

time.sleep(2)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(2)

# 02. FAZER LOGIN

# - Criar arquivo auxiliar.py
#   - Importar Bibliotecas
#   - Descobrir posição do Mouse
#     sleep > position

# - Comandos
#   click-campo1 > write-email > press-tab > write-senha > press-tab > press-enter
#   time.sleep()
pyautogui.click(x=595, y=514)
pyautogui.write("aitudopramim@gmail.com")
pyautogui.press("tab")
pyautogui.write("Opa123")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)

# 03. IMPORTAR DATABASE: 

# - Instalar Bibliotecas
# %pip install pandas openpyxl numpy

# - Importar Bibliotecas
import pandas as pd

# - Tabela que vai ler o arquivo do DataBase
tabela = pd.read_csv("produtos.csv")
print(tabela)

# 04. - CADASTRAR PRODUTO

# - Descobrir posição do mouse no campo 1 do Cadastro [auxiliar.py]

# - Comandos
#   click-campo1 > write-campo1 > press-tab > ... > press-enter > scroll()


# 05. CADASTRAR TODOS OS PRODUTOS DO DATABASE

# - Para cada linha da Tabela
#   click-campo1 > campo1-str(loc) > write-campo1 > press-tab > ... > press-enter > scroll() [Comandos]
for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"])
    marca = str(tabela.loc[linha, "marca"])
    tipo = str(tabela.loc[linha, "tipo"])
    categoria = str(tabela.loc[linha, "categoria"])
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    custo = str(tabela.loc[linha, "custo"])
    obs = str(tabela.loc[linha, "obs"])
    
    pyautogui.click(x=594, y=365)

    pyautogui.write(codigo)
    pyautogui.press("tab")

    pyautogui.write(marca)
    pyautogui.press("tab")

    pyautogui.write(tipo)
    pyautogui.press("tab")

    pyautogui.write(categoria)
    pyautogui.press("tab")

    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    
    pyautogui.write(custo)
    pyautogui.press("tab")

    time.sleep(0.5)
    #  [Condição para Campo com valor NaN]
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(5000)