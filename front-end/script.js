const leftPane = document.querySelector(".left_pane");
const rightPane = document.querySelector(".right_pane");

['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    leftPane.addEventListener(eventName, preventDefaults, false);
    rightPane.addEventListener(eventName, preventDefaults, false);
});

function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

[leftPane, rightPane].forEach(pane => {
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