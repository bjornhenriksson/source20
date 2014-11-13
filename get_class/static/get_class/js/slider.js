jQuery(document).ready(function ($) {

    var delay = (function(){
      var timer = 0;
      return function(callback, ms){
        clearTimeout (timer);
        timer = setTimeout(callback, ms);
      };
    })();

    $(window).resize(function() {
        delay(function(){
            location.reload();
        }, 500);
    });

    var slideCount = $('.slider ul li').length;
    var slideWidth = $('.slider ul li').width();
    var slideSection = $('.slider').width();
    var slideHeight = $('.slider ul li#highest').height();
    var sliderUlWidth = slideCount * slideWidth; 

    var ems = parseFloat($("body").css("font-size"));
    var responsive = ems * 60;

    $('.slider ul').css({ width: sliderUlWidth, marginLeft: - slideWidth });
    $('.slider ul li').css({ width: slideSection, height: slideHeight });
    if ($(window).width() < responsive) {
       $('.cases.active').css({ height: slideHeight + 300 });
       $("#oneimage").attr("src", "../img/guru-case-double.jpg");
    }
    $('.slider ul li:last-child').prependTo('.slider ul');

    function moveLeft() {
        $('.slider ul').animate({
            left: + slideWidth
        }, 500, function () {
            $('.slider ul li:last-child').prependTo('.slider ul');
            $('.slider ul').css('left', '');
        });
    };

    function moveRight() {
        $('.slider ul').animate({
            left: - slideWidth
        }, 500, function () {
            $('.slider ul li:first-child').appendTo('.slider ul');
            $('.slider ul').css('left', '');
        });
    };

    $('#prev, #horizontal-prev').click(function () {
        moveLeft();
    });

    $('#next, #horizontal-next').click(function () {
        moveRight();
    });

});   