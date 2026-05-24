import pytest
from src.cadastro import GerenciadorClientes

def test_deve_adicionar_cliente_com_sucesso():
    # Arrange (Organizar)
    gerenciador = GerenciadorClientes()
    
    # Act (Agir)
    resultado = gerenciador.adicionar_cliente("Joao Silva")
    
    # Assert (Aferir)
    assert "Joao Silva" in gerenciador.listar_clientes()
    assert resultado == "Cliente Joao Silva adicionado."

def test_nao_deve_adicionar_cliente_com_nome_vazio():
    gerenciador = GerenciadorClientes()
    
    with pytest.raises(ValueError, match="Nome inválido!"):
        gerenciador.adicionar_cliente("")

def test_deve_remover_cliente_existente():
    gerenciador = GerenciadorClientes()
    gerenciador.adicionar_cliente("Maria")
    
    removido = gerenciador.remover_cliente("Maria")
    
    assert removido is True
    assert "Maria" not in gerenciador.listar_clientes()