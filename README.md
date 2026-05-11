**1- Título do jogo**
- Starfall: Last Shelter

**2- Descrição Geral**

*Desenvolvedores do jogo:*

- Rafael Victor Cabral de Azevedo
- Vinícius Morais de Araújo
- Pedro Lázaro de Araújo Dantas

Tipo de jogo: Shooter espacial / Arcade
Ambiente: Espaço sideral (campo aberto com zonas de combate)

*Ideia principal:*
- O jogador controla uma nave espacial em batalhas intensas contra uma frota inimiga misteriosa. Conforme avança, descobre que o conflito não é tão simples quanto parecia, culminando em uma batalha final contra uma grande nave central.

**3- Objetivo do Jogo**

- O objetivo do jogador é destruir as naves inimigas e, ao final, derrotar a nave principal (nave mãe).

- A meta principal é Eliminar inimigos ao longo do percurso, Sobreviver aos ataques Alcançar e destruir a Nave Mãe, e assim, descobrindo o final da lore


**4- Personagem Principal**

*Quem é:*
- Joseff, Um piloto alienígina solitário sobrevivente da destruição do seu planeta.

*Movimentação:*

- Movimento livre em 2D (horizontal e vertical)
- Pode se deslocar em todas as direções

*Atributos:*

- Vida (começa com 3 vidas)
- Velocidade
- Pontuação
- Tipo de tiro
- upgrades


**5- Inimigos e Obstáculos**

*Tipos de inimigos*

- Naves básicas (ataque direto)
- Nave Mãe(Inimigo final)

*Comportamento da nave de defesa:*

- Nave tenta eliminar o user com tiros de raio lazer ou se jogando nele. Formação em grupo. De acordo com as fases, o comportamento muda, as naves fazem um bloqueio Bloqueio de caminho (principal comportamento narrativo) e ficam mais desesperadas

*Comportamento da nave mãe:*

- Nave tenta eliminar e fugir do player. nave única com muita vida e tiros diferentes.


*Colisão:*

- O jogador perde vida ao colidir com outras naves ou ser atingido por projéteis de outras naves
- Inimigos podem ser destruídos ao receber dano  de tiro

**6- Cenário (Mapa)**

*Ambiente:*
- Espaço cideral aberto com progressão linear

*Elementos do mapa:*

- Área de movimentação livre
- Limites do mapa
- Zona da nave central

*Distribuição:

- Inimigos aparecem ao longo do percurso
- A nave principal está localizada no começo

**7- Sistema de Pontuação**

*Como ganhar pontos:*

- Destruir inimigos
- Passar de fase

*Valores:*

- Nave defensiva = 15 pontos
- passar de fase = 400 pontos

**8- Sistema de Vida**

*Vida inicial:*
- 3 corações, mas pode aumentar dependendo de upgrades

*Perda de vida:*
- Ao ser atingido por projéteis
- Ao colidir com inimigos

*Game Over:*
- Quando a vida chega a zero → Game Over


**9- Controles**

- W / ↑ → mover para cima
- S / ↓ → mover para baixo
- A / ← → mover para esquerda
- D / → → mover para direita
- Espaço → atirar
- ESC → pausa

**10- Fluxo do Jogo**

*Inicio:*
- O jogo inicia com o jogador controlando a nave, Inimigos começam a aparecer, se o jogador vence, pontua, se for atingido por um projétil ou por uma nave, perde uma de suas 3 vidas. Comportamento dos inimigos muda (mais defensivo) conforme o jogador passa de fase.

- Condição de vitória: destruir as naves inimigas e avançar. Condição de derrota: Jogador perder suas 3 vidas

*Condições na fase final*
- Na fase final, o Jogador encontra a nave mãe e Batalha final acontece, se o jogador vence, uma cena final aparece e o jogador zera o jogo, se for atingido por um projétil, perde uma de suas 3 vidas e se for atingido por um tiro carregado da nave mãe, perde 2 vidas.

- Condição de vitória: destruir a nave mãe. Condição de derrota: Jogador perder suas 3 vidas

**11 -Regras do Jogo**

- Não atravessar limites do mapa
- Colidir com inimigos causa dano
- Colidir com projéteis causa dano
- Inimigos vivos bloqueiam o progresso
- O jogador deve avançar para completar o jogo

**12- Estrutura do projeto**

- /Starfall-Last-Shelter
- │── main.py
- │── player.py
- │── enemy.py
- │── boss.py
- │── map.py
- │── projectile.py
- │── assets/
- │   ├── sprites/
- │   ├── sounds/
- │── README.md

**13- Funcionalidades Mínimas**

- Movimentação do jogador
- Sistema de tiro
- Inimigos com comportamento básico
- Sistema de vida
- Colisão
- Pontuação

**15- Melhorias Futuras**

- Diferentes tipos de armas
- Sistema de upgrades
- Animações mais detalhadas
- Cutscenes para contar a história
- Sistema de níveis/fases
- Criação de um "especial" pra o jogador, que carrega com o tempo


