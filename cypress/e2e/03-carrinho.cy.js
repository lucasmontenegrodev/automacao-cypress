// cypress/e2e/03-carrinho.cy.js
// Testes do carrinho de compras

describe("Carrinho de compras", () => {

  // Antes de cada teste faz login automaticamente
  beforeEach(() => {
    cy.login("standard_user", "secret_sauce");
  });

  it("deve adicionar um produto ao carrinho", () => {
    // Clica em "Add to cart" no primeiro produto
    cy.get('[data-test="add-to-cart-sauce-labs-backpack"]').click();

    // Verifica se o badge do carrinho mostra 1 item
    cy.get(".shopping_cart_badge").should("have.text", "1");
  });

  it("deve remover um produto do carrinho", () => {
    // Adiciona o produto
    cy.get('[data-test="add-to-cart-sauce-labs-backpack"]').click();
    cy.get(".shopping_cart_badge").should("have.text", "1");

    // Remove o produto
    cy.get('[data-test="remove-sauce-labs-backpack"]').click();

    // Verifica se o badge sumiu (carrinho vazio)
    cy.get(".shopping_cart_badge").should("not.exist");
  });

  it("deve adicionar múltiplos produtos ao carrinho", () => {
    cy.get('[data-test="add-to-cart-sauce-labs-backpack"]').click();
    cy.get('[data-test="add-to-cart-sauce-labs-bike-light"]').click();
    cy.get('[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click();

    // Verifica se o badge mostra 3 itens
    cy.get(".shopping_cart_badge").should("have.text", "3");
  });

  it("deve exibir os produtos corretos dentro do carrinho", () => {
    cy.get('[data-test="add-to-cart-sauce-labs-backpack"]').click();

    // Acessa a página do carrinho
    cy.get(".shopping_cart_link").click();

    // Verifica se o produto aparece listado no carrinho
    cy.get(".cart_item").should("have.length", 1);
    cy.get(".inventory_item_name").should("have.text", "Sauce Labs Backpack");
  });

});