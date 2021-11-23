const inputFile = document.getElementById("uploadFile");
const clickArea = document.getElementById("clickArea");
const submitBtn = document.getElementById("submitImg");
const dropText = document.getElementById("dropText");
const preImg = document.getElementById("imgPreview");
const debugSwt = document.getElementById("flexSwitchCheckDefault")
const confInput = document.getElementById("confInput")
const widthInput = document.getElementById("widthInput")
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
      const debug = debugSwt.checked
      const parseConf = parseFloat(confInput.value)
      const conf = parseConf < 1 ? confInput.value : parseConf || 1
      const parseWid = parseFloat(widthInput.value)
      const width = parseWid < 1 ? widthInput.value : parseWid || 30
      const imgResponse = await fetch(`acne?debug=${debug}&conf=${conf}&width=${width}`, {
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
