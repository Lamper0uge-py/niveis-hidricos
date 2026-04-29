# 💧 Sistema de Controle e Alerta de Níveis Hídricos 🌊

Sistema simples para monitoramento de reservatórios de água executado no terminal.

---

## 🎯 Objetivo

Exibir mensagens de alerta no terminal com cores diferentes, conforme o nível de água do reservatório.

---

## 🛠 Tecnologias Utilizadas

- ![Python](https://img.shields.io/badge/code-python-3776AB?style=for-the-badge&logo=python&logoColor=white)
- ![Git](https://img.shields.io/badge/version%20control-git-F05032?style=for-the-badge&logo=git&logoColor=white)

---

## 🧱 Estrutura do Projeto

O projeto foi desenvolvido como uma simulação simples de monitoramento de nível de um reservatório, utilizando conceitos básicos de Python como listas, funções e bibliotecas externas.

---

## 🐛 Tratamento de Erros

### Tratamento implementado
- Existe um fallback de cor na função get_message_color():
    - Caso o nível não esteja entre os valores esperados (0 a 4), o programa retorna uma cor padrão (LIGHTRED_EX).
- A lista de mensagens contém uma posição extra para lidar com valores inesperados:
    - "Valor inesperado recebido, verifique os sensores por favor."

### Limitação atual
    - O acesso à lista é feito diretamente com message[level], o que pode gerar erro (IndexError) caso o valor ultrapasse o tamanho da lista.

---

## 🚀 Melhorias Futuras

#### Pensando no sistema como um ambiente real de monitoramento, algumas evoluções possíveis a serem implementadas são:

### Simulação mais realista
- Substituir o valor aleatório por dados vindos de sensores (ou simulação mais complexa)
- Simular variações contínuas do nível do reservatório
- Criar diferentes tipos de alerta (visual, sonoro, etc.)

### Organização do código
- Separar responsabilidades em funções ou módulos adicionais

### Funcionalidades extras
- Registro (log) dos níveis ao longo do tempo
- Exibição de histórico
- Interface interativa no terminal

### Robustez
- Garantir que o nível esteja sempre dentro de um intervalo válido
- Padronizar os níveis com constantes ou enumerações
- Melhorar o controle de erros para simular falhas de sensores
- Utilizar try/except para garantir a robustez do sistema diante de falhas externas, como erros de leitura de sensores ou dados inesperados

---
