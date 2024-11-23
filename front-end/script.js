const leftPane = document.querySelector(".left_pane");
const rightPane = document.querySelector(".right_pane");
const files = [];

['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    leftPane.addEventListener(eventName, preventDefaults, false);
    rightPane.addEventListener(eventName, preventDefaults, false);
});
function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

[leftPane, rightPane].forEach(pane => {
  pane.addEventListener("drop", handleDrop, false);

});
function handleDrop(event) {
    const pane = event.target;
    const files = event.dataTransfer.files; // Get the files from the drop
    if (files.length > 0) {
        const file = files[0];
        if (file.type === 'application/pdf') {
            const fileURL = URL.createObjectURL(file); // Create a URL for the PDF
            pane.innerHTML = `<iframe src="${fileURL}"></iframe>`;
        } else {
            pane.innerHTML = '<p>Please drop a valid PDF file.</p>';
        }
    }
}
