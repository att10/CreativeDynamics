var xValues, aValues, data;
var count = 0;
var oldCount = 0;

function init() {
  Plotly.newPlot(chart, [], {showLegend: false}, {staticPlot: true} );
  aValues = math.range(2.8, 4, 0.0012).toArray();
  aValues = aValues.concat(aValues);
}


function feigenbaum(start) {
  document.getElementById("graph0").style.visibility = "hidden";
  document.getElementById("graph1").style.visibility = "hidden";
  xValues = new Array(2000);
  var x;
  var currX = start;
  for(i=0;i<2000;i++){
    if(i==999){
      start += 0.02;
    }
    x = start;
    for(j=0;j<1000;j++) {
      x = logistic(aValues[i], x);
    }
    xValues[i] = x;
  }

  data = [{
    x: aValues,
    y: xValues,
    type: 'scatter',
    mode: 'markers',
    marker: {
      opacity: 0.4,
      size: 1,
      line: {
        width: 1
      }
    },
    showlegend:false
  }];

  var chart = document.getElementById("chart");
  Plotly.plot(chart, data, {staticPlot: true});
  if(count < 45) {
    count += 2;
    setTimeout(function(){ feigenbaum(start+0.02) },100);
  }
}

function logistic(a, x) {
  return a*x*(1-x);
}
