💻 Projeto: Sistema Bancário em Python
Este projeto simula um sistema bancário simples com funcionalidades como:

Depósito

Saque com limite diário

Extrato bancário

Cadastro de usuários

Criação e listagem de contas

O objetivo é praticar lógica de programação, modularização, uso de funções e testes automatizados em Python.

📂 Estrutura do Projeto

📁 projeto_banco/
├── banco.py           # Código principal do sistema bancário
├── test_banco.py      # Testes automatizados com pytest
└── README.md          # Documentação do projeto

🧠 Funcionalidades principais
menu() – Exibe o menu de operações

depositar() – Realiza depósitos válidos e atualiza o extrato

sacar() – Faz saques respeitando limite de valor e quantidade

exibir_extrato() – Mostra todas as movimentações e saldo atual

criar_usuario() – Cadastra novos usuários por CPF

criar_conta() – Cria contas para usuários existentes

listar_contas() – Mostra todas as contas criadas

main() – Controla o fluxo principal do sistema


✅ Testes Automatizados
Os testes são escritos com pytest e cobrem:

Depósitos válidos e inválidos

Saques com saldo suficiente, limite excedido e valores inválidos

Filtro de usuários por CPF

Criação de conta para usuários existentes

📄 Exemplo de teste:

def test_depositar_valido():
    saldo, extrato = depositar(100, 50, "")
    assert saldo == 150
    assert "Depósito" in extrato

🧪 Como rodar os testes

1. Instale o pytest:
pip install pytest

2.Execute os testes com:
python -m pytest

Observações:
🔒 O script banco.py possui um if __name__ == "__main__" para evitar que a função main() rode durante os testes.

🚀 Próximos Passos:
Adicionar persistência em arquivos ou banco de dados

Implementar autenticação de usuário

Melhorar a cobertura de testes com testes de entrada inválida

Criar interface gráfica com tkinter ou versão web com Flask


