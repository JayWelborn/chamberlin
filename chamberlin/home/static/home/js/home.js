$(document).ready(function(){
    // set height of jumbotron
    var jumboHeight = $('.jumbotron').outerHeight();
    // change height of bg as document is scrolled
    function parallax(){
        var scrolled = $(window).scrollTop();
        $('.bg').css('height', (jumboHeight-scrolled) + 'px');
    }

    $(window).scroll(function(e){
        parallax();
    });

    $('.blog .button').click(function(){
        $( '.blog' ).toggleClass( "expanded" );
        $( this ).text(function(i, text){
            return text === "Read More" ? "Read Less" : "Read More";
        })
    });
});