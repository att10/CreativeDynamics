var a = 1.4;
var b = 0.3;

function start() {
  henon(1,1,10000)
  henon(0.5,0.5, 50);
  henon(0.50000001,0.50000001, 50);

}

function henon(x,y, n) {
  document.getElementById("graph1").style.visibility = "hidden";
  var xValues = new Array(100);
  var yValues = new Array(100);
  xValues[0] = x;
  yValues[0] = y;
  for(i=0;i<n;i++) {
    xValues[i+1] = 1 - (a * xValues[i] * xValues[i]) + yValues[i];
    yValues[i+1] = b * xValues[i];
  }
  var size = 5;
  var color = "rgb(0, 0, 255)";
  if(x == 1) {
    color = "rgb(255, 0, 0)";
    size = 1;
  } else if (x == 0.5) {
    color = "rgb(0, 255, 0)";
  }
  var data = [{
    x: xValues,
    y: yValues,
    type: 'scatter',
    mode: 'markers',
    marker: {
      size: size,
      color: color,
      line: {
        width: .8
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
