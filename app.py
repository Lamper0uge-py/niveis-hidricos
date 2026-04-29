import random
from colorama import Fore, Style

level = random.randint(0, 5) #Gera um nível para simular o estado do sistema;

#Mensagens associadas a cada nível de criticidade (índice = nível);
message = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)",
    "Valor inesperado recebido, verifique os sensores por favor."
]

def get_message_color(level): #Função para retornar a cor da mensagem;
    if level == 0:
        return Fore.RED
    elif level == 1:
        return Fore.YELLOW
    elif level == 2:
        return Fore.GREEN
    elif level == 3:
        return Fore.CYAN
    elif level == 4:
        return Fore.BLUE
    else:
        return Fore.LIGHTRED_EX #Fallback para valores inesperados;

def main(): #Função para exibir a mensagem correspondente ao nível com a cor apropriada;
    print(get_message_color(level) + message[level] + Style.RESET_ALL)

main()
