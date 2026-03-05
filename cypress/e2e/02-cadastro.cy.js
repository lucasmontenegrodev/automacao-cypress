// cypress/e2e/02-cadastro.cy.js
// Testes do fluxo de cadastro no Sauce Demo
// Obs: o Sauce Demo não tem cadastro real — simulamos validações de formulário
// Esse padrão de teste se aplica a qualquer sistema com formulário de cadastro

describe("Cadastro de usuário", () => {

  beforeEach(() => {
    cy.visit("/");
  });

  it("deve exibir erro ao tentar login com usuário não cadastrado", () => {
    // Simula tentativa de acesso com usuário inexistente
    cy.get('[data-test="username"]').type("usuario_novo_nao_cadastrado");
    cy.get('[data-test="password"]').type("Senha@123");
    cy.get('[data-test="login-button"]').click();

    // Sistema deve rejeitar e exibir mensagem de erro
    cy.get('[data-test="error"]').should("be.visible");
    cy.get('[data-test="error"]').should(
      "contain",
      "Username and password do not match"
    );
  });

  it("deve exibir erro ao deixar o campo de usuário vazio", () => {
    cy.get('[data-test="password"]').type("Senha@123");
    cy.get('[data-test="login-button"]').click();

    cy.get('[data-test="error"]').should("be.visible");
    cy.get('[data-test="error"]').should("contain", "Username is required");
  });

  it("deve exibir erro ao deixar o campo de senha vazio", () => {
    cy.get('[data-test="username"]').type("standard_user");
    cy.get('[data-test="login-button"]').click();

    cy.get('[data-test="error"]').should("be.visible");
    cy.get('[data-test="error"]').should("contain", "Password is required");
  });

  it("deve permitir fechar a mensagem de erro", () => {
    // Gera um erro primeiro
    cy.get('[data-test="login-button"]').click();
    cy.get('[data-test="error"]').should("be.visible");

    // Fecha a mensagem de erro clicando no X
    cy.get('[data-test="error"]').find("button").click();

    // Verifica se a mensagem sumiu
    cy.get('[data-test="error"]').should("not.exist");
  });

});