bandera = true;
setInterval(function(){

    if(bandera){
        document.getElementById('title').style.backgroundColor = "red";
        bandera = false;
    } else {
        document.getElementById('title').style.backgroundColor = "blue";
        bandera = true;

    }
},1000)

setTimeout(function(){
    window.alert("Ya salte")
},5000)