# Desafio-IA-Berkeley-CS188.1x-
Um conjunto de desafios para resolver problemas em um ambiente simulado do jogo Pacman, usando Inteligência Artificial



<h2>Encontrando comida em um ponto fixo usando algoritmos de busca</h2>

<h3>Passo 1 (2 pontos) Implemente o algoritmo de busca em profundidade (DFS)</h3>

<b>A ordem de exploração foi de acordo com o esperado?</b>
<i>Sim</i>

<b>Pacman realmente passa por todos os estados explorados no seu caminho para o objetivo?</b>
<i>Não, nem todos os estados explorados levam ao objetivo</i>

<b>Essa é uma solução ótima? Senão, o que a busca em profundidade está fazendo de errado?</b>
<i>Não é, o algoritimo é convluido assim que encontra um caminho que o leve até o objetivo</i>

<h3>Passo 2 (2 pontos) Implemente o algoritmo de busca em extensão (BFS) </h3>

<b>A busca BFS encontra a solução ótima? </b>
<i>Sim</i>

<h3>Passo 3 (2 pontos) Implemente o algoritmo de busca de custo uniforme </h3>

<h3>Passo 4 (2 pontos) Implemente a busca A* </h3>

<b>A O que acontece em openMaze para as várias estratégias de busca? </b>
<i>Em DFS ele não vai diretamente ao objetivo, e sim preenchendo todas as linhas até ele, em BFS, Algoritimo de Custo e A*, o pecman vai diretamente ao objetico em deslocamento manhattan</i>
