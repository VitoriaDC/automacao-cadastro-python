# 🤖 Automação de Cadastro de Produtos em Python

> Projeto desenvolvido durante a **Jornada Python** da Hashtag Treinamentos, com foco em automação de processos repetitivos (RPA).

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

---

## 🎬 Demonstração da Automação

<!-- SOLTE OU ARRASTE O SEU GIF AQUI NESSA LINHA DE BAIXO -->


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
<img width="800" height="447" alt="Gravando2026-09-29194017-ezgif com-video-to-gif-converter" src="https://github.com/user-attachments/assets/5f27b573-84b4-473e-9914-03a4cb7f0a2a" />


## 🛠️ Tecnologias Utilizadas

| Ferramenta / Biblioteca | Finalidade |
| :--- | :--- |
| **Python** | Linguagem principal do projeto |
| **PyAutoGUI** | Controle de cliques, digitação e rolagem da tela |
| **Pandas** | Leitura, manipulação e iteração dos dados em CSV |
| **Time** | Gerenciamento de pausas e sincronização de telas |

---

