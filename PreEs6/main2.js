// function Pi(){ 
//   var regresar = (Math.PI).toFixed(2); 
//   return regresar;  
// }
// var result = Pi()
// console.log(  result   )
// Pi()


// function sacarIva(precio, ivaEntrada){
//   const ivaFunction = ivaEntrada || 18
//   var coniva = (precio + precio*ivaFunction/100);
//   return coniva;
// }
// var precio = 100
// var iva = 15

// console.log(sacarIva(100))
// console.log(sacarIva(100,15))
// function VoltearTexto(Aba){
//     var textoAlReves = ""

//     for(index = Aba.length - 1; index > -1; index--){
//         textoAlReves = textoAlReves + Aba[index]
//     }
//     return textoAlReves
// }
// console.log(VoltearTexto("casaNueva") + VoltearTexto("Viejo"));
function generarNumeroAleatorio() {
    return Math.floor(Math.random() * 100) + 1;
  }
  
  var numeroAleatorio = generarNumeroAleatorio();
  console.log(numeroAleatorio);



  function generarNumerosAleatorios() {
    var numeros = [];
  
    while (numeros.length < 100) {
      var numero = Math.floor(Math.random() * 1000) + 1;
  
      if (!numeros.includes(numero)) {
        numeros.push(numero);
      }
    }
  
    return numeros;
  }
  
  var numerosAleatorios = generarNumerosAleatorios();
  
  numerosAleatorios.forEach(function(numero) {
    console.log(numero);
  });
  generarNumerosAleatorios()
