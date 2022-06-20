//JSON temporal en lo que queda la base de datos
var Informacion= {
    "TweetsRecibidos" : [
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
        {"screenname":"Miley Cyrus", "username":"@hannamontana", "timestamp":"2h", "tweet":"hola final"}
    ],
    "numTweets" : 21,
    "usuario" : "@hannamontana",
    "nombre" : "Myley Cyrus"
}

miUsuario = Informacion.usuario;
numeroTweets = Informacion.numTweets-1;
number=0; //Variable que determina cuántos tweets se han impreso

//Función que imporime los primeros 10 tweets
window.onload = function() {
    ImprimeTweets(number);
}

//Función que permite tener un delay a la hora de cargar los tweets nuevos
const sleep = async (milliseconds) => {
    await new Promise(resolve => {
        return setTimeout(resolve, milliseconds)
    });
};

//Función que imprime los siguientes 10 tweets cuando se llega al final de la página
function ImprimeTweets(number) {
    // testSleep genera un pequeño delay al cargar los tweets nuevos
    const testSleep = async () => {
        await sleep(1000);
        for(i=number;(i<(number+10));i++) {
            // Validar que siga habiendo tweets
            if (i<=numeroTweets) {
                //En post se guardaa el HTML para el tweet, agregandole la información de la base de datos
                var post = "<h6 class=\"text-body\">";
                post += "<div class=\"p-3 border-bottom\">";
                post += "<img src=\"https://mdbcdn.b-cdn.net/img/Photos/Avatars/img (29).webp\" class=\"rounded-circle\" height=\"50\" loading=\"lazy\"/>  ";
                post += Informacion.TweetsRecibidos[i].screenname;
                post += "<div style=\"display:inline\" class=\"small text-muted font-weight-normal\"> • </div>";
                post += "<span class=\"small text-muted font-weight-normal\">";
                post += Informacion.TweetsRecibidos[i].username;
                post += "</span><span class=\"small text-muted font-weight-normal\">  ";
                post += Informacion.TweetsRecibidos[i].timestamp;
                post += "</span>";
                //Menu para borrar, editar, etc., tus propios tweets
                if(Informacion.TweetsRecibidos[i].username==miUsuario){
                    post += "<div class=\"dropdown\" style=\"display: inline-block\">";
                    post += "<button class=\"btn btn-link dropdown-toggle\" type=\"button\" id=\"dropdownMenu\" data-bs-toggle=\"dropdown\" aria-expanded=\"false\" style=\"color: grey\"></button>";
                    post += "<ul class=\"dropdown-menu\">";
                    post += "<li><a class=\"dropdown-item\" onclick=\"BorraTweet(this)\" id=\"Borrar_";
                    post += i;
                    post += "\">Borrar</a></li>";
                    post += "<li><a class=\"dropdown-item\"  onclick=\"EditaTweet(this)\" id=\"Editar_";
                    post += i;
                    post += "\">Editar</a></li>";
                    post += "</ul></div>";
                }
                post += "</div></h6><p class=\"p-3 border-bottom border-dark\" id=\"Tweet";
                post += i;
                post += "\" style=\"line-height: 1.2;\">";
                post += Informacion.TweetsRecibidos[i].tweet;
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

//Obtener el texto de un tweet nuevo
function NuevoTweet(){
    var text = document.getElementById("tweetForm").value;
    console.log(text);
    //Insertar el tweet en la página
    var post = "<h6 class=\"text-body\">";
    post += "<div class=\"p-3 border-bottom\">";
    post += "<img src=\"https://mdbcdn.b-cdn.net/img/Photos/Avatars/img (29).webp\" class=\"rounded-circle\" height=\"50\" loading=\"lazy\"/>  ";
    post += Informacion.nombre;
    post += "<div style=\"display:inline\" class=\"small text-muted font-weight-normal\"> • </div>";
    post += "<span class=\"small text-muted font-weight-normal\">";
    post += Informacion.usuario;
    post += "</span><span class=\"small text-muted font-weight-normal\">  ";
    post += " just now";
    post += "</span>";
    post += "<div class=\"dropdown\" style=\"display: inline-block\">";
    post += "<button class=\"btn btn-link dropdown-toggle\" type=\"button\" id=\"dropdownMenu\" data-bs-toggle=\"dropdown\" aria-expanded=\"false\" style=\"color: grey\"></button>";
    post += "<ul class=\"dropdown-menu\" aria-labelledby=\"dropdownMenuButton1\">";
    post += "<li><a class=\"dropdown-item\" href=\"#\">Borrar</a></li>";
    post += "<li><a class=\"dropdown-item\" href=\"#\">Editar</a></li>";
    post += "</ul></div>";
    post += "</div></h6><p class=\"p-3 border-bottom border-dark\" style=\"line-height: 1.2;\">";
    post += text;
    post += "</p>";
    //El contenido se agrega antes de los demás tweets
    const div = document.getElementById('divprint');
    div.insertAdjacentHTML('afterbegin', post);

    //Post
    //$.post("tweet/new",tweet);
}

//Borrar un tweet
function BorraTweet(boton){
    idOriginal=boton.id;
    splitId = idOriginal.split("_");
    numid = splitId[1];
    var id = "Tweet";
    id += numid;
}

//Editar un tweet
function EditaTweet(boton){
    //Obtener el id del boton a editar
    idOriginal=boton.id;
    splitId = idOriginal.split("_");
    numid = splitId[1];
    var id = "Tweet";
    id += numid;
    //Obtener el texto del tweet original
    var text = document.getElementById(id).innerHTML;
    //Generar el entrybox
    const textarea = document.createElement('textarea');
    //Reemplazar el contenido original con el entrybox
    document.getElementById(id).replaceWith(textarea);
    //Darle formato al entrybox nuevo
    textarea.setAttribute("id", id);
    textarea.setAttribute("class", "form-control form-status border-0 pe-3");
    textarea.setAttribute("type", "text");
    textarea.setAttribute("maxlength", "512");
    textarea.setAttribute("rows","2");
    //Insertar el tweet original en el entrybox
    document.getElementById(id).value = text;
    //Generar un boton nuevo
    var boton = "<div class=\"d-flex align-items-center float-end pe-3\"><button id=\"editButton";
    boton += numid;
    boton += "\" type=\"button\" onclick=\"TweetEditado(this)\" class=\"btn btn-primary btn-rounded\">Publicar</button></div>";
    //Insertar el boton
    var div = document.getElementById(id);
    div.insertAdjacentHTML('afterend', boton);
}

//Publicar el tweet editado
function TweetEditado(boton){
    //Obtener el id del boton a editar
    idOriginal=boton.id;
    splitId = idOriginal.split("_");
    numid = splitId[1];
    var id = "Tweet";
    id += numid;
    //Obtener el texto del tweet
    var text = document.getElementById(id).innerHTML;
}
