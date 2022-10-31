// memnngunakan objek 

const identitas = {
    name: "joko",
    address: "sobayan rt 04/ rw 02",
    umur: 23,
    sekolah: true,
    mantan: "dia yag menyakitai",
    "city": "ampel",
};

//funsgi memanipulasi objek
identitas.address = "DK Sobayan rt 04 / rw 02";
//fungsi ddelete
delete identitas.mantan;
//menampilkan dengan tempalte literal
console.log(`Halo nama saya ${identitas.name} alamat saya ${identitas.address}`);
console.log(`umur saya ${identitas.umur} saya sedang sekolah ${identitas.sekolah}`);
console.log(`saya berasal dari ${identitas["city"]}`);

//menampilkan objek
console.log(identitas);