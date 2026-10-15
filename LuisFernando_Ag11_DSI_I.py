
from colorama import init, Fore, Style

init()

# Lista dos níveis de água
niveis = [
    "Nível 1 - Muito baixo (CRÍTICO)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (ALERTA)"
]

# Função para escolher a cor
def definir_cor(nivel):
    cores = {
        1: Fore.RED,
        2: Fore.YELLOW,
        3: Fore.GREEN,
        4: Fore.CYAN,
        5: Fore.BLUE
    }
    return cores.get(nivel, Fore.WHITE)

# Exibição dos níveis
print("MONITORAMENTO DO RESERVATÓRIO DE ÁGUA\n")

for nivel in range(1, 6):
    cor = definir_cor(nivel)
    print(cor + niveis[nivel - 1] + Style.RESET_ALL)

print("\nMonitoramento finalizado.")
