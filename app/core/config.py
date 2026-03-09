# BaseSettings é uma classe do Pydantic feita para configurações
# Ela lê automaticamente variáveis de ambiente ou de um arquivo .env
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Nome da aplicação - útil para logs e documentação automática do FastAPI
    APP_NAME: str = "Yoga Pose API"

    # Versão da API
    APP_VERSION: str = "0.1.0"

    # Caminho para o modelo TF salvo
    MODEL_PATH: str = "models/yoga_model.keras" # placeholder

    # Lista com os nomes das poses na mesma ordem que o modelo foi treinado
    # Precisa ajudar conforme o nome das classes
    CLASS_NAMES: list[str] = ["Placeholder"]

    # Tamanho da imagem esperada pelo modelo (altura e largura)
    IMAGE_SIZE: int = 224

    class Config:
        # Se existir um arquivo .env na raíz do projeto,
        # o Pydantic vai ler as variáveis de lá automaticamente
        env_file = ".env"

# Cria uma instância única de Settings que será importada pelo resto do projeto.
# Assim, as configurações são carregadas de uma vez só.
settings = Settings()