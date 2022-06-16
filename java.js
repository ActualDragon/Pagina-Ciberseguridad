
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
