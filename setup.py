import subprocess
import sys

def run_cmd(cmd):
    """Executa comando e mostra resultado"""
    print(f"▶️  Executando: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ Sucesso")
        return True
    else:
        print(f"❌ Erro: {result.stderr}")
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
            print(f"✅ {package} instalado")
        else:
            print(f"❌ Falha ao instalar {package}")
    
    # Criar arquivo .env exemplo
    with open(".env.example", "w") as f:
        f.write("SUPABASE_URL=seu_url_aqui\n")
        f.write("SUPABASE_KEY=sua_chave_aqui\n")
        f.write("CHECK_INTERVAL=3600\n")
    
    print("\n🎉 Configuração concluída!")
    print("\nPróximos passos:")
    print("1. cp .env.example .env")
    print("2. Edite .env com suas credenciais do Supabase")
    print("3. python main.py")

if __name__ == "__main__":
    main()
