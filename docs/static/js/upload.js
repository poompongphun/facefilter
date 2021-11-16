const inputFile = document.getElementById("uploadFile");
const clickArea = document.getElementById("clickArea");
const submitBtn = document.getElementById("submitImg");
const dropText = document.getElementById("dropText");
const preImg = document.getElementById("imgPreview");
let tmpFile = null;
let beforeImg = null;

clickArea.onclick = () => {
  inputFile.click();
};

clickArea.ondragover = (ev) => {
  ev.preventDefault();
};

clickArea.ondrop = (ev) => {
  ev.preventDefault();
  previewImg(ev.dataTransfer.files[0]);
};

inputFile.onchange = function () {
  previewImg(this.files[0]);
};

function previewImg(file) {
  var reader = new FileReader();
  reader.readAsDataURL(file);
  tmpFile = file;
  dropText.style.display = "none";
  reader.onload = () => {
    preImg.src = reader.result;
    submitBtn.disabled = false;
  };
}

submitBtn.onclick = async () => {
  if (submitBtn.innerHTML == "Clear") {
    reset();
  } else {
    loading(true);
    let dataImg = new FormData();
    dataImg.append("img", tmpFile);
    try {
      const imgResponse = await fetch("acne?debug=true", {
        method: "post",
        body: dataImg,
      });
      setTimeout(async () => {
        preImg.src = URL.createObjectURL(await imgResponse.blob());
        beforeImg = tmpFile;
        tmpFile = null;
        loading(false);
      }, 500);
    } catch (error) {
      console.log(error);
    }
  }
};

function loading(state) {
  const myload = document.getElementById("loading");
  if (state) {
    myload.style.display = "inline";
    submitBtn.disabled = true;
    submitBtn.innerHTML = "Loading...";
    clickArea.style.pointerEvents = "none";
  } else {
    myload.style.display = "none";
    submitBtn.disabled = false;
    submitBtn.innerHTML = "Clear";
  }
}

function reset() {
  tmpFile = null;
  beforeImg = null;
  submitBtn.innerHTML = "Submit";
  submitBtn.disabled = true;
  preImg.src = "";
  dropText.style.display = "inline";
  clickArea.style.pointerEvents = "auto";
  inputFile.value = "";
}
