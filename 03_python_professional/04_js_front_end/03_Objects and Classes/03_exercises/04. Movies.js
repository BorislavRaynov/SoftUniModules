function storeMovies(data) {
  let listMovie = [];
  function findMovie(name) {
    for (let m of listMovie) {
      if (m.name === name) {
        return m;
      }
    }
  }
  for (let info of data) {
    let movie = { name: "", director: "", date: "" };
    if (info.includes("addMovie")) {
      let currentName = info.replace("addMovie", "").trim();
      if (!findMovie(currentName)) {
        movie.name = currentName;
        listMovie.push(movie);
      }
    } else if (info.includes("directedBy")) {
      let currentInfo = info.replace("directedBy", "").split("  ");
      let currentName = currentInfo[0];
      let director = currentInfo[1];
      let thisMovie = findMovie(currentName);
      if (thisMovie) {
        thisMovie.director = director;
      }
    } else if (info.includes("onDate")) {
      let currentInfo = info.replace("onDate", "").split("  ");
      let currentName = currentInfo[0];
      let date = currentInfo[1];
      let thisMovie = findMovie(currentName);
      if (thisMovie) {
        thisMovie.date = date;
      }
    }
  }
  for (let movie of listMovie) {
    if (Object.values(movie).includes("")) {
      continue;
    } else {
      console.log(JSON.stringify(movie));
    }
  }
}

storeMovies([
  "addMovie The Avengers",
  "addMovie Superman",
  "The Avengers directedBy Anthony Russo",
  "The Avengers onDate 30.07.2010",
  "Captain America onDate 30.07.2010",
  "Captain America directedBy Joe Russo",
]);
