const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(url, { format: 'json' }, function (data, stat) {
  if (stat === 'success') {
    const name = data.name;
    $('DIV#character').text(name);
  }
});
