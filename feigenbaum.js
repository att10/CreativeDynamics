function init() {
  Plotly.newPlot(chart, []);
}

function feigenbaum(start) {
  var aValues = math.range(2.002, 4, 0.002).toArray();
  var xValues = new Array(1000);
  for(i=0;i<1000;i++){
    var x = start;
    for(j=0;j<1000;j++) {
      x = logistic(aValues[i], x);
    }
    xValues[i] = x;
  }

  var chart = document.getElementById("chart");
  Plotly.plot(chart, [{
    x: aValues,
    y: xValues}]
  );
  if(start < 1) {
    setTimeout(function(){ feigenbaum(start+0.01) },1000);
  }
}

function logistic(a, x) {
  return a*x*(1-x);
}
