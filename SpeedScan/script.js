document.addEventListener('DOMContentLoaded', function(object){

    console.log(chrome)
    let text = window.location.href;
    document.querySelector("#result").innerHTML = text;

    document.querySelector('#btn').addEventListener('click', function(){
        console.log(window.location)
        let text = window.location.href;
        document.querySelector("#result").innerHTML = text;
    })

})