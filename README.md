# Asset Management API🖥️
[APP](https://github.com/igormaxlima/assets-management-app)

## Esse aplicativo de gerenciamento de ativos é uma ferramenta projetada para ajudar empresas e indivíduos a acompanhar, monitorar e gerenciar seus ativos de forma eficiente. Isso inclui uma variedade de itens, como equipamentos, propriedades, veículos e investimentos financeiros.



https://github.com/pedronassero/assets-management-api/assets/121307602/3c626927-08e1-4d46-be28-82ff7c6e3a24



## 1. Introdução

### 1.1 Propósito

Este documento tem como objetivo detalhar os requisitos para o sistema de gerenciamento de ativos de TI, proporcionando uma visão clara das funcionalidades e estrutura necessárias para a implementação do sistema.

### 1.2 Escopo do Projeto

O sistema permitirá a manutenção de ativos de TI, gerenciamento das dependências entre os ativos, e fornecerá uma interface para a listagem e visualização das relações entre os ativos. O sistema contará com um menu de opções para facilitar a navegação do usuário e persistência dos dados em formato de arquivo.

## 2. Descrição Geral

### 2.1 Perspectiva do Produto

Nosso sistema completo de aplicativo com API e banco de dados oferece uma solução abrangente e integrada para atender às necessidades do trabalho proposto.

### 2.2 Funcionalidades do Produto

- **Manutenção de Ativos:** Capacidade de adicionar, editar e remover ativos do sistema.
  
- **Manutenção de Dependências:** Gerenciar relações de dependência entre os ativos.
  
- **Listagem e Visualização:** Interface para visualizar ativos e suas dependências em formato tabular ou gráfico.
  
- **Menu de Usuário:** Menu interativo para acesso às diversas funcionalidades do sistema.
  
- **Persistência de Dados:** Salvar e recuperar dados utilizando Banco de Dados.

## 3. Requisitos Específicos

### 3.1 Requisitos Funcionais

**RF01 - Manutenção de Ativos**
- **RF01.1:** O sistema deve permitir a adição de novos ativos.
- **RF01.2:** O sistema deve permitir a edição de ativos existentes.
- **RF01.3:** O sistema deve permitir a remoção de ativos.

**RF02 - Manutenção de Dependências**
- **RF02.1:** O sistema deve permitir a criação de dependências entre ativos.
- **RF02.2:** !O sistema deve permitir a modificação de dependências existentes!.
- **RF02.3:** O sistema deve permitir a exclusão de dependências.

**RF03 - Listagem de Ativos e Dependências**
- **RF03.1:** O sistema deve listar todos os ativos e suas dependências.
- **RF03.2:** O sistema deve oferecer uma visualização gráfica das dependências.

**RF04 - Autenticação de Usuário**
- **RF04.1:** O sistema deve permitir que os usuários façam login fornecendo um nome de usuário e uma senha.

**RF05 - Validação de Credenciais**
- **RF05.1:** O sistema deve verificar se o nome de usuário e a senha fornecidos pelo usuário estão corretos

**RF06 - Menu de Usuário**
- **RF06.1:** O sistema deve oferecer um menu interativo para acesso às funcionalidades.

**RF07 - Persistência de Dados**
- **RF07.1:** O sistema deve armazenar os dados em um bando de dados.
- **RF07.2:** O sistema deve ler os dados do bando de dados ao iniciar.

### 3.2 Requisitos Não Funcionais

- **RNF01 - Usabilidade:** Interface simples e intuitiva.
- **RNF02 - Performance:** Respostas rápidas às solicitações do usuário.
- **RNF03 - Segurança:** Dados armazenados devem ser protegidos contra acessos não autorizados.

## Stack utilizada:
### Backend:
- **Python**
- **Flask**
### Persistência de dados:
- **MySQL**
- **Firebase**
### Versionamento:
- **Git**
### Virtualização:
- **Docker**
### APP:
- **Swift**
- **SwiftUI**

## Testes
### 1. Adição de Ativos e Dependências:
### Verificar se um novo ativo pode ser adicionado corretamente ao sistema.
- ### Passos: Apertar na opção 'Adicionar novo ativo' ou '+', preencher os detalhes do ativo e de suas dependências, apertar no botão 'Adicionar'.
- ### Resultado esperado: O ativo é adicionado no banco de dados.

### 2. Remoção de Ativos:
### Verificar se um ativo será removido do sistema junto de suas dependências.
- ### Passos: Arraste pro lado esquerdo o ativo de sua escolha e aperte na mensagem vermelha "Deletar".
- ### Resultado esperado: O ativo é removido junto de suas dependências do banco de dados.

### 3. Edição de Ativos:
### Verificar se a edição de dados de um ativo é feita corretamente no sistema.
- ### Passos: Clicar no ativo de sua escolha, clicar no ícone de edição (caneta), editar as informações, clicar no botão 'Salvar'.
- ### Resultado esperado: O ativo é editado com suas novas informações no banco de dados.

### 4. Listagem de Ativos:
### Verificar se os ativos do usuário estão sendo listados corretamente.
- ### Passos: Após realizar o login, você verá na página Home todos os seus ativos.
- ### Resultado esperado: Aparecer na página Home a listagem de todos os ativos do usuários com os seus respectivos detalhes e dependências.

### 5. Edição de Dependências:
### Verificar se a edição de dependências de um ativo é feita corretamente no sistema.
- ### Passos: Selecione o ativo que deseja editar as dependências, abra a seção de dependências do ativo, edite as dependências conforme necessário, salve as alterações.
- ### Resultado esperado: As dependências do ativo são editadas corretamente no sistema.

### 6. Cadastro de Usuário:
### Verificar se um novo usuário pode se cadastrar com sucesso no sistema.
- ### Passos: Acesse a página de cadastro do sistema, preencha todos os campos obrigatórios do formulário de cadastro, como nome de usuário, senha, e-mail, etc, aperte no botão de cadastro.
- ### Resultado esperado: O novo usuário é cadastrado com sucesso no banco de dados e redirecionado para a página principal do sistema.

### 7. Login com Sucesso:
### Verificar se um usuário pode fazer login com sucesso no sistema utilizando credenciais válidas.
- ### Passos: Acesse a página de login do sistema, insira o email e a senha corretos nos campos de login, aperte no botão de login.
- ### Resultado esperado: O usuário é redirecionado para a página principal do sistema após fazer login com sucesso.

### 8. Pesquisa de Ativo:
### Verificar se a pesquisa de ativos está funcionando corretamente no sistema.
- ### Passos: Acesse a página principal do sistema, localize o campo de pesquisa de ativos, insira o nome do ativo que deseja pesquisar.
- ### Resultado esperado: Os ativos que correspondem à pesquisa são exibidos corretamente na lista de ativos.


## Integrantes do Grupo:
- ### Pedro Nasser
- ### Igor Max
- ### Filipe Marra
- ### Brenno Lopes
- ### Lucas Dantas
- ### Caleb Medeiros
