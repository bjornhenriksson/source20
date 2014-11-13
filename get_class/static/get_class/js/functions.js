jQuery(document).ready(function ($) {

	$('.click').click(function () {
		var number = $(this).data("id");
       	$(".cases").removeClass("active");
       	$(".cases#"+number).addClass("active");
    });

	var portfolioOffset = $( ".summary" ).offset().top;

	$('.button-portfolio').click(function () {
		$('html,body').animate({
          scrollTop: portfolioOffset
        }, 600);
    });

});   