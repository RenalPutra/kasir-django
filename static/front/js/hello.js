let select_bt = document.querySelectorAll(".hub");

select_bt.forEach((value, index) => {
  select_bt[index].onclick = (event) => {
    event.preventDefault();
    const href = select_bt[index].getAttribute("href");
    swal({
      title: "Yakin nih mau hapus?",
      text: "Jika data terhapus maka tidak bisa di recovery kembali!",
      icon: "warning",
      buttons: true,
      dangerMode: true,
    }).then((result) => {
      if (result) {
        document.location.href = href;
      }
    });
  };
});

let ad_bt = document.querySelector(".add-btn");
let formulir = document.querySelector(".formulir");
ad_bt.onclick = (event) => {
  event.preventDefault();
  swal({
    title: "Berhasil",
    text: "Penambahan atau perubahan data berhasil dilakukan!",
    icon: "success",
  }).then((result) => {
    if (result) {
      formulir.submit();
    }
  });
};
