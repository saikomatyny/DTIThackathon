const leftPane = document.querySelector(".left_pane");
const rightPane = document.querySelector(".right_pane");

['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    userButtonUpload.addEventListener(eventName, preventDefaults, false);
    templateButtonUpload.addEventListener(eventName, preventDefaults, false);
});
function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}


userButtonUpload.addEventListener('drop', (e) => {
  userButtonUpload.style.visibility = "hidden";
  handleDrop(e);
}, false);
templateButtonUpload.addEventListener('drop', (e) => {
  templateButtonUpload.style.visibility = "hidden";
  handleDrop(e);
}, false);

function handleDrop(e) {
    const files = e.dataTransfer.files; // Get the files from the drop
    if (files.length > 0) {
        const file = files[0];
        if (file.type === 'application/pdf') {
            const fileURL = URL.createObjectURL(file); // Create a URL for the PDF
            pdfDisplay.innerHTML = `<iframe src="${fileURL}"></iframe>`;
        } else {
            pdfDisplay.innerHTML = '<p>Please drop a valid PDF file.</p>';
        }
    }
}


if ()
