var numero = 6

console.log("Triangulo de asteriscos:")

for (var i = 1; i <= numero; i++) {
  var linea = "";

  for (var j = 1; j <= i; j++) {
    linea += "*";
  }

  console.log(linea);
}
var numero = 8
var suma = 0;

for (var i = 0; i <= numero; i++) {
  suma += i;
}

console.log("Los numeros enteros de 0 a " + numero + " suman " + suma);

var numero1 = 3
var numero2 = 5
var numero3 = 7
var numero4 = 2

var suma = numero1 + numero2 + numero3 + numero4;
var media = suma / 4;

console.log("La media aritmetica de los 4 numeros ingresados es: " + media);