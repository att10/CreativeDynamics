function init() {
  Plotly.newPlot(chart, [], {showLegend: false}, {staticPlot: true} );
}

const w = 1920;
const h = 1000;

function julia() {
  var xValues = math.range(-1, 1, 0.02).toArray();
  var yValues = math.range(-1, 1, 0.02).toArray();
  var reValues = new Array(20000);
  var imValues = new Array(20000);
  var cReal = document.getElementById("alpha").value;
  var cImag = document.getElementById("beta").value;
  var real, imag, z, rTemp, iTemp;
  var count = 0;
  for(y=0;y<h;y++) {
    for(x=0;x<w;x++) {
      real = 1.5 * (x-w/2) / (0.5*w) + cReal;
      imag = (y-h/2) / (0.5*h) + cImag;
      var k;
      var iter = 0;
      var max = 250;
      while((((real*real) + (imag*imag)) < 4) && iter < max) {
        rTemp = real;
        iTemp = imag;

        real = (rTemp*rTemp) - (iTemp*iTemp) + cReal;
        imag = 2 * rTemp * iTemp + cImag;

        iter = iter + 1;
      }
      //alert(reValues);
      reValues[count] = real;
      imValues[count] = imag;
      count++;

    }
  }


  var data = [{
    x: reValues,
    y: imValues,
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

}

function getZ(x, y) {
  return math.complex(x,y)
}
