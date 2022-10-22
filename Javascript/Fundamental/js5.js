const isRaining = true;

//console.log("Persiapan sebelum berangkat kegiatan.");
if (isRaining) {
    console.log("Dadi payung naliko udane teko.");
} else {
    console.log("Berangkat kegiatan.");
}

//latihan switch javascriipt
let language = "English";
let greeting = null;

switch (language) {
    case "English":
        greeting = "Good Morning!";
        break;
    case "French":
        greeting = "Bonjour!";
        break;
    case "Japanese":
        greeting = "Ohayou Gozaimasu!";
        break;
    default:
        greeting = "Selamat Pagi!";
}

console.log(greeting);