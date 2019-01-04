function init() {
  Plotly.newPlot(chart, [], {showLegend: false}, {staticPlot: true} );
}

function feigenbaum(start) {
  document.getElementById("graph").style.visibility = "hidden";
  var aValues = math.range(2.503, 4, 0.0015).toArray();
  var xValues = new Array(1000);
  for(i=0;i<1000;i++){
    var x = start;
    for(j=0;j<1000;j++) {
      x = logistic(aValues[i], x);
    }
    xValues[i] = x;
  }

  var data = [{
    x: aValues,
    y: xValues,
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

  var chart = document.getElementById("chart");
  Plotly.plot(chart, data, {staticPlot: true});
  if(start < 1) {
    document.getElementById("iter").innerHTML = "&nbsp Iterations: " + Math.round(start * 100);
    setTimeout(function(){ feigenbaum(start+0.01) },1000);
  }
}

function logistic(a, x) {
  return a*x*(1-x);
}
