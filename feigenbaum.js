function init() {
  var ctx = document.getElementById("canvas").getContext('2d');
  let chart = new Chart(ctx, {
    type: 'line',
    data: {
        datasets: [{
            data: [0, 20, 40, 50],
        }, {
            data: testData
        }],
        labels: ['1', '2', '3', '4']
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            yAxes: [{
                ticks: {
                    suggestedMin: 10,
                    suggestedMax: 30
                }
            }]
        }
    }
  });
}

var testData = [10, 20, 30, 40, 50];
function feigenbaum() {
  var data = new Array(100);
}
