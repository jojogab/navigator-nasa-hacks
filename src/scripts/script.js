fetch('src/chart_data.json')
  .then(response => {
      console.log(response);
      return response.json();
  })
  .then(data => {
      Plotly.newPlot('chart', data.data, data.layout);
  })
  .catch(error => {
      console.error('Erro ao carregar o gráfico:', error);
  });