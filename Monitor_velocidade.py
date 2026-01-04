import psutil
import time
from datetime import datetime

def medidor_fixo():
    print("-" * 63)
    print("🚀 Medidor de Rede - Pressione Ctrl+C para sair")
    print("-" * 63)
    
    cores = {
        'verde': '\033[92m',
        'azul': '\033[94m',
        'amarelo': '\033[93m',
        'vermelho': '\033[91m',
        'roxo': '\033[95m',
        'reset': '\033[0m',
        'negrito': '\033[1m'
    }
    
    C = cores
    
    stat_inicial = psutil.net_io_counters()
    stat_antes = stat_inicial
    inicio_tempo = time.time()
    
    total_upload_mb = 0
    total_download_mb = 0
    pico_upload = 0
    pico_download = 0
    
    print("\n")
    print("-" * 63)
    
    try:
        while True:
            time.sleep(1)
            stat_depois = psutil.net_io_counters()
            
            upload = (stat_depois.bytes_sent - stat_antes.bytes_sent) * 8 / 1_000_000
            download = (stat_depois.bytes_recv - stat_antes.bytes_recv) * 8 / 1_000_000
            
            total_upload_mb += (stat_depois.bytes_sent - stat_antes.bytes_sent) / (1024 * 1024)
            total_download_mb += (stat_depois.bytes_recv - stat_antes.bytes_recv) / (1024 * 1024)
            
            if upload > pico_upload:
                pico_upload = upload
            if download > pico_download:
                pico_download = download
            
            def escolher_emoji(valor):
                if valor > 10:
                    return '🔥' 
                elif valor > 1:
                    return '⚡' 
                elif valor > 0.1:
                    return '📶'  
                else:
                    return '💤' 
            
            emoji_up = escolher_emoji(upload)
            emoji_down = escolher_emoji(download)
            
            hora_atual = datetime.now().strftime("%H:%M:%S")
            
            print("\033[2A", end="")
            
            print(f"{C['negrito']}🕒 {hora_atual}{C['reset']} | "
                  f"{emoji_down} ↓ {C['verde']}{download:6.3f}{C['reset']} Mbps | "
                  f"{emoji_up} ↑ {C['azul']}{upload:6.3f}{C['reset']} Mbps")

            print("-" * 63)
            stat_antes = stat_depois
            
    except KeyboardInterrupt:
        tempo_total = time.time() - inicio_tempo
        
        stat_final = psutil.net_io_counters()
        upload_total_bytes = stat_final.bytes_sent - stat_inicial.bytes_sent
        download_total_bytes = stat_final.bytes_recv - stat_inicial.bytes_recv
        
        def formatar_bytes(bytes_size):
            if bytes_size >= 1024 * 1024 * 1024:
                return f"{bytes_size / (1024 * 1024 * 1024):.2f} GB"
            elif bytes_size >= 1024 * 1024:
                return f"{bytes_size / (1024 * 1024):.2f} MB"
            elif bytes_size >= 1024:
                return f"{bytes_size / 1024:.2f} KB"
            else:
                return f"{bytes_size} bytes"
        
        print(f"\n{C['negrito']}{C['verde']}📊 RELATÓRIO DE USO DE DADOS{C['reset']}")
        print(f"{C['negrito']}{'=' * 50}{C['reset']}")
        print(f"{C['azul']}⏱️  Tempo total: {int(tempo_total)} segundos{C['reset']}")
        print(f"{C['azul']}📅 Início: {datetime.fromtimestamp(inicio_tempo).strftime('%H:%M:%S')}{C['reset']}")
        print(f"{C['azul']}📅 Fim: {datetime.now().strftime('%H:%M:%S')}{C['reset']}")
        print()
        print(f"{C['verde']}📥 DOWNLOAD TOTAL:{C['reset']}")
        print(f"  {formatar_bytes(download_total_bytes)}")
        print(f"  Média: {download_total_bytes / tempo_total / 1024:.1f} KB/s")
        print(f"  Pico: {pico_download:.2f} Mbps")
        print()
        print(f"{C['azul']}📤 UPLOAD TOTAL:{C['reset']}")
        print(f"  {formatar_bytes(upload_total_bytes)}")
        print(f"  Média: {upload_total_bytes / tempo_total / 1024:.1f} KB/s")
        print(f"  Pico: {pico_upload:.2f} Mbps")
        print()
        print(f"{C['roxo']}📊 TOTAL TRANSFERIDO:{C['reset']}")
        print(f"  {formatar_bytes(upload_total_bytes + download_total_bytes)}")
        print(f"  ({download_total_bytes:,} bytes + {upload_total_bytes:,} bytes)")
        print(f"{C['negrito']}{'=' * 50}{C['reset']}")
        
        salvar = input(f"\n{C['amarelo']}💾 Deseja salvar este relatório em um arquivo? (s/n): {C['reset']}")
        if salvar.lower() == 's':
            data_atual = datetime.now().strftime("%Y%m%d")
            nome_arquivo = f"Relatorio_uso_rede_{data_atual}.txt"
            
            with open(nome_arquivo, 'w', encoding='utf-8') as f:
                f.write("📊 RELATÓRIO DE USO DE DADOS\n")
                f.write("=" * 50 + "\n")
                f.write(f"⏱️  Tempo total: {int(tempo_total)} segundos\n")
                f.write(f"📅 Início: {datetime.fromtimestamp(inicio_tempo).strftime('%H:%M:%S')}\n")
                f.write(f"📅 Fim: {datetime.now().strftime('%H:%M:%S')}\n\n")
                f.write(f"📥 DOWNLOAD TOTAL:\n")
                f.write(f"  {formatar_bytes(download_total_bytes)}\n")
                f.write(f"  Média: {download_total_bytes / tempo_total / 1024:.1f} KB/s\n")
                f.write(f"  Pico: {pico_download:.2f} Mbps\n\n")
                f.write(f"📤 UPLOAD TOTAL:\n")
                f.write(f"  {formatar_bytes(upload_total_bytes)}\n")
                f.write(f"  Média: {upload_total_bytes / tempo_total / 1024:.1f} KB/s\n")
                f.write(f"  Pico: {pico_upload:.2f} Mbps\n\n")
                f.write(f"📊 TOTAL TRANSFERIDO:\n")
                f.write(f"  {formatar_bytes(upload_total_bytes + download_total_bytes)}\n")
                f.write(f"  ({download_total_bytes:,} bytes + {upload_total_bytes:,} bytes)\n")
                f.write("=" * 50 + "\n")
            
            print(f"{C['verde']}✅ Relatório salvo como: {nome_arquivo}{C['reset']}")
        
        print(f"\n{C['negrito']}{C['roxo']}🎯 Medidor finalizado!{C['reset']}")

if __name__ == "__main__":
    medidor_fixo()
