// cypress/e2e/04-busca-produto.cy.js
// Testes de ordenação e filtro de produtos

describe("Filtro e ordenação de produtos", () => {

  beforeEach(() => {
    cy.login("standard_user", "secret_sauce");
  });

  it("deve ordenar produtos por nome A-Z", () => {
    // Seleciona a opção de ordenação
    cy.get('[data-test="product-sort-container"]').select("az");

    // Pega o nome do primeiro produto e verifica se está em ordem alfabética
    cy.get(".inventory_item_name").first().should("have.text", "Sauce Labs Backpack");
  });

  it("deve ordenar produtos por nome Z-A", () => {
    cy.get('[data-test="product-sort-container"]').select("za");

    // O primeiro item deve ser o último em ordem alfabética
    cy.get(".inventory_item_name").first().should("have.text", "Test.allTheThings() T-Shirt (Red)");
  });

  it("deve ordenar produtos por menor preço", () => {
    cy.get('[data-test="product-sort-container"]').select("lohi");

    // Verifica que o primeiro produto é o mais barato
    cy.get(".inventory_item_price").first().should("have.text", "$7.99");
  });

  it("deve ordenar produtos por maior preço", () => {
    cy.get('[data-test="product-sort-container"]').select("hilo");

    // Verifica que o primeiro produto é o mais caro
    cy.get(".inventory_item_price").first().should("have.text", "$49.99");
  });

  it("deve exibir todos os produtos na página", () => {
    // O Sauce Demo tem 6 produtos cadastrados
    cy.get(".inventory_item").should("have.length", 6);
  });

});