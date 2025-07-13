# language: pt

Funcionalidade: Cadastro de usuário

  Como QA
  Quero validar os comportamentos funcionais do fluxo de cadastro, para garantir que o sistema
  respeite as regras de negócio definidas.

  Cenário: Cadastrar usuário administrador
    Dado que acessei o login
    Quando clico no botão para acessar o cadastro
    E preencho as informações
    Então devo ver a mensagem "Cadastro realizado com sucesso"
    E devo ser redirecionado para a área logada
    Então posso ver meu usuario logado