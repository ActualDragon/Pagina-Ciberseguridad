//JSON temporales en lo que queda la base de datos
var TweetsRecibidos = [
    {"screenname":"Miley Cyrus", "username":"@hannamontana", "timestamp":"2h", "tweet":"hola"},
    {"screenname":"Miley Cyrus", "username":"@myleycyrus", "timestamp":"2h", "tweet":"hola"},
    {"screenname":"Miley Cyrus", "username":"@myleycyrus", "timestamp":"2h", "tweet":"hola"},
    {"screenname":"Miley Cyrus", "username":"@myleycyrus", "timestamp":"2h", "tweet":"hola"},
    {"screenname":"Miley Cyrus", "username":"@myleycyrus", "timestamp":"2h", "tweet":"hola"},
    {"screenname":"Miley Cyrus", "username":"@myleycyrus", "timestamp":"2h", "tweet":"hola"},
    {"screenname":"Miley Cyrus", "username":"@myleycyrus", "timestamp":"2h", "tweet":"hola"},
    {"screenname":"Miley Cyrus", "username":"@myleycyrus", "timestamp":"2h", "tweet":"hola"},
    {"screenname":"Miley Cyrus", "username":"@myleycyrus", "timestamp":"2h", "tweet":"hola"},
    {"screenname":"Miley Cyrus", "username":"@myleycyrus", "timestamp":"2h", "tweet":"hola"},
    {"screenname":"Miley Cyrus", "username":"@myleycyrus", "timestamp":"2h", "tweet":"hola"},
    {"screenname":"Miley Cyrus", "username":"@myleycyrus", "timestamp":"2h", "tweet":"hola"},
    {"screenname":"Miley Cyrus", "username":"@myleycyrus", "timestamp":"2h", "tweet":"hola"},
    {"screenname":"Miley Cyrus", "username":"@myleycyrus", "timestamp":"2h", "tweet":"hola"},
    {"screenname":"Miley Cyrus", "username":"@myleycyrus", "timestamp":"2h", "tweet":"hola"},
    {"screenname":"Miley Cyrus", "username":"@myleycyrus", "timestamp":"2h", "tweet":"hola"},
    {"screenname":"Miley Cyrus", "username":"@myleycyrus", "timestamp":"2h", "tweet":"hola"},
    {"screenname":"Miley Cyrus", "username":"@myleycyrus", "timestamp":"2h", "tweet":"hola"},
    {"screenname":"Miley Cyrus", "username":"@myleycyrus", "timestamp":"2h", "tweet":"hola"},
    {"screenname":"Miley Cyrus", "username":"@myleycyrus", "timestamp":"2h", "tweet":"hola"},
    {"screenname":"Miley Cyrus", "username":"@myleycyrus", "timestamp":"2h", "tweet":"hola"}
]

//Arreglos temporales en lo que queda la base de datos
var screenname = ["Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus",
                  "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus"];
var username = ["@hannamontana", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus",
                "@hannamontana", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus final"];
var timestamp = ["2h", "2h", "2h", "2h", "2h", "2h", "2h", "2h", "2h", "2h",
                 "2h", "2h", "2h", "2h", "2h", "2h", "2h", "2h", "2h", "2h"];
var tweet = ["hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola",
             "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola final"];

var miUsuario = "@hannamontana";

number=0; //Variable que permite cargar los siguientes 10 tweets

//Función que permite tener un delay a la hora de cargar los tweets nuevos
const sleep = async (milliseconds) => {
    await new Promise(resolve => {
        return setTimeout(resolve, milliseconds)
    });
};

//Función que imporime los primeros 10 tweets
window.onload = function() {
    for(i=0;i<10;i++) {
        // Validar que siga habiendo tweets
        if (TweetsRecibidos[i].screenname !== null) {
            //En post se guardaa el HTML para el tweet, agregandole la información de la base de datos
            var post = "<h6 class=\"text-body\">";
            post += "<div class=\"p-3 border-bottom\">";
            post += "<img src=\"https://mdbcdn.b-cdn.net/img/Photos/Avatars/img (29).webp\" class=\"rounded-circle\" height=\"50\" loading=\"lazy\"/>  ";
            post += TweetsRecibidos[i].screenname;
            post += "<div style=\"display:inline\" class=\"small text-muted font-weight-normal\"> • </div>";
            post += "<span class=\"small text-muted font-weight-normal\">";
            post += TweetsRecibidos[i].username;
            post += "</span><span class=\"small text-muted font-weight-normal\">  ";
            post += TweetsRecibidos[i].timestamp;
            post += "</span>";
            //Menu para borrar, editar, etc., tus propios tweets
            if(TweetsRecibidos[i].username==miUsuario){
                post += "<div class=\"dropdown\" style=\"display: inline-block\">";
                post += "<button class=\"btn btn-link dropdown-toggle\" type=\"button\" id=\"dropdownMenu\" data-bs-toggle=\"dropdown\" aria-expanded=\"false\" style=\"color: grey\"></button>";
                post += "<ul class=\"dropdown-menu\" aria-labelledby=\"dropdownMenuButton1\">";
                post += "<li><a class=\"dropdown-item\" href=\"#\">Borrar</a></li>";
                post += "<li><a class=\"dropdown-item\" href=\"#\">Editar</a></li>";
                post += "</ul></div>";
            }
            post += "</div></h6><p class=\"p-3 border-bottom border-dark\" style=\"line-height: 1.2;\">";
            post += TweetsRecibidos[i].tweet;
            post += "</p>";
            //El contenido de post se agrega como hijo de un div vacío
            const div = document.getElementById('divprint');
            div.insertAdjacentHTML('beforeend', post);
        }
    }
}

//Función que imprime los siguientes 10 tweets cuando se llega al final de la página
function ImprimeTweets(number) {
    // testSleep genera un pequeño delay al cargar los tweets nuevos
    const testSleep = async () => {
        await sleep(1000);
        for(i=number;(i<(number+10));i++) {
            // Validar que siga habiendo tweets
            console.log(TweetsRecibidos[i].screenname);
            if (!(jQuery.isEmptyObject(TweetsRecibidos[i].screenname))) {
                //En post se guardaa el HTML para el tweet, agregandole la información de la base de datos
                var post = "<h6 class=\"text-body\">";
                post += "<div class=\"p-3 border-bottom\">";
                post += "<img src=\"https://mdbcdn.b-cdn.net/img/Photos/Avatars/img (29).webp\" class=\"rounded-circle\" height=\"50\" loading=\"lazy\"/>  ";
                post += TweetsRecibidos[i].screenname;
                post += "<div style=\"display:inline\" class=\"small text-muted font-weight-normal\"> • </div>";
                post += "<span class=\"small text-muted font-weight-normal\">";
                post += TweetsRecibidos[i].username;
                post += "</span><span class=\"small text-muted font-weight-normal\">  ";
                post += TweetsRecibidos[i].timestamp;
                post += "</span>";
                //Menu para borrar, editar, etc., tus propios tweets
                if(TweetsRecibidos[i].username==miUsuario){
                    post += "<div class=\"dropdown\" style=\"display: inline-block\">";
                    post += "<button class=\"btn btn-link dropdown-toggle\" type=\"button\" id=\"dropdownMenu\" data-bs-toggle=\"dropdown\" aria-expanded=\"false\" style=\"color: grey\"></button>";
                    post += "<ul class=\"dropdown-menu\" aria-labelledby=\"dropdownMenuButton1\">";
                    post += "<li><a class=\"dropdown-item\" href=\"#\">Borrar</a></li>";
                    post += "<li><a class=\"dropdown-item\" href=\"#\">Editar</a></li>";
                    post += "</ul></div>";
                }
                post += "</div></h6><p class=\"p-3 border-bottom border-dark\" style=\"line-height: 1.2;\">";
                post += TweetsRecibidos[i].tweet;
                post += "</p>";
                //El contenido de post se agrega como hijo de un div vacío
                const div = document.getElementById('divprint');
                div.insertAdjacentHTML('beforeend', post);
            }
            // Desactivar el botón si no hay más tweets por cargar
            else {
                document.getElementById("cargar").disabled = true;
                document.getElementById("cargar").innerHTML = "Esperando tweets"; 
            }
        }
    }
    testSleep();
}

//Infinite Scroll
$(window).on("scroll", function() {
    //Altura de la página
    var scrollHeight = $(document).height();
    //Posición del cursor
    var scrollPos = $(window).height() + $(window).scrollTop();
    // Disparar si la posición del cursor está 300 pixeles más abajo del principio de la pagina 
    if(((scrollHeight - 300) >= scrollPos) / scrollHeight == 0){
        number = number+10;
        $("#cargar").click();
        $("#cargar").onclick=ImprimeTweets(number);
    }
    });
