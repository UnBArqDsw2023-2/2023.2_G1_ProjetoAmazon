# Diagrama de Estados

## Introdução

A Linguagem de modelagem unificada (UML) foi criada para estabelecer uma linguagem de modelagem visual comum, semanticamente e sintaticamente rica, para arquitetura, design e implementação de sistemas de software complexos, tanto estruturalmente quanto para comportamentos [¹](#ancora1). Temos diversos tipos de diagramas estruturais UML, sendo assim, este artefato tem como objetivo abordar a diagramação UML de _estados_ afim de promover uma melhor organização para o código do projeto.

## Diagrama de estados

É um diagrama comportamental e dinâmico. O diagrama de estados consiste em estados, transições, eventos e atividades. Eles são importantes na modelagem de comportamentos de interface,
classe ou colaboração. Ele enfatiza a ordem dos eventos do comportamento de um objeto.
Esse tipo de diagrama tem diversos usos, entre eles:

- Descrever objetos orientados a eventos em um sistema reativo;
- Ilustrar cenários de caso de uso em um contexto de negócios;
- Descrever como um objeto se move por vários estados em seu tempo vida;
- Mostrar o comportamento geral de uma máquina de estados ou o comportamento de um conjunto relacionado de máquinas de estados.

Como componentes básicos podemos citar Estados; Primeiro estado; Transições; Ações de estado; Estado composto; Pseudoestado de escolha; Evento; Ponto de saída; Proteção; Subestado; Exterminador; Comportamento transicional; Acionador.

## Metodologia

Para a confecção do diagrama de estados, os membros responsáveis decidiram dividir o diagrama em 4 temas:

1 - Cadastro: Relativo a parte de cadastro no aplicativo,após clicar em "Quero me cadastrar" ou "Cadastrar-se".
2 - Login: Relativo a parte de entrada no aplicativo, ao clicar em "Login".
3 - Pagamento: Relativo a parte em que o usuário clica em pagar o seu produto até à finalização do pagamento.
4 - Produto: Relativo a parte de inicio do aplicativo até o pagamento.

Oque resultou na seguinte configuração:

<center>

| Diagrama  | Encarregado |
| --------- | ----------- |
| Cadastro  | Ana Beatriz |
| Login     | Kauã        |
| Pagamento | Mylena      |
| Produto   | Kauã        |

</center>

<div style="text-align: center">
<p> Tabela 1: Relação diagrama-encarregado.Fonte: autor, 2023.</p>
</div>

Com isso, os responsáveis começaram os trabalhos no dia 01/10/2023. Foi decidido que o diagrama seria elaborado na plataforma [Lucidchart](https://lucid.app/lucidchart/f0a2748a-4b6a-4d24-b1f1-d8f17136f0d4/edit?viewport_loc=-11%2C-10%2C1993%2C759%2CrP5zvCyaz_BT&invitationId=inv_edea634f-f5ca-4f8c-90b1-e977012aa695).

## Diagramas

Para o bom entendimento dos diagramas, é importante ressaltar que durante a confecção dos mesmos, o grupo teve problemas relacionados à ferramenta de produção. Sendo assim, ressalta-se que:

- O diagrama de produto está relacionado com o diagrama de pagamento.
- O diagrama de pagamento está relacionado com o diagrama de cadastro e login.
- O diagrama de cadastro está relacionado com diagrama de login.

Seguem as versões:

### Primeira versão

As imagens 1 a 4 mostram as primeiras versões dos diagramas de estados que serão abordados neste documento. Seguem os mesmos:

#### Cadastro

<center>
    <img src="./EstadosCadastro.png" style="width:60vw"/>
    <p> Imagem 1: Diagrama de estados de cadastro, primeira versão. Fonte: Ana Beatriz</p> 
</center>

#### Login

<center>
    <img src="./EstadosLoginV1.png" style="width:60vw"/>
    <p> Imagem 2: Diagrama de estados de login, primeira versão. Fonte: Kauã</p> 
</center>

#### Pagamento

<center>
    <img src="./estados_pagamento_primeira.jpg" style="width:60vw"/>
    <p> Imagem 3: Diagrama de estados do pagamento, primeira versão. Fonte: Mylena</p> 
</center>

#### Produto

<center>
    <img src="./EstadosProdV1.png" style="width:60vw"/>
    <p> Imagem 4: Diagrama de estados de produto, primeira versão. Fonte: Kauã</p> 
</center>

### Versão final

As imagens 5 a 8 mostram as versões finais dos diagramas de estados que serão abordados neste documento. Seguem os mesmos:

#### Cadastro

<center>
    <img src="./EstadosCadastro.png" style="width:60vw"/>
    <p> Imagem 5: Diagrama de estados de cadastro, versão final. Fonte: Ana Beatriz</p> 
</center>

#### Login

<center>
    <img src="./EstadosLoginV1.png" style="width:60vw"/>
    <p> Imagem 6: Diagrama de estados de login, versão final. Fonte: Kauã</p> 
</center>

#### Pagamento

<center>
    <img src="./estados_pagamento.png" style="width:60vw"/>
    <p> Imagem 7: Diagrama de estados de pagamento, versão final. Fonte: Mylena</p> 
</center>

#### Produto

<center>
    <img src="./EstadosProdutoVF.png" style="width:60vw"/>
    <p> Imagem 8: Diagrama de estados de produto, versão final. Fonte: Kauã</p> 
</center>

## Bibliografia

> [1] O que é um diagrama UML? Lucidchart. Disponível em: <https://www.lucidchart.com/pages/pt/o-que-e-uml>. Acesso em: 01 out. 2023.
>
> [2] O que é diagrama UML e como fazer? Veja tipos, modelos e exemplos. https://miro.com/. Disponível em: <https://miro.com/pt/diagrama/o-que-e-uml/>. Acesso em: 01 out. 2023.
>
> [3] Tutorial sobre diagramas de estados UML. Lucidchart. Disponível em: <https://www.lucidchart.com/pages/pt/o-que-e-diagrama-de-maquina-de-estados-uml>. Acesso em: 01 out. 2023.
>
> [4] All you need to know about state diagrams. Disponível em: <https://www.visual-paradigm.com/guide/uml-unified-modeling-language/about-state-diagrams/>. Acesso em: 01 out. 2023.
>
> [5] UML 2 Tutorial - State Machine Diagram. Disponível em: <https://sparxsystems.com/resources/tutorials/uml2/state-diagram.html>. Acesso em: 01 out. 2023.
>
> [6] .NET - Apresentando o padrão Repository. Macoratti.net. Disponível em: <https://www.macoratti.net/11/10/net_pr1.htm#:~:text=O%20que%20%C3%A9%20o%20padr%C3%A3o,camada%20de%20neg%C3%B3cios%20(BLL).>. Acesso em: 01 out. 2023.
>
> [7] UML state machine diagrams. Disponível em: <https://www.uml-diagrams.org/state-machine-diagrams.html> . Acesso em: 01 out. 2023

‌

## Histórico de versão

| Versão |    Data    |         Descrição          |       Autor        | Revisor |
| :----: | :--------: | :------------------------: | :----------------: | :-----: |
| `1.1`  | 01/10/2023 |    Criação do documento    | Ana, Kauã e Mylena | Beatriz |
| `1.2`  | 05/10/2023 | Adição de alguns diagramas |        Kauã        | Beatriz |
| `1.3`  | 07/10/2023 |   Adição de observações    |        Kauã        | Beatriz |
| `1.4`  | 07/10/2023 |  Continuação do documento  |        Kauã        | Beatriz |
| `1.5`  | 07/10/2023 |    Adição de diagramas     |       Mylena       | Beatriz |
| `1.6`  | 07/10/2023 |  Finalização do documento  |     Ana e Kauã     | Beatriz |
| `1.7`  | 09/10/2023 |  Revisão antes da entrega  |       Arthur       | Arthur  |
