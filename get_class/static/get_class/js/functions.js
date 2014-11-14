jQuery(document).ready(function ($) {

    $(".rate").hide();
    $(".pagination").click(function() {
      $(".pagination").slideUp(200);
      $(".description").slideUp(200);
      $(".rate").slideDown(200);
    });

});   