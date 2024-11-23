"use strict";

const leftPane = document.querySelector(".left-pane");
const rightPane = document.querySelector(".right-pane");
const fileInputs = document.querySelectorAll(".file-input");
const payload = {
  userFile: "",
  templateFile: ""
};

['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
  leftPane.addEventListener(eventName, preventDefaults, true);
  rightPane.addEventListener(eventName, preventDefaults, true);
});

function preventDefaults(e) {
  e.preventDefault();
  e.stopPropagation();
}

[leftPane, rightPane].forEach(pane => {
  pane.addEventListener("click", openFileDialog, true);
  pane.addEventListener("drop", handleDrop, true);
});

fileInputs.forEach(input => {
  input.addEventListener("change", handleFileSelection, true);
});

async function handleDrop(event) {
  const files = event.dataTransfer.files; 
  const file = files.length && files[0];

  if (file) {
    const pane = event.currentTarget;
    await handleFile(file, pane);
  }
}

async function handleFileSelection(event) {
  const input = event.target;
  const file = input.files[0];

  if (file) {
    const pane = input.dataset.pane === "left" ? leftPane : rightPane;
    await handleFile(file, pane);
  }
}

async function handleFile(file, pane) {
  if (file.type === 'application/pdf') {
    const base64String = await convertFileToBase64(file);
    if (pane === leftPane) {
      payload.templateFile = base64String;
    } else {
      payload.userFile = base64String;
    }

    pane.innerHTML = "";
    const fileURL = URL.createObjectURL(file); 
    const iframe = document.createElement("iframe");
    iframe.src = fileURL;
    pane.appendChild(iframe);
    iframe.contentWindow.document.addEventListener("drop", event => {
      event.stopPropagation();
      event.preventDefault();
    }, true);
  } else {
    pane.innerHTML = '<p>Please drop a valid PDF file.</p>';
  }
}

function openFileDialog(event) {
  const pane = event.currentTarget;
  const input = pane.querySelector(".file-input");
  input.click();
}

function convertFileToBase64(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => resolve(reader.result.split(',')[1]);
    reader.onerror = error => reject(error);
    reader.readAsDataURL(file);
  });
}

const button = document.querySelector("button");
button.addEventListener("click", () => {
  if (payload.userFile && payload.templateFile) {
    fetch("http://localhost:8000", {
      method: "POST",
      body: JSON.stringify(payload)
    })
    .then(res => res.json())
    .then(data => {
      data = JSON.parse(data);
      console.log(data);
      const analysis = document.createElement("div");
      for (const entry of data) {
        analysis.innerHTML += `
          <div>
            ${entry.correct}
          </div>
          <br>
          <br>
          <div>
            ${entry.explanation}
          </div>
        `;
      }
      document.body.append(analysis);
    })
    .catch(err => console.log(err));
  }
});
