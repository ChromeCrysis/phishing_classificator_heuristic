let url = window.location.href;

jQuery.support.cors = true;
$.ajax({
    type: 'GET',
    url: 'https://127.0.0.1:8000/tg/engine_execution?url='+url,
    dataType: 'json',
    cache:"false",
    success: function (data){
        if(int(data.score) >= 80){
            window.alert('Existe uma alta chance do site a qual está tentando acessar ser um phishing !!!')
        }
        
    },
    error: function (jxhr){window.alert(jxhr.responseText)}
});

(function (){
    activate();
})();

let active = null;

async function activate(){
    window.alert('oi')
    active = await getActive();
    if(!active) return;
}