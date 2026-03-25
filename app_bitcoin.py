import os
import time
from flask import Flask, jsonify
from flask_cors import CORS  # Essencial para destravar o site
import requests
from dotenv import load_dotenv

# Carrega suas chaves do arquivo .env
load_dotenv()

app = Flask(__name__)
# Permite que o seu site no GitHub acesse os dados do seu PC local
CORS(app)

# Simulação de base de dados do Bot (Substitua pela sua lógica de análise)
def get_market_analysis():
    # Aqui entraria sua lógica de RSI, MACD e NLP
    return {
        "BTC/USDT": {
            "price": "67,432.50",
            "score": 0.8,
            "sentiment": "BULLISH (Forte)",
            "headline": "Instituições aumentam custódia de BTC nas últimas 24h.",
            "time": time.strftime("%H:%M:%S")
        },
        "ETH/USDT": {
            "price": "3,521.10",
            "score": 0.2,
            "sentiment": "NEUTRO",
            "headline": "Rede Ethereum apresenta estabilidade nas taxas de gás.",
            "time": time.strftime("%H:%M:%S")
        }
    }

@app.route('/status', methods=['GET'])
def status():
    try:
        data = get_market_analysis()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("---")
    print("🚀 MONITORAMENTO HÍBRIDO ATIVO: KOVALIOSKY DeV")
    print("📡 Servidor Flask rodando em http://127.0.0.1:5000/status")
    print("---")
    # Roda o servidor na porta 5000 que você liberou no Firewall
app.run(host='127.0.0.1', port=5000, debug=True)