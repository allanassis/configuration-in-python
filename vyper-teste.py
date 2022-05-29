from os import path

from vyper import Vyper


def init_config(path_config):
    config_file_path = path.abspath(path_config)

    # Instancia a classe Vyper
    config = Vyper()
    
    # Diz qual será o caminho do arquivo de configuração
    config.add_config_path(config_file_path) 
    
    # Diz qual será a extensão do arquivo de configuração
    config.set_config_type("yml") 
    
    # Diz qual será o prefixo para não existir conflitos entre variáveis de ambiente
    config.set_env_prefix("PREFIX") 

    # Lê as configurações do arquivo
    config.read_in_config()
    
    # Olha primeiro para as variáveis de ambiente antes do arquivo de configuração
    config.automatic_env()
    
    # Checa qualquer alteração no arquivo de configuração para refletir automaticamente
    config.watch_config()

    return config

if __name__ == "__main__":
    # Pronto para uso :D
    conf = init_config(".")
    print(conf.get_string("domain"))