"use strict";

const leftPane = document.querySelector(".left-pane");
const rightPane = document.querySelector(".right-pane");
const fileInputs = document.querySelectorAll(".file-input");
const button = document.querySelector("button");
const resultField = document.querySelector(".result-field");

const loadingAnimation = document.createElement("div");
loadingAnimation.classList.add("loading-animation");

const payload = {
  userFile: "",
  templateFile: "",
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

button.addEventListener("click", async () => {
  if (payload.userFile && payload.templateFile) {
    showLoading();
    try {
      const response = await fetch("http://localhost:8000", {
        method: "POST",
        body: JSON.stringify(payload),
      });
      const data = await response.json();
      processResults(data);
    } catch (err) {
      console.error(err);
    } finally {
      hideLoading();
    }
  }
});

function showLoading() {
  button.disabled = true;
  button.innerText = "";
  button.appendChild(loadingAnimation);
}

function hideLoading() {
  button.disabled = false;
  button.innerText = "Compare";
  loadingAnimation.remove();
}

function processResults(data) {
  data = JSON.parse(data.string);
  resultField.innerHTML = "";
  for (const entry of data) {
    resultField.innerHTML += createRecommendation(entry.correct, entry.explanation);
  }
  resultField.hidden = false;
}

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
    const pane = input.parentElement === leftPane ? leftPane : rightPane;
    await handleFile(file, pane);
  }
}

async function handleFile(file, pane) {
  if (file.type === "application/pdf") {
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
    iframe.contentWindow.document.addEventListener("drop", (event) => {
      event.stopPropagation();
      event.preventDefault();
    }, true);
  } else {
    pane.innerHTML = "<p>Please drop a valid PDF file.</p>";
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
    reader.onload = () => resolve(reader.result.split(",")[1]);
    reader.onerror = (error) => reject(error);
    reader.readAsDataURL(file);
  });
}

function createRecommendation(header, body) {
  return `
  <div class="recommendation">
    <div class="recommendation-header">
      <h3>It should be:</h3>
      ${header}
    </div>
    <div class="recommendation-body">
      <h3>Why?</h3>
      ${body}
    </div>
  </div>
  `;
}