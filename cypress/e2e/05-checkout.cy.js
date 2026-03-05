// cypress/e2e/05-checkout.cy.js
// Testes do fluxo completo de checkout (compra)

describe("Checkout", () => {

  beforeEach(() => {
    cy.login("standard_user", "secret_sauce");
  });

  it("deve completar o fluxo de checkout com sucesso", () => {
    // Passo 1: Adiciona produto ao carrinho
    cy.get('[data-test="add-to-cart-sauce-labs-backpack"]').click();

    // Passo 2: Acessa o carrinho
    cy.get(".shopping_cart_link").click();
    cy.url().should("include", "/cart");

    // Passo 3: Clica em Checkout
    cy.get('[data-test="checkout"]').click();
    cy.url().should("include", "/checkout-step-one");

    // Passo 4: Preenche os dados pessoais
    cy.get('[data-test="firstName"]').type("Lucas");
    cy.get('[data-test="lastName"]').type("Montenegro");
    cy.get('[data-test="postalCode"]').type("50000-000");
    cy.get('[data-test="continue"]').click();

    // Passo 5: Verifica o resumo do pedido
    cy.url().should("include", "/checkout-step-two");
    cy.get(".summary_info").should("be.visible");

    // Passo 6: Finaliza o pedido
    cy.get('[data-test="finish"]').click();

    // Passo 7: Verifica a mensagem de sucesso
    cy.url().should("include", "/checkout-complete");
    cy.get(".complete-header").should("have.text", "Thank you for your order!");
  });

  it("deve exibir erro ao tentar avançar sem preencher os dados", () => {
    cy.get('[data-test="add-to-cart-sauce-labs-backpack"]').click();
    cy.get(".shopping_cart_link").click();
    cy.get('[data-test="checkout"]').click();

    // Tenta avançar sem preencher nada
    cy.get('[data-test="continue"]').click();

    // Verifica mensagem de erro
    cy.get('[data-test="error"]').should("be.visible");
    cy.get('[data-test="error"]').should("contain", "First Name is required");
  });

  it("deve permitir cancelar o checkout e voltar ao carrinho", () => {
    cy.get('[data-test="add-to-cart-sauce-labs-backpack"]').click();
    cy.get(".shopping_cart_link").click();

    // Clica em Cancel em vez de Checkout
    cy.get('[data-test="continue-shopping"]').click();

    // Verifica que voltou para a lista de produtos
    cy.url().should("include", "/inventory");
  });

});