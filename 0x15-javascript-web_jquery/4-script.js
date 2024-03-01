$('Div#toggle_header').click(function () {
  if ($('header').hasClass('green')) {
    $('header').removeClass('green');
    $('header').addClass('red');
  } else if ($('header').hasClass('red')) {
    $('header').toggleClass('red green');
  }
});
