$(document).ready(function() {
    $(".menu-icon").on("click", function() {
          $("nav ul").toggleClass("showing");
    });
});

// Scrolling Effect

$(window).on("scroll", function() {
    if($(window).scrollTop()) {
          $('nav').addClass('black');
    }

    else {
          $('nav').removeClass('black');
    }
})

// init Isotope
var $grid = $('.collection-list').isotope({
      // options
    });
    // filter items on button click
    $('.filter-button-group').on( 'click', 'button', function() {
      var filterValue = $(this).attr('data-filter');
      resetFilterBtns();
      $(this).addClass('active-filter-btn');
      $grid.isotope({ filter: filterValue });
    });
    
    var filterBtns = $('.filter-button-group').find('button');
    function resetFilterBtns(){
      filterBtns.each(function(){
        $(this).removeClass('active-filter-btn');
      });
    }