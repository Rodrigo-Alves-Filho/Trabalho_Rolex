import subprocess
import webbrowser
import http.server
import socketserver
import threading
import os
import sys

# Configurações
PORT = 8000
HTML_REPORT = "profile_report.html"
CSV_FILE = "rolex_scaper_clean.csv" 

# 1. Gerar o HTML com seu pipeline
subprocess.run([sys.executable, "main.py", "profile", CSV_FILE])

# 2. Iniciar o servidor em background
def serve_html():
    os.chdir(".")
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Servidor rodando em http://localhost:{PORT}")
        httpd.serve_forever()

thread = threading.Thread(target=serve_html, daemon=True)
thread.start()

# 3. Abrir no navegador
webbrowser.open(f"http://localhost:{PORT}/index.html")

# Manter o script vivo (Ctrl+C para parar)
input("Pressione Enter para encerrar o servidor...\n")
