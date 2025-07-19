import pytest
from desafio import depositar, sacar, filtrar_usuario, criar_conta

# Teste de depósito válido
def test_depositar_valido():
    saldo, extrato = depositar(100, 50, "")
    assert saldo == 150
    assert "Depósito" in extrato

# Teste de depósito inválido (valor negativo)
def test_depositar_invalido():
    saldo, extrato = depositar(100, -50, "")
    assert saldo == 100
    assert extrato == ""

# Teste de saque com saldo suficiente
def test_sacar_valido():
    saldo, extrato = sacar(
        saldo=100, valor=50, extrato="", limite=500, numero_saques=1, limite_saques=3
    )
    assert saldo == 50
    assert "Saque" in extrato

# Teste de saque com saldo insuficiente
def test_sacar_sem_saldo():
    saldo, extrato = sacar(
        saldo=20, valor=50, extrato="", limite=500, numero_saques=1, limite_saques=3
    )
    assert saldo == 20
    assert extrato == ""

# Teste de filtro de usuário existente
def test_filtrar_usuario_existente():
    usuarios = [{"cpf": "123", "nome": "Rafael"}]
    usuario = filtrar_usuario("123", usuarios)
    assert usuario["nome"] == "Rafael"

# Teste de filtro de usuário inexistente
def test_filtrar_usuario_inexistente():
    usuarios = [{"cpf": "123", "nome": "Rafael"}]
    usuario = filtrar_usuario("000", usuarios)
    assert usuario is None

# Teste de criação de conta com usuário existente
def test_criar_conta(monkeypatch):
    usuarios = [{"cpf": "123", "nome": "Rafael"}]

    monkeypatch.setattr("builtins.input", lambda _: "123")
    conta = criar_conta("0001", 1, usuarios)

    assert conta["agencia"] == "0001"
    assert conta["numero_conta"] == 1
    assert conta["usuario"]["nome"] == "Rafael"
