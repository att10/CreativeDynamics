const w = 400;
const h = 300;

function julia() {
  var reValues = new Array(20000);
  var imValues = new Array(20000);
  var cReal = document.getElementById("alpha").value;
  var cImag = document.getElementById("beta").value;
  var real, imag, rTemp, iTemp;
  var count = 0;
  var counter = document.getElementById("counter");
  for(y=0;y<h;y++) {
    for(x=0;x<w;x++) {
      real = 1.5 * (x-w/2) / (0.5*w);
      imag = (y-h/2) / (0.5*h);

      var iter = 0;
      var max = 255;
      while((((real*real) + (imag*imag)) < 4) && iter < max) {
        rTemp = real;
        iTemp = imag;

        real = (rTemp*rTemp) - (iTemp*iTemp) + cReal;
        imag = 2 * rTemp * iTemp + cImag;

        iter = iter + 1;
      }

      if(iter < max) {
        drawPixel(x, y,iter/2, 0, 100, 255);
      } else {
        drawPixel(x, y,0, 0, 0, 255);
      }


      //alert(x);

    }
  }
  updateCanvas();
}

var canvasData, ctx, canvasWidth;

function init() {
  var canvas = document.getElementById("myCanvas");
  canvasWidth = canvas.width;
  var canvasHeight = canvas.height;
  ctx = canvas.getContext('2d');
  canvasData = ctx.getImageData(0, 0, canvasWidth, canvasHeight);
  julia();
}

// That's how you define the value of a pixel //
function drawPixel (x, y, r, g, b, a) {
    var index = (x + y * canvasWidth) * 4;

    canvasData.data[index + 0] = r;
    canvasData.data[index + 1] = g;
    canvasData.data[index + 2] = b;
    canvasData.data[index + 3] = a;
}

// That's how you update the canvas, so that your //
// modification are taken in consideration //
function updateCanvas() {
    ctx.putImageData(canvasData, 0, 0);
}
