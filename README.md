# Asset Management API🖥️


## Esse aplicativo de gerenciamento de ativos é uma ferramenta projetada para ajudar empresas e indivíduos a acompanhar, monitorar e gerenciar seus ativos de forma eficiente. Isso inclui uma variedade de itens, como equipamentos, propriedades, veículos e investimentos financeiros.

## 1. Introdução

### 1.1 Propósito

Este documento tem como objetivo detalhar os requisitos para o sistema de gerenciamento de ativos de TI, proporcionando uma visão clara das funcionalidades e estrutura necessárias para a implementação do sistema.

### 1.2 Escopo do Projeto

O sistema permitirá a manutenção de ativos de TI, gerenciamento das dependências entre os ativos, e fornecerá uma interface para a listagem e visualização das relações entre os ativos. O sistema contará com um menu de opções para facilitar a navegação do usuário e persistência dos dados em formato de arquivo.

## 2. Descrição Geral

### 2.1 Perspectiva do Produto

O sistema funcionará de forma independente e não integrará inicialmente com outros sistemas. Será uma aplicação standalone com interface de linha de comando (CLI).

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

**RF04 - Menu de Usuário**
- **RF04.1:** O sistema deve oferecer um menu interativo para acesso às funcionalidades.

**RF05 - Persistência de Dados**
- **RF05.1:** O sistema deve armazenar os dados em um bando de dados.
- **RF05.2:** O sistema deve ler os dados do bando de dados ao iniciar.

### 3.2 Requisitos Não Funcionais

- **RNF01 - Usabilidade:** Interface simples e intuitiva.
- **RNF02 - Performance:** Respostas rápidas às solicitações do usuário.
- **RNF03 - Segurança:** Dados armazenados devem ser protegidos contra acessos não autorizados.



## Testes
### 1. Adição de Ativos e Dependências:
**Verificar se um novo ativo pode ser adicionado corretamente ao sistema.
- ### Passos: Apertar na opção 'Adicionar novo ativo' ou '+', preencher os detalhes do ativo e de suas dependências, apertar no botão 'Adicionar'.
