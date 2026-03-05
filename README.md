# 🤖 Automação de Testes E2E com Cypress

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