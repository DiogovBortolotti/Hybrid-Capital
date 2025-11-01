from celery import shared_task
from binance.client import Client
from .models import ChaveAPI, RegistroTrade
import time


@shared_task
def monitorar_e_operar(chave_id, simbolo):
    chave = ChaveAPI.objects.get(id=chave_id)
    client = Client(chave.api_key, chave.obter_secret(), testnet=chave.testnet)

    ultimo_preco = None
    while True:
        try:
            ticker = client.get_symbol_ticker(symbol=simbolo)
            preco_atual = float(ticker['price'])

            if ultimo_preco:
                variacao = (preco_atual - ultimo_preco) / ultimo_preco * 100

                if variacao >= 2:
                    RegistroTrade.objects.create(
                        chave=chave, acao=simbolo, tipo="venda",
                        preco=preco_atual, quantidade=0.001
                    )

                elif variacao <= -2:
                    RegistroTrade.objects.create(
                        chave=chave, acao=simbolo, tipo="compra",
                        preco=preco_atual, quantidade=0.001
                    )

            ultimo_preco = preco_atual
            time.sleep(10)
        except Exception as e:
            print(f"Erro: {e}")
            time.sleep(5)
