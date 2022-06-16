//Variables temporales en lo que queda la base de datos
var screenname = ["Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus",
                  "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus", "Miley Cyrus"];
var username = ["@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus",
                "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus", "@mileycyrus final"];
var timestamp = ["2h", "2h", "2h", "2h", "2h", "2h", "2h", "2h", "2h", "2h",
                 "2h", "2h", "2h", "2h", "2h", "2h", "2h", "2h", "2h", "2h"];
var tweet = ["hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola",
             "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola", "hola final"];


var post = "<h6 class=\"text-body\">";
</h6><span class="small text-muted font-weight-normal"> • </span>
                      <span class="small text-muted font-weight-normal" id="TimeStamp"></span>
                      <span><i class="fas fa-angle-down float-end"></i></span>
                      <span class="small text-muted font-weight-normal" id="UserName"></span>
                      <p style="line-height: 1.2;" id="Tweet"></p>
//Función que imporime los tweets
window.onload = function() {
    for(i=0;i<10;i++) {
        const div0 = document.getElementById('ScreenName');
        div0.insertAdjacentHTML('beforeend', screenname[i]);
        const div1 = document.getElementById('UserName');
        div1.insertAdjacentHTML('beforeend', username[i]);
        const div2 = document.getElementById('TimeStamp');
        div2.insertAdjacentHTML('beforeend', timestamp[i]);
        const div3 = document.getElementById('Tweet');
        div3.insertAdjacentHTML('beforeend', tweet[i]);
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
