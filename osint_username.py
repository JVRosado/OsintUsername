
import subprocess
import sys
import os
from pathlib import Path
from datetime import datetime

def buscar_username():
    print("=" * 55)
    print("       OSINT - BUSCADOR DE USERNAMES")
    print("=" * 55)

    username = input("\nDigite o nome de usuário: ").strip()

    if not username:
        print("[!] Informe um username válido.")
        return

    # Pasta onde os resultados serão armazenados
    pasta = Path("resultados_osint")
    pasta.mkdir(exist_ok=True)

    # Nome da pasta para esta pesquisa
    horario = datetime.now().strftime("%Y%m%d_%H%M%S")
    destino = pasta / f"{username}_{horario}"

    destino.mkdir(exist_ok=True)

    print(f"\n[+] Iniciando pesquisa para: {username}")
    print("[+] Consultando todos os sites cadastrados...")
    print("[+] Isso pode levar alguns minutos.\n")

    comando = [
        sys.executable,
        "-m", "maigret",
        username,
        "-a",
        "--html",
        "--json", "simple",
        "--folderoutput", str(destino)
    ]

    try:
        resultado = subprocess.run(comando)

        if resultado.returncode == 0:
            print("\n[+] Pesquisa finalizada!")
            print(f"[+] Resultados salvos em: {destino.resolve()}")
        else:
            print("\n[!] A pesquisa terminou com avisos ou erros.")
            print("Verifique a instalação e a conexão.")

    except FileNotFoundError:
        print("[!] Python ou Maigret não encontrado.")

    except KeyboardInterrupt:
        print("\n[!] Pesquisa interrompida pelo usuário.")

    except Exception as erro:
        print(f"[!] Erro inesperado: {erro}")


if __name__ == "__main__":
    buscar_username()
