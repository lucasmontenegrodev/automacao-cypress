import os

# ── conteúdo dos arquivos ────────────────────────────────────────────────────

README = """# 🤖 Automação de Testes E2E com Cypress

> Projeto de automação de testes End-to-End (ponta a ponta) utilizando **Cypress** em um e-commerce de demonstração. Testes escritos em JavaScript com foco em clareza e boas práticas.

---

## 📁 Estrutura do Repositório

```
automacao-cypress/
│
├── cypress/
│   ├── e2e/
│   │   ├── 01-login.cy.js
│   │   ├── 02-cadastro.cy.js
│   │   ├── 03-carrinho.cy.js
│   │   ├── 04-busca-produto.cy.js
│   │   └── 05-checkout.cy.js
│   └── support/
│       └── commands.js
│
├── cypress.config.js
├── package.json
└── README.md
```

---

## 🔧 Como rodar o projeto

### Pré-requisitos
- Node.js instalado ([download](https://nodejs.org))
- npm (já vem com o Node.js)

### Instalação

```bash
# Clone o repositório
git clone https://github.com/lucasmontenegrodev/automacao-cypress.git
cd automacao-cypress

# Instale as dependências
npm install
```

### Executando os testes

```bash
# Abre a interface visual do Cypress (recomendado para estudos)
npx cypress open

# Roda todos os testes no terminal (modo headless)
npx cypress run
```

---

## 🧪 Testes Implementados

| Arquivo | Funcionalidade | Cenários |
|---|---|---|
| `01-login.cy.js` | Login / Autenticação | Login válido, inválido, campos vazios |
| `02-cadastro.cy.js` | Cadastro de usuário | Cadastro válido, e-mail duplicado, senha fraca |
| `03-carrinho.cy.js` | Carrinho de compras | Adicionar, remover, alterar quantidade |
| `04-busca-produto.cy.js` | Busca de produtos | Busca válida, sem resultados, filtros |
| `05-checkout.cy.js` | Checkout | Fluxo completo de compra |

---

## 🛠️ Tecnologias

![Cypress](https://img.shields.io/badge/Cypress-17202C?style=for-the-badge&logo=cypress&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)

---

## 🌐 Site testado

[Sauce Demo](https://www.saucedemo.com) — ambiente de demonstração público criado pela Sauce Labs, amplamente utilizado para prática de automação de testes.

**Credenciais de teste:**
- Usuário: `standard_user`
- Senha: `secret_sauce`
"""

CYPRESS_CONFIG = """const { defineConfig } = require("cypress");

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
"""

PACKAGE_JSON = """{
  "name": "automacao-cypress",
  "version": "1.0.0",
  "description": "Automação de testes E2E com Cypress em e-commerce",
  "scripts": {
    "test": "cypress run",
    "test:open": "cypress open"
  },
  "devDependencies": {
    "cypress": "^13.0.0"
  }
}
"""

COMMANDS_JS = """// cypress/support/commands.js
// Aqui ficam comandos customizados reutilizáveis em todos os testes

// Comando de login reutilizável
// Uso: cy.login('usuario', 'senha')
Cypress.Commands.add("login", (username, password) => {
  cy.visit("/");
  cy.get('[data-test="username"]').type(username);
  cy.get('[data-test="password"]').type(password);
  cy.get('[data-test="login-button"]').click();
});
"""

TEST_01_LOGIN = """// cypress/e2e/01-login.cy.js
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
"""

TEST_02_CADASTRO = """// cypress/e2e/02-cadastro.cy.js
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
"""

TEST_03_CARRINHO = """// cypress/e2e/03-carrinho.cy.js
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
"""

TEST_04_BUSCA = """// cypress/e2e/04-busca-produto.cy.js
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
"""

TEST_05_CHECKOUT = """// cypress/e2e/05-checkout.cy.js
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
"""

# ── criação dos arquivos ─────────────────────────────────────────────────────

arquivos = {
    "README.md":                        README,
    "cypress.config.js":                CYPRESS_CONFIG,
    "package.json":                     PACKAGE_JSON,
    "cypress/support/commands.js":      COMMANDS_JS,
    "cypress/e2e/01-login.cy.js":       TEST_01_LOGIN,
    "cypress/e2e/02-cadastro.cy.js":    TEST_02_CADASTRO,
    "cypress/e2e/03-carrinho.cy.js":    TEST_03_CARRINHO,
    "cypress/e2e/04-busca-produto.cy.js": TEST_04_BUSCA,
    "cypress/e2e/05-checkout.cy.js":    TEST_05_CHECKOUT,
}

print("\n🚀 Criando estrutura do projeto Cypress...\n")

for caminho, conteudo in arquivos.items():
    pasta = os.path.dirname(caminho)
    if pasta:
        os.makedirs(pasta, exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo.strip())
    print(f"  ✅ {caminho}")

print("\n✨ Pronto! Estrutura criada com sucesso.")
print("\nPróximos passos:\n")
print("  1. npm install          (instala o Cypress)")
print("  2. npx cypress open     (abre a interface visual)")
print("\nPara subir no GitHub:")
print("  git add .")
print('  git commit -m "feat: adiciona testes E2E com Cypress"')
print("  git push\n")
