import yaml
from os import environ

# Classe para gerenciar configuração
class Config:

    # Dicionário para guardar as configurações
    yml_config = {}

    def __init__(self, config_file):
        # Abrindo arquivo de configurações
        with open(config_file) as file:
            # Lendo as configurações do arquivo e colocando no dicionário
            self.yml_config = yaml.load(file, yaml.Loader)

    # Método para ter acesso as configurações pela chave
    def get(self, key):
        # Tentar achar o valor primeiro na variável de ambiente
        value = environ.get(key)
        if value:
            return value
        # Caso não exista na variável de ambiente pego do dicionário
        return self.yml_config.get(key)

if __name__ == "__main__":
    conf = Config("./config.yml")
    print(conf.get("domain"))
    
