// cypress/e2e/01-login.cy.js
// Testes do fluxo de login no Sauce Demo

describe("Login", () => {

  // Antes de cada teste, acessa a página inicial
  beforeEach(() => {
    cy.visit("/");
  });

  it("deve fazer login com credenciais válidas", () => {
    // Preenche o campo de usuário
    cy.get('[data-test="username"]').type("standard_user");

    // Preenche o campo de senha
    cy.get('[data-test="password"]').type("secret_sauce");

    // Clica no botão de login
    cy.get('[data-test="login-button"]').click();

    // Verifica se foi redirecionado para a página de produtos
    cy.url().should("include", "/inventory");

    // Verifica se o título da página aparece
    cy.get(".title").should("have.text", "Products");
  });

  it("deve exibir erro ao usar senha incorreta", () => {
    cy.get('[data-test="username"]').type("standard_user");
    cy.get('[data-test="password"]').type("senha_errada");
    cy.get('[data-test="login-button"]').click();

    // Verifica se a mensagem de erro aparece
    cy.get('[data-test="error"]').should("be.visible");
    cy.get('[data-test="error"]').should(
      "contain",
      "Username and password do not match"
    );
  });

  it("deve exibir erro ao deixar campos vazios", () => {
    // Clica em login sem preencher nada
    cy.get('[data-test="login-button"]').click();

    // Verifica se a mensagem de campo obrigatório aparece
    cy.get('[data-test="error"]').should("be.visible");
    cy.get('[data-test="error"]').should("contain", "Username is required");
  });

  it("deve exibir erro ao usar usuário bloqueado", () => {
    // O Sauce Demo tem um usuário bloqueado para testar esse cenário
    cy.get('[data-test="username"]').type("locked_out_user");
    cy.get('[data-test="password"]').type("secret_sauce");
    cy.get('[data-test="login-button"]').click();

    cy.get('[data-test="error"]').should("be.visible");
    cy.get('[data-test="error"]').should("contain", "Sorry, this user has been locked out");
  });

});