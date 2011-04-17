$(document).ready(function() {

    $('nav > h2 >  a').mouseover(function() {
        var tag = $(this).text().toLowerCase();
        var highlighted = $('.' + tag).addClass('highlight');
    }).mouseout(function() {
        var tag = $(this).text().toLowerCase();
        var highlighted = $('.' + tag).removeClass('highlight');
    });
});
