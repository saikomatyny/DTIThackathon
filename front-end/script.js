<<<<<<< HEAD
"use strict"
const leftPane = document.querySelector(".left-pane");
const rightPane = document.querySelector(".right-pane");
const payload = {
  userFile: "",
  templateFile: ""
};
=======
const leftPane = document.querySelector(".left_pane");
const rightPane = document.querySelector(".right_pane");
>>>>>>> 0c5bb942c4939570687d1b09bc6d3b768bfad1ed

['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
  leftPane.addEventListener(eventName, preventDefaults, true );
  rightPane.addEventListener(eventName, preventDefaults, true );
});

function preventDefaults(e) {
  e.preventDefault();
  e.stopPropagation();
}

[leftPane, rightPane].forEach(pane => {
<<<<<<< HEAD
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


=======
    pane.addEventListener("dragenter", handleDragEnter, false);
    pane.addEventListener("drop", handleDrop, false);
    pane.addEventListener("dragleave", handleDragLeave, false);
});

function handleDragEnter(event) {
    const pane = event.currentTarget;

    if (!pane.classList.contains("drag-active")) {
        pane.style.backgroundColor = "rgba(142, 37, 100, 0.5)";
    }
}

function handleDragLeave(event) {
    const pane = event.currentTarget;

    pane.style.backgroundColor = "rgba(0, 0, 0, 0.3)";
}

function handleDrop(event) {
    const pane = event.currentTarget;
    const files = event.dataTransfer.files;

    if (files.length > 0) {
        const file = files[0];
        if (file.type === 'application/pdf') {
            const fileURL = URL.createObjectURL(file);

            const iframe = document.createElement("iframe");
            iframe.src = fileURL;
            iframe.style.width = "95%";
            iframe.style.height = "95%";
            iframe.style.zIndex = "-1";

            pane.innerHTML = '';
            pane.appendChild(iframe);
        } else {
            pane.innerHTML = '<p>Please drop a valid PDF file.</p>';
        }
    }
    pane.style.backgroundColor = "transparent";
}
>>>>>>> 0c5bb942c4939570687d1b09bc6d3b768bfad1ed
