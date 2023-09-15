# Three Level Scale ou TLS

## Introdução

Este é o documento de Three Level Scale do projeto de arquitetura e desenho de software do grupo 1 referente ao aplicativo Amazon. A princípio, o documento tem a finalidade de definir quais requisitos serão priorizados pela equipe de desenvolvimento através das tabelas dos requisitos.

## Definição

**Three Level Scale** ou TLS é uma técnica de priorização que separa os requisitos em 3 quadrantes que são: baixa, média e alta prioridade. É importante salientar que esta técnica gera uma priorização subjetiva e imprecisa [1](#ancora1), isto ocorre devido às politicas das empresas e metas do negócio. Nesta técnica, as palavras principais são: "importância" e "urgência" já que ambas são os principais parâmetros para decidir em qual quadrante o requisito de encaixa. De acordo com Karl E. Wiegers, temos a seguinte definição de cada quadrante:

- **Alta prioridade**: São tanto importantes quanto urgentes, estes requisitos devem ser implementados o mais rápido o possível. </br>
- **Média prioridade**: Requisitos que são importantes, entretanto, não são urgentes.</br>
- **Baixa prioridade**: Não são nem importantes e nem urgentes.</br>

Em grandes projetos, queremos realizar a priorização de forma iterativa, então, caso seja observado que a quantidade de requisitos classificados em "alta prioridade" são muitos, pode-se fazer uma sub-priorização dos mesmos classificando-os em: Altissímo, Muito alto e Alto. Vale lembrar que para esta técnica funcionar, é importânte que a interdependência entre os requisitos sejam respeitadas.

## Metodologia

Para realizar a etapa de priorização, foi reunido todos os requisitos elicitados pelo projeto atavés das etapas de:

- [Brainstorming](./Brainstorm.md)
- [Entrevista](./Entrevista.md)
- [Mapa Mental](./MapaMental.md)
- [StoryBoard](./StoryBoard.md)

Em seguida, foi feito uma filtragem dos requisitos obtidos afim de que possa ter uma amostragem de dados mais consistente e menos repetitiva. Com a quantidade de requisitos classificados como altos na priorização final, foi feita uma segunda filtragem, afim de reclassificar os requisitos na categoria "alta".

## Resultados

A tabela 1 revela os resultados da priorização dos requisitos funcionais, e a tabela 2 mostra os dos requisitos não funcionais.

#### Requisitos funcionais:

| Identificador  | Requisito                                                                                                                                                       | Quadrante            |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| ENT01/BS05     | O comprador deve ser capaz de se cadastrar na plataforma                                                                                                        | Altíssima prioridade |
| ENT02          | O comprador deve ser capaz de fazer login na plataforma                                                                                                         | Altíssima prioridade |
| ENT03/BS23     | O comprador deve ser capaz de visualizar os produtos do site                                                                                                    | Altíssima prioridade |
| ENT04          | O comprador deve ser capaz de realizar a compra de produtos na plataforma                                                                                       | Altíssima prioridade |
| ENT05/MM14     | O comprador deve ser capaz de ter um carrinho                                                                                                                   | Altíssima prioridade |
| MM12/BS12/BS22 | O sistema deve possibilitar filtragem dos produtos                                                                                                              | Altíssima prioridade |
| MM13/BS32      | Ser possível realizar uma ordenação na lista de produtos exibidos atraves de uma palavra chave.                                                                 | Altíssima prioridade |
| BS06           | O sistema deve permitir alteração de informações do usuário                                                                                                     | Altíssima prioridade |
| BS09           | O sistema deve possibilitar a redefinição de senha                                                                                                              | Altíssima prioridade |
| BS11           | O sistema deve realizar confirmação em duas etapas da conta de usuário no processo de cadastro                                                                  | Altíssima prioridade |
| BS14           | O sistema deve disponibilizar informações detalhadas sobre os produtos (ficha técnica)                                                                          | Altíssima prioridade |
| BS21           | O sistema deve mostrar informações sobre status de um pedido                                                                                                    | Altíssima prioridade |
| BS26           | O sistema deve mostrar as avaliações de um produto                                                                                                              | Altíssima prioridade |
| BS29           | O sistema deve evidenciar os métodos de pagamento aceitos                                                                                                       | Altíssima prioridade |
| BS33           | O sistema deve permitir a visualização da disponibilidade de um produto                                                                                         | Altíssima prioridade |
| ENT07/MM05     | O comprador deve ser capaz de guardar alguns de seus registros econômicos                                                                                       | Alta prioridade      |
| SB04           | O sistema deve validar se o número e o e-mail do usuário esta correto.                                                                                          | Alta prioridade      |
| MM04           | O site fornecer recomendações de produtos                                                                                                                       | Alta prioridade      |
| BS08           | O sistema deve permitir o cadastro de múltiplos endereços de entrega                                                                                            | Alta prioridade      |
| BS15           | O sistema deve disponibilizar informações do carrinho                                                                                                           | Alta prioridade      |
| BS16           | O sistema deve disponibilizar dados do vendedor                                                                                                                 | Alta prioridade      |
| BS25           | O sistema deve mostrar o preço total do carrinho                                                                                                                | Alta prioridade      |
| BS28           | O sistema deve permitir a remoção de produtos do carrinho                                                                                                       | Alta prioridade      |
| BS31           | O sistema deve permitir a alteração das informações de entrega na tela do carrinho                                                                              | Alta prioridade      |
| BS34           | O sistema deve permitir que o usuário aplique cupons de desconto                                                                                                | Alta prioridade      |
| MM06/BS07      | O sistema deve permitir o cadastro de métodos de pagamento                                                                                                      | Média prioridade     |
| BS17           | O sistema deve permitir adicionar produtos à lista de desejos                                                                                                   | Média prioridade     |
| BS18           | O sistema deve permitir remover produtos da lista de desejos                                                                                                    | Média prioridade     |
| BS19           | O sistema deve mostrar se um produto é novo ou usado                                                                                                            | Média prioridade     |
| BS24           | O sistema deve permitir simulação de frete                                                                                                                      | Média prioridade     |
| MM15           | No carrinho de compras, ser exibidos os itens previamente adquiridos, tornando mais fácil a compra repetida de um item sem a necessidade de uma busca demorada. | Baixa prioridade     |
| BS13/BS20      | O sistema deve permitir a pesquisa e comparação do mesmo produto em lojas distintas                                                                             | Baixa prioridade     |
| BS27           | O sistema deve permitir a consulta do preço histórico de um produto                                                                                             | Baixa prioridade     |

<p align="center"> Tabela 1: Tabela de priorização TLE para os requisitos funcionais <br> Fonte: autor</p>

#### Requisitos não funcionais:

| Identificador        | Requisito                                                                                                | Quadrante            |
| -------------------- | -------------------------------------------------------------------------------------------------------- | -------------------- |
| ENT06/BS01/MM01/SB02 | O sistema deve ser seguro                                                                                | Altíssima prioridade |
| BS03                 | O sistema deve possuir interface fluida                                                                  | Altíssima prioridade |
| MM02                 | A empresa ser transparente na forma como está utilizando os dados do usuário.                            | Altíssima prioridade |
| ENT11                | O comprador deve ser capaz de localizar facilmente o tipo de pagamento que ele deseja realiza            | Altísisma prioridade |
| ENT08/BS02           | O Layout do site deve ser limpo e intuitívo                                                              | Alta prioridade      |
| ENT09                | O sistema deve me permitir realizar uma compra em até 10 minutos                                         | Alta prioridade      |
| SB03                 | O sistema deve fornecer campos obrigatórios para o cadastro, incluindo nome, endereço de e-mail e senha. | Alta prioridade      |
| BS04                 | O sistema deve ser veloz e eficiente                                                                     | Alta prioridade      |
| BS10                 | O sistema deve possibilitar autenticação em dois fatores                                                 | Alta prioridade      |
| MM03                 | O processo de login e cadastro na conta serem práticos                                                   | Alta prioridade      |
| SB01                 | O sistema deve exibir a opção "Criar conta" na página inicial.                                           | Alta prioridade      |
| ENT10                | O Layout da página deve ter uma paleta de cores que leva ao consumo                                      | Média prioridade     |

<p align="center"> Tabela 2: Tabela de priorização TLE para os requisitos não funcionais <br> Fonte: autor </p>

### Legenda:

- BS: Brainstorming
- ENT: Entrevista
- MM: Mapa Mental
- SB: Storyboard

## Bibliografia

> [1] First Things First: Prioritizing Requirements Karl E. Wiegers

> [2] K. Wiegers, “Five Requirements Prioritization Methods - Analyst’s corner - Medium,” Medium, Jun. 03, 2020. [https://medium.com/analysts-corner/five-requirements-prioritization-methods-86f4c5e0433e](https://medium.com/analysts-corner/five-requirements-prioritization-methods-86f4c5e0433e) (acessado Set. 14, 2023).

> ‌[3] Escala de Três Níveis - Simplenote. Github.io. Disponível em: <https://requisitos-de-software.github.io/2023.1-Simplenote/elicitacao/Prioriza%C3%A7%C3%A3o/ThreeLevelScale/>. Acesso em: 15 set. 2023.

‌

## Histórico de versão

| Versão |    Data    |         Descrição          | Autor  | Revisor |
| :----: | :--------: | :------------------------: | :----: | :-----: |
| `1.0`  | 14/09/2023 | Inicialização do documento |  Kauã  | Arthur  |
| `2.0`  | 15/09/2023 |   Migração para o MkDocs   | Arthur | Gabriel |
