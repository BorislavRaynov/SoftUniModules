function park(data) {
  let parking = [];
  for (let info of data) {
    [direction, plate] = info.split(", ");
    if (!parking.includes(plate)) {
      if (direction === "IN") {
        parking.push(plate);
      }
    } else {
      if (direction === "OUT") {
        carLot = parking.indexOf(plate);
        parking.splice(carLot, 1);
      }
    }
  }
  if (parking.length === 0) {
    console.log("Parking Lot is Empty");
  } else {
    console.log(parking.sort().join("\n"));
  }
}

park([
  "IN, CA2844AA",
  "IN, CA1234TA",
  "OUT, CA2844AA",
  "IN, CA9999TT",
  "IN, CA2866HI",
  "OUT, CA1234TA",
  "IN, CA2844AA",
  "OUT, CA2866HI",
  "IN, CA9876HH",
  "IN, CA2822UU",
]);
