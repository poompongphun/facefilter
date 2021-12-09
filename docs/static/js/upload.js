const inputFile = document.getElementById("uploadFile");
const clickArea = document.getElementById("clickArea");
const submitBtn = document.getElementById("submitImg");
const downloadBtn = document.getElementById("downloadBtn");
const dropText = document.getElementById("dropText");
const preImg = document.getElementById("imgPreview");
const debugSwt = document.getElementById("flexSwitchCheckDefault");
const confInput = document.getElementById("confInput");
const widthInput = document.getElementById("widthInput");
const cardAlrt = document.getElementById("showAlert");
let tmpFile = null;
let beforeImg = null;
let download = null;

// click event in dropdown area
clickArea.onclick = () => {
  inputFile.click(); // click hidden file input
};

// drag something over dropdown area
clickArea.ondragover = (ev) => {
  ev.preventDefault(); // dont do anything
};

// drop something over dropdown area
clickArea.ondrop = (ev) => {
  ev.preventDefault(); // dont do anything
  previewImg(ev.dataTransfer.files[0]); // send file to preview
};

// hidden file input change value
inputFile.onchange = function () {
  previewImg(this.files[0]); // send file to preview
};

// download button click
downloadBtn.onclick = () => {
  const a = document.createElement("a"); // create new a element
  a.href = download; // set link
  a.download = "PhotoRetouch.png"; // set name
  document.body.appendChild(a); // create a tag!!
  a.click(); // then click for download!!
  document.body.removeChild(a); // remove a tag
};

// preview image
function previewImg(file) {
  let reader = new FileReader(); // new file reader
  reader.readAsDataURL(file); // convert file to url
  tmpFile = file; // keep file to tmp
  dropText.style.display = "none"; // hide "Drop your image here or browse." text
  reader.onload = () => {
    preImg.src = reader.result; // set src to show image
    submitBtn.disabled = false; // enable submit button
  };
}

// submit button click
submitBtn.onclick = async () => {
  if (submitBtn.innerHTML == "Clear") { // if text in submit button is Clear then reset all
    reset();
  } else {
    loading(true); // show loading effect
    let dataImg = new FormData(); // new formdata
    dataImg.append("img", tmpFile); // add file to key img
    try {
      const debug = debugSwt.checked;
      const parseConf = parseFloat(confInput.value);
      const conf = parseConf < 1 ? confInput.value : parseConf || 1; // if no confInput use default value
      const parseWid = parseFloat(widthInput.value);
      const width = parseWid < 1 ? widthInput.value : parseWid || 30; // if no widthInput use default value
      const imgResponse = await fetch(
        `acne?debug=${debug}&conf=${conf}&width=${width}`,
        {
          method: "post",
          body: dataImg,
        }
      ); // send request to clear acne api
      // delay 0.5 sec after request done
      setTimeout(async () => {
        download = URL.createObjectURL(await imgResponse.blob()); // convert response image to url
        preImg.src = download; // set response img to show in preview
        beforeImg = tmpFile;
        tmpFile = null;
        loading(false); // hide loading effect
        if (imgResponse.status != 200) // request status is not 200 will show alert error
          showAlrt("Failed", "alert-danger", "bi-x-circle-fill");
      }, 500);
    } catch (error) {
      console.log(error);
    }
  }
};

// loading effect
function loading(state) {
  const myload = document.getElementById("loading");
  if (state) {
    myload.style.display = "inline";
    submitBtn.disabled = true;
    downloadBtn.disabled = true;
    submitBtn.innerHTML = "Loading...";
    clickArea.style.pointerEvents = "none";
  } else {
    myload.style.display = "none";
    submitBtn.disabled = false;
    downloadBtn.disabled = false;
    submitBtn.innerHTML = "Clear";
    showAlrt("Success ก็ไปตากสิ");
  }
}

// show alert
showAlrt = (
  text = "Success",
  type = "alert-success",
  icon = "bi-check-circle-fill"
) => {
  cardAlrt.classList.add(type);
  cardAlrt.innerHTML = `<i class="bi ${icon}"></i> ${text}`;
  cardAlrt.style.opacity = 100;
  setTimeout(() => {
    cardAlrt.style.opacity = 0;
  }, 2000);
};

// reset everything
function reset() {
  tmpFile = null;
  beforeImg = null;
  download = null;
  submitBtn.innerHTML = "Submit";
  submitBtn.disabled = true;
  downloadBtn.disabled = true;
  preImg.src = "";
  dropText.style.display = "inline";
  clickArea.style.pointerEvents = "auto";
  inputFile.value = "";
}
