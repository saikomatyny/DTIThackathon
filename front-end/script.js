"use strict"
const leftPane = document.querySelector(".left-pane");
const rightPane = document.querySelector(".right-pane");
const payload = {
  userFile: "",
  templateFile: ""
};

['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
  leftPane.addEventListener(eventName, preventDefaults, true );
  rightPane.addEventListener(eventName, preventDefaults, true );
});

function preventDefaults(e) {
  e.preventDefault();
  e.stopPropagation();
}

[leftPane, rightPane].forEach(pane => {
  pane.addEventListener("drop", handleDrop, true);
});

async function handleDrop(event) {
  const files = event.dataTransfer.files; 
  const file = files.length && files[0];

  if (file) {
    const pane = event.currentTarget;
    if (file.type === 'application/pdf') {
      const base64String = await convertFileToBase64(file); // Convert to Base64
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
}

function convertFileToBase64(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader(); // Create a FileReader instance

        // Event triggered when reading is complete
        reader.onload = () => {
            resolve(reader.result.split(',')[1]); // Remove the data URL prefix to get the Base64 string
        };

        // Event triggered if there's an error
        reader.onerror = (error) => {
            reject(error);
        };

        // Read the file as a data URL
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
    .then(res => console.log(res))
    .catch(err => console.log(err));
  }
});


