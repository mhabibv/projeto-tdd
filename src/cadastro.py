class GerenciadorClientes:
    """
    Classe para gerenciamento de um cadastro de clientes.
    """

    def __init__(self):
        """Inicializa a lista de clientes vazia."""
        self.clientes = []

    def adicionar_cliente(self, nome: str):
        """
        Adiciona um cliente à lista.
        Lança ValueError se o nome for vazio ou não for string.
        """
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Nome inválido!")
        
        self.clientes.append(nome.strip())
        return f"Cliente {nome} adicionado."

    def listar_clientes(self):
        """Retorna a lista atual de clientes."""
        return self.clientes

    def remover_cliente(self, nome: str):
        """Remove um cliente pelo nome. Retorna True se removido."""
        if nome in self.clientes:
            self.clientes.remove(nome)
            return True
        return False