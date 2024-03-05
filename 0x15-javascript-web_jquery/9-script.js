const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$('document').ready(function () {
  $.get(url, function (data, stat) {
    if (stat === 'success') {
      $('Div#hello').text(data.hello);
    }
  });
});
