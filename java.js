//Variables temporales en lo que queda la base de datos
var screenname = ["Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus",
                  "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus"];
var username = ["@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus",
                "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus final"];
var timestamp = ["2h", "2h", "2h", "2h", "2h", "2h", "2h", "2h", "2h", "2h",
                 "2h", "2h", "2h", "2h", "2h", "2h", "2h", "2h", "2h", "2h"];
var tweet = ["hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola",
             "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola final"];


//Función que imporime los tweets
window.onload = function() {
    for(i=0;i<10;i++) {
        var post = "<div class=\"d-flex p-3 border-bottom\"><img src=\"https://mdbcdn.b-cdn.net/img/Photos/Avatars/img (29).webp\" class=\"rounded-circle\" height=\"50\" loading=\"lazy\"/></div>";
        post += "<div><h6 class=\"text-body\">";
        post += screenname[i];
        post += "</h6><span class=\"small text-muted font-weight-normal\"> • </span><span class=\"small text-muted font-weight-normal\">";
        post += username[i];
        post += "</span><span><i class=\"fas fa-angle-down float-end\"></i></span><span class=\"small text-muted font-weight-normal\">";
        post += timestamp[i];
        post += "</span><p style=\"line-height: 1.2;\">";
        post += tweet[i];
        post += "</p></div>";
        const div = document.getElementById('divprint');
        div.insertAdjacentHTML('beforeend', post);
    }
}

function ImprimeTweets(number) {
    for(i=number;i<(number+10);i++) {
        document.getElementById('ScreenName').innerHTML = screenname[i];
        document.getElementById('UserName').innerHTML   = username[i];
        document.getElementById('TimeStamp').innerHTML = timestamp[i];
        document.getElementById('Tweet').innerHTML = tweet[i];
    }
}

//Infinite Scroll
$(window).on("scroll", function() {
    //Altura de la página
    var scrollHeight = $(document).height();
    //Posición del cursor
    var scrollPos = $(window).height() + $(window).scrollTop();
    // Disparar si la posición del cursor está 300 pixeles más abajo del principio de la pagina 
    if(((scrollHeight - 300) >= scrollPos) / scrollHeight == 0){
        $("#cargar").click();
        console.log("bottom!");
    }
    });
