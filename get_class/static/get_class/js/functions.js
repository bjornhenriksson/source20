jQuery(document).ready(function ($) {

    $(".rate").hide();
    $(".next").click(function() {
      $(".pagination").slideUp(200);
      $(".description").slideUp(200);
      $(".rate").slideDown(200);
      $(".course").addClass("toned");
    });

});   