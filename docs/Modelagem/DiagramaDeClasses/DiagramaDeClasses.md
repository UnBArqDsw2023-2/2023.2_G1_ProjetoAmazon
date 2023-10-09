# Diagrama de Classes

## Introdução

O Diagrama de Classes é uma ferramenta fundamental na UML (Unified Modeling Language) que oferece uma perspectiva 
abrangente da estrutura de um sistema orientado a objetos. Neste diagrama, são apresentados em detalhes os componentes 
essenciais, como classes e interfaces, revelando suas características distintivas, limitações e conexões cruciais, como 
associações, generalizações e dependências, entre outros elementos [¹](#ancora1).

## Metodologia

Nesta etapa foi desenvolvido um diagrama de classes baseado no escopo do projeto (**Perfil Comprador e 
fluxos do cadastro até visualização/compra/pagamento de produtos na Amazon.**). Com principal objetivo de
facilitar o desenvolvimento de um sistema ao representar visualmente as classes, seus atributos, métodos e
relacionamentos.

Para a criação do diagrama de classes, foi selecionada a plataforma [Lucidchart](https://www.lucidchart.com/) devido à 
sua facilidade de uso e à capacidade de colaboração em tempo real que oferece.  

Para iniciar o processo de criação do diagrama, os membros responsáveis, [Ana Beatriz](https://github.com/ananorberto) e
[Beatriz](https://github.com/Beatrizvn), realizaram uma análise léxica e lógica dos requisitos previamente 
elicitados, então, foi separado uma lista [³](#ancora3) de possíveis classes para o projeto. A seleção dessas classes foi baseada em 
sua relevância para o sistema, importância para os objetivos do projeto e dependências entre elas. Essa lista serviu 
como base para a criação do diagrama de classes.

É importante destacar que a tomada de decisões cruciais e discussões relevantes para a elaboração do diagrama ([versão 1.0](#versão-10)) 
ocorreram durante uma reunião de colaboração. Esta reunião foi realizada via Discord no dia 28/09/2023 às 16 horas. A escolha 
desta plataforma se deu pela familiaridade e afinidade da equipe durante os processos de elaboração de trabalhos e 
projetos acadêmicos. 

Além disso, identificamos a necessidade de aprimorar o Diagrama de Classes com base em feedbacks relevantes, que incluíram 
sugestões valiosas da professora. Portanto, decidimos desenvolver uma [versão 2.0](#versão-20) do Diagrama de Classes. Essas modificações 
foram implementadas na mesma plataforma, visando enriquecer a modelagem e torná-la ainda mais coerente e fiel ao escopo do projeto.

## Diagrama de Classes

### Versão 1.0

Na versão 1.0 do Diagrama de Classes, apresentamos uma representação inicial da estrutura do sistema, enfocando o escopo do projeto. 
Nesta versão, as classes, atributos e relacionamentos foram esboçados de forma abrangente e precisa, buscando fornecer uma visão geral 
do sistema, embora sujeitos a alterações.

<center>
    <img src="Classe UML_V2.png"/>
    <p> Figura 1 (Fonte: Autor, 2023).</a></p> 
</center>

### Versão 2.0

Na versão 2.0 do Diagrama de Classes, ocorreram melhorias significativas seguindo os feedbacks da professora, 
visando aprimorar a modelagem e torná-la mais fiel ao escopo do projeto. As modificações incluíram ajustes nas 
direções e multiplicidades das relações entre as classes, a adição de métodos para representar o comportamento 
das classes e a introdução de novas classes, como "Carrinho" e um elemento `<<enum>>` chamado "Status" para monitorar 
o status dos pedidos.

<center>
    <img src="Classe UML - Amazon_v2.1.png"/>
    <p> Figura 2 (Fonte: Autor, 2023).</a></p> 
</center>


## Referências

> [1] UML Class and Object Diagrams Overview. Disponivel em: [uml-diagrams.org](https://www.uml-diagrams.org/class-diagrams-overview.html). Acesso em 28 de set. de 2023.
>
> [2] SLIDE AULA - MODELAGEM UML ESTÁTICA. Prof. Profa. Milene Serrano. Disponivel em: [Aprender3](https://aprender3.unb.br/pluginfile.php/2649429/mod_label/intro/Arquitetura%20e%20Desenho%20de%20Software%20-%20Aula%20Modelagem%20UML%20Est%C3%A1tica%20-%20Profa.%20Milene.pdf). Acesso em 28 de set. de 2023.
>
> [3] PROBLEMA DE BIOS. UML na pratica - Diagramas de Classes. YouTube, 24 nov. 2020. Disponível em: <https://www.youtube.com/watch?v=srA9jiCxfj4>. Acesso em:  28 set. 2023
>
‌

## Histórico de versão

| Versão | Data       | Descrição                            | Autor(es)     |  Revisor(es) |
| ------ | ---------- | ------------------------------------ | ------------- | ------------ |
| `1.0`  | 28/09/2023 | Iniciando o documento                | Beatriz e Ana | Kauã, Mylena |
| `1.1`  | 28/09/2023 | Adicionando versão 1                 | Ana e Beatriz | Kauã, Mylena |
| `1.2`  | 02/10/2023 | Adicionando Metodologia              | Ana           | Beatriz      |
| `1.3`  | 05/10/2023 | Corrigindo erros de ortografia na UML| Beatriz       | Ana          |
| `1.4`  | 08/10/2023 | Adicionando versão 2 do UML          | Ana           | Beatriz, Kauã|



