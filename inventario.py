import platform
import psutil
import shutil
import socket

def inventario():
    print("="*40, "INVENTÁRIO DO COMPUTADOR", "="*40)

    # Informações básicas do sistema
    print(f"Sistema Operacional : {platform.system()} {platform.release()}")
    print(f"Versão              : {platform.version()}")
    print(f"Arquitetura         : {platform.machine()}")
    print(f"Processador         : {platform.processor()}")
    print(f"Nome do Computador  : {socket.gethostname()}")
    print(f"Endereço IP         : {socket.gethostbyname(socket.gethostname())}")

    # Memória RAM
    memoria = psutil.virtual_memory()
    print(f"Memória RAM Total   : {round(memoria.total / (1024**3), 2)} GB")

    # Disco
    disco = shutil.disk_usage("/")
    print(f"Disco Total         : {round(disco.total / (1024**3), 2)} GB")
    print(f"Espaço Usado        : {round(disco.used / (1024**3), 2)} GB")
    print(f"Espaço Livre        : {round(disco.free / (1024**3), 2)} GB")

    # CPU
    print(f"Núcleos (físicos)   : {psutil.cpu_count(logical=False)}")
    print(f"Núcleos (lógicos)   : {psutil.cpu_count(logical=True)}")
    print(f"Uso atual da CPU    : {psutil.cpu_percent(interval=1)}%")

    print("="*110)

if __name__ == "__main__":
    inventario()
