var a = 1.4;
var b = 0.3;

function henon() {
  var xValues = new Array(10000);
  var yValues = new Array(10000);
  xValues[0] = 1;
  yValues[0] = 1;
  for(i=0;i<9999;i++) {
    xValues[i+1] = 1 - (a * xValues[i] * xValues[i]) + yValues[i];
    yValues[i+1] = b * xValues[i];
  }
  var data = [{
    x: xValues,
    y: yValues,
    type: 'scatter',
    mode: 'markers',
    marker: {
      size: 1,
      line: {
        width: 1
      }
    },
    showlegend:false
  }];

  // var layout = {
  //   yaxis: {range: [-.5, 0.5]},
  // }
  var chart = document.getElementById("chart");
  Plotly.plot(chart, data, {staticPlot: true});
  //Plotly.plot(chart, data, layout, {staticPlot: true});
}