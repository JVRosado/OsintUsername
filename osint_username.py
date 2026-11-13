
import subprocess
import sys

def executar_busca():

    print("=" * 55)
    print("          OSINT USERNAME SCANNER")
    print("=" * 55)

    username = input("\nDigite o username: ").strip()

    if not username:
        print("\n[!] Username inválido.")
        return

    print("\nEscolha o tipo de pesquisa:")
    print("\n[1] Busca rápida - 50 sites populares")
    print("[2] Busca profunda - Todos os sites disponíveis")
    print("[0] Sair")

    opcao = input("\nSelecione uma opção: ").strip()

    if opcao == "0":
        print("\nEncerrando...")
        return

    if opcao == "1":
        argumentos = ["--top-sites", "50"]
        modo = "BUSCA RAPIDA"

    elif opcao == "2":
        argumentos = ["--all-sites"]
        modo = "BUSCA PROFUNDA"

    else:
        print("\n[!] Opção inválida.")
        return

    comando = [
        sys.executable,
        "-m",
        "maigret",
        username,
        *argumentos,
        "--no-extracting",
        "--no-recursion",
        "--folderoutput",
        ".",
    ]

    print("\n" + "=" * 55)
    print("INICIANDO INVESTIGAÇÃO")
    print("=" * 55)

    print(f"\nUsername: {username}")
    print(f"Modo: {modo}")
    print("\n[+] Procurando perfis disponíveis...")
    print("[+] Exibindo resultados diretamente no terminal.\n")

    try:
        resultado = subprocess.run(comando, check=False)

        print("\n" + "=" * 55)

        if resultado.returncode == 0:
            print("[+] PESQUISA FINALIZADA")
        else:
            print("[!] Pesquisa finalizada com erros.")

        print("=" * 55)

    except KeyboardInterrupt:
        print("\n[!] Pesquisa interrompida.")

    except Exception as erro:
        print(f"\n[!] Erro: {erro}")


if __name__ == "__main__":
    executar_busca()
