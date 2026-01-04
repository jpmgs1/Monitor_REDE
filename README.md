# 🚀 Medidor de Uso de Rede em Tempo Real (CLI)

Ferramenta em **Python** para monitoramento de **upload e download da interface de rede**, executada diretamente no terminal, com exibição em tempo real, emojis dinâmicos, cores ANSI e geração de relatório final.

## 📌 Visão Geral

Este projeto implementa um **medidor de tráfego de rede em tempo real**, utilizando a biblioteca `psutil` para coletar estatísticas da interface de rede do sistema operacional.

A aplicação é executada no **terminal (CLI)** e exibe, a cada segundo:

- 📥 Velocidade de download (Mbps)
- 📤 Velocidade de upload (Mbps)
- Emojis dinâmicos conforme intensidade do tráfego
- Registro de picos de upload e download
- Relatório final detalhado ao encerrar a execução

## 🖥️ Funcionamento no Terminal

Durante a execução, o programa mostra:

🕒 21:45:10 | 📶 ↓ 1.234 Mbps | ⚡ ↑ 0.512 Mbps


Os valores são atualizados **em tempo real**, sem poluir o terminal, utilizando controle de cursor ANSI.

## 🎯 Funcionalidades

- ⏱️ Monitoramento contínuo (1 segundo de intervalo)
- 📊 Cálculo de:
  - Velocidade instantânea (Mbps)
  - Total transferido (Upload + Download)
  - Média de transferência
  - Pico de upload e download
- 🎨 Interface colorida no terminal
- 😀 Emojis indicativos de intensidade do tráfego
- 📄 Geração opcional de relatório em arquivo `.txt`
- ⛔ Finalização segura com `Ctrl + C`

## 📦 Tecnologias Utilizadas

- **Python 3**
- **psutil**
- Biblioteca padrão:
  - `time`
  - `datetime`

## 📥 Instalação

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/medidor-rede-cli.git
cd medidor-rede-cli
Python Monitor_velocidade.py


