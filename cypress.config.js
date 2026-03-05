const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    // URL base do site que vamos testar
    baseUrl: "https://www.saucedemo.com",

    // Tamanho da janela do navegador durante os testes
    viewportWidth: 1280,
    viewportHeight: 720,

    // Tempo máximo de espera para elementos aparecerem (em ms)
    defaultCommandTimeout: 6000,
  },
});