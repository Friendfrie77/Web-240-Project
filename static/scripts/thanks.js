function redirect(){
     var span = document.getElementById('countdown');
     span.innerText = '10';
     var countdown = 10;

     setInterval(function(){
        if (countdown <= 0){
        window.location.replace("https://toebeansanctuary.azurewebsites.net/");
        } else {
            span.innerText = countdown;
        }
        countdown -= 1;
        }, 1000);
};
document.addEventListener('DOMContentLoaded', redirect());