function songs(data) {
  class Song {
    constructor(typeList, name, time) {
      this.typeList = typeList;
      this.name = name;
      this.time = time;
    }
  }
  let count = data[0];
  let searchedType = data.slice(-1)[0];
  let listAll = [];
  for (let i = 1; i <= count; i++) {
    let song = data[i];
    [typeList, names, time] = song.split("_");
    if (searchedType === "all") {
      listAll.push(new Song(typeList, names, time));
    } 
    else if (typeList === searchedType) {
      listAll.push(new Song(typeList, names, time));
    }
  }
  for (let s of listAll) {
    console.log(s.name);
  }
}

// songs([
//   3,
//   "favourite_DownTown_3:14",
//   "favourite_Kiss_4:16",
//   "favourite_Smooth Criminal_4:01",
//   "favourite",
// ]);

songs([2, "like_Replay_3:15", "ban_Photoshop_3:48", "all"]);

// songs([
//   4,
//   "favourite_DownTown_3:14",
//   "listenLater_Andalouse_3:24",
//   "favourite_In To The Night_3:58",
//   "favourite_Live It Up_3:48",
//   "listenLater",
// ]);
