from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.ml.model import load_model
from app.core.config import settings

# O lifespan é uma função do FastAPI que controla o ciclo de vida
# O ciclo de vida da aplicação: o que roda ao ligar e ao desligar
@asynccontextmanager
async def lifespan(app: FastAPI):

    # Tudo antes do "yield" roda quando a PI liga (startup)
    # Carregamos o modelo aqui para que ele não carregue a cada requisição
    print(f'Carregando modelo de {settings.MODEL_PATH}...')
    app.state.model = load_model(settings.MODEL_PATH)
    print("Modelo carregado com sucesso")

    # O yield marca a separação entre startup e shutdown
    # A API fia "viva" enquanto estiver rodando.
    yield

    # tudo depois do "yield" roda quando a API desliga (shutdown)
    # boa prática liberar recursos
    print("Encerrando aplicação...")
    app.state.model = None