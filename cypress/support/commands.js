// cypress/support/commands.js
// Aqui ficam comandos customizados reutilizáveis em todos os testes

// Comando de login reutilizável
// Uso: cy.login('usuario', 'senha')
Cypress.Commands.add("login", (username, password) => {
  cy.visit("/");
  cy.get('[data-test="username"]').type(username);
  cy.get('[data-test="password"]').type(password);
  cy.get('[data-test="login-button"]').click();
});