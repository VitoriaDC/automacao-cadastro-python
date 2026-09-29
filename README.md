# 🤖 Automação de Cadastro de Produtos em Python

> Projeto desenvolvido durante a **Jornada Python** da Hashtag Treinamentos, com foco em automação de processos repetitivos (RPA).

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

---

## 💻 Sobre o Projeto

Este projeto automatiza o fluxo completo de cadastro em um sistema web corporativo. A solução integra leitura de dados estruturados em CSV e simulação de comandos humanos de teclado e mouse, eliminando o preenchimento manual, reduzindo erros operacionais e otimizando o tempo de execução.

### 🔄 Fluxo da Automação
1. **Inicialização do Navegador:** Abre o Google Chrome e acessa automaticamente a página do sistema.
2. **Autenticação:** Preenche as credenciais de acesso e realiza o login com segurança.
3. **Leitura da Base de Dados:** Carrega os dados dos produtos via `pandas`.
4. **Ciclo de Cadastro:** Percorre linha por linha da tabela, preenchendo todos os campos do formulário (código, marca, tipo, categoria, preços e observações).
5. **Envio e Reset de Tela:** Submete o formulário e rola a página de volta ao topo para iniciar o próximo cadastro.

---

## 🛠️ Tecnologias Utilizadas

| Ferramenta / Biblioteca | Finalidade |
| :--- | :--- |
| **Python** | Linguagem principal do projeto |
| **PyAutoGUI** | Controle de cliques, digitação e rolagem da tela |
| **Pandas** | Leitura, manipulação e iteração dos dados em CSV |
| **Time** | Gerenciamento de pausas e sincronização de telas |

---

## 🛑 Como Parar a Execução (Parada de Emergência)

Como o script assume o controle do mouse e do teclado, utilize uma das opções abaixo caso precise interromper o código imediatamente:

* **Pelo Mouse (Fail-Safe):** Puxe o mouse rapidamente com a mão até o **extremo canto superior esquerdo da tela** (coordenada `0, 0`). O PyAutoGUI possui essa trava de segurança de fábrica e encerra o script na mesma hora.
* **Pelo Teclado:** Se estiver com a janela do VS Code / Terminal visível, pressione **`Ctrl + C`** para abortar o processo.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Ter o Python instalado na máquina.

1. **Clone ou baixe este repositório:**
   ```bash
   git clone [https://github.com/VitoriaDC/automacao-cadastro-python.git](https://github.com/VitoriaDC/automacao-cadastro-python.git)
