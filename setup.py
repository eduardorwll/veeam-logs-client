import subprocess
import sys

def run_cmd(cmd):
    """Executa comando e mostra resultado"""
    print(f"Executando: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Sucesso")
        return True
    else:
        print(f"Erro: {result.stderr}")
        return False

def main():
    print("🔧 Instalando dependências no monitor_env...")
    
    # Lista de dependências
    packages = [
        "supabase",
        "requests", 
        "schedule",
        "python-dotenv"
    ]
    
    # Instalar cada pacote
    for package in packages:
        if run_cmd(f"pip install {package}"):
            print(f"{package} instalado")
        else:
            print(f"Falha ao instalar {package}")

if __name__ == "__main__":
    main()
