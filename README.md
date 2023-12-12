<h2 align="center"> Calendário dos feriado em 2024 em <img align="center" alt="Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"></h2>

<p>O código Python apresenta um script que utiliza a biblioteca matplotlib para criar um gráfico de linha, mostrando a distribuição mensal de feriados ao longo de um ano específico.
O script utiliza a biblioteca holidays para obter informações sobre os feriados brasileiros.</p>

<h3 align="center">⭐Detalhes do Código:⭐</h3>

<h4> Bibliotecas Utilizadas:</h4>

<p>➡️matplotlib.pyplot: Usada para criar visualizações gráficas, neste caso, um gráfico de linha.</p>
<p>➡️holidays: Utilizada para obter informações sobre feriados brasileiros.</p>
<p>➡️collections.Counter: Usada para contar a frequência de feriados por mês.</p>
<p>➡️datetime.date: Utilizada para manipulação de datas.</p>

<h4> Função plot_holidays(year):</h4>

<p>➡️Recebe um ano como parâmetro.</p>
<p>➡️Obtém os feriados brasileiros para o ano especificado.</p>
<p>➡️Filtra apenas os feriados que ocorrem no ano determinado.</p>
<p>➡️Agrupa feriados por mês, contando sua ocorrência.</p>
<p>➡️Cria um gráfico de linha utilizando matplotlib.pyplot.</p>
<p>➡️Adiciona rótulos e título ao gráfico.</p>
<p>➡️Ajusta o tamanho da fonte dos meses no eixo x.</p>
<p>➡️Exibe o gráfico na tela.</p>
  
<h4> Configuração do Gráfico:</h4>

<p>➡️O gráfico exibe o número de feriados no eixo y e os meses no eixo x.</p>
<p>➡️Cada ponto no gráfico representa um mês e a quantidade de feriados nesse mês.</p>
<p>➡️Utiliza marcadores vermelhos ('o') e uma linha de ligação para facilitar a visualização.</p>
  
<h4> Execução do Script:</h4>

<p>➡️Substitua o ano desejado (no exemplo, 2024) na variável ano_desejado.</p>
<p>➡️Executa a função plot_holidays com o ano especificado.</p>
<p>➡️Salva o gráfico como uma imagem chamada 'calendario.png' (ou outro formato desejado).</p>
  
<h4> Instruções para Execução:</h4>

<p>➡️Execute o script no ambiente Python desejado (terminal, VSCode, Jupyter, etc.).</p>
<p>➡️Certifique-se de ter as bibliotecas matplotlib e holidays instaladas.</p>
<p>➡️O gráfico será exibido na tela e, opcionalmente, salvo como uma imagem.</p>
  
<p>Este código oferece uma maneira simples de visualizar a distribuição dos feriados brasileiros ao longo de um ano e pode ser útil para análises temporais.</p>


<div align="center">
<img  src="calendario.png" alt="grafico">
</div>
