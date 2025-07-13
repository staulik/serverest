# language: pt

Funcionalidade: Validações na tela de login

  Como QA
  Quero validar os elementos visuais e comportamentais da tela de login
  Para garantir a experiência correta do usuário em todos os cenários de autenticação

  @visual
  Cenário: Validar elementos visuais da tela
    Dado que estou na tela de login
    Então os textos, campos e imagem devem estar visíveis

  @negativo
  Esquema do Cenário: Validar mensagens de erro no login
    Dado que estou na tela de login
    Quando eu preencho o email "<email>" e senha "<senha>"
    E clico no botão de login
    Então devo ver "<mensagem_erro>"

    Exemplos:
      | email                     | senha   | mensagem_erro                     |
      | "silvio.tadeu@gmail.com"  | "12345" | "Email e/ou senha inválidos"      |
      |        ""                 | "12345" | "Email é obrigatório"  |
      | "silvio.tadeu@gmail.com"  | ""      | "Password é obrigatório"      |
      | ""                        | ""      | "Email é obrigatório, Password é obrigatório" |
