function solve(speed, area) {
  let areaLimit = 0;
  if (area === "motorway") {
    areaLimit = 130;
  } else if (area === "interstate") {
    areaLimit = 90;
  } else if (area === "city") {
    areaLimit = 50;
  } else {
    areaLimit = 20;
  }

  if (speed <= areaLimit) {
    console.log(`Driving ${speed} km/h in a ${areaLimit} zone`);
  } else {
    let status = "reckless driving";
    let difference = speed - areaLimit;
    if (difference <= 20) {
      status = "speeding";
    } else if (difference <= 40) {
      status = "excessive speeding";
    }
    console.log(`The speed is ${difference} km/h faster than the allowed speed of ${areaLimit} - ${status}`)
  }
}

solve(21, 'residential')
