const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, { format: 'json' }, function (data, stat) {
  if (stat === 'success') {
    const movies = data.results;
    for (const movie of movies) {
      $('UL#list_movies').append('<li>' + movie.title + '</li>');
    }
  }
});
