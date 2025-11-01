from django.conf import settings
from django.db import models
from cryptography.fernet import Fernet

CHAVE_CRIPTO = settings.ENCRYPT_KEY.encode()


def criptografar(valor: str) -> str:
    f = Fernet(CHAVE_CRIPTO)
    return f.encrypt(valor.encode()).decode()


def descriptografar(token: str) -> str:
    f = Fernet(CHAVE_CRIPTO)
    return f.decrypt(token.encode()).decode()


class ChaveAPI(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="chaves_api"
    )
    nome = models.CharField(max_length=100, default="Binance")
    api_key = models.CharField(max_length=255)
    api_secret_enc = models.TextField()
    testnet = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def definir_secret(self, secret: str):
        self.api_secret_enc = criptografar(secret)

    def obter_secret(self) -> str:
        return descriptografar(self.api_secret_enc)

    def __str__(self):
        return f"{self.nome} ({'Testnet' if self.testnet else 'Real'})"


class RegistroTrade(models.Model):
    chave = models.ForeignKey(ChaveAPI, on_delete=models.CASCADE)
    acao = models.CharField(max_length=50)
    tipo = models.CharField(max_length=10)
    preco = models.FloatField()
    quantidade = models.FloatField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.acao} - {self.tipo} - {self.preco}"
