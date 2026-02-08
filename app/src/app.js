const dropZone = document.getElementById('drop-zone');

// 1. Prevent default behavior for drag events
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropZone.addEventListener(eventName, (e) => {
        e.preventDefault();
        e.stopPropagation();
    }, false);
});

// 2. Handle the drop
dropZone.addEventListener('drop', (e) => {
    const files = e.dataTransfer.files;
    
    if (files.length > 0) {
        const file = files[0];

        // Ensure it is a text-based file
        if (file.type === "text/html" || file.type === "text/plain") {
            const reader = new FileReader();

            // 3. Define what happens when reading is complete
            reader.onload = (event) => {
                const content = event.target.result;
                console.log("--- File Content Start ---");
                console.log(content);
                console.log("--- File Content End ---");
            };

            // 4. Start reading the file as text
            reader.readAsText(file);
        } else {
            console.error("Please drop a text or HTML file.");
        }
    }
});



// 4. Handle the "Enter" key to print to console
dropZone.addEventListener('keydown', (e) => {
    // Check if the key pressed was 'Enter'
    if (e.key === 'Enter') {
        // Prevent the default behavior (which adds a new line in the box)
        e.preventDefault();

        const currentText = dropZone.innerText.trim();

        if (currentText.length > 0) {
            console.log("--- Manual Input Start ---");
            console.log(currentText);
            console.log("--- Manual Input End ---");

            // Optional: Clear the box after printing
            dropZone.innerText = "Aye Drop your text/HTML file here or Paste words!";
        }
    }
});

dropZone.addEventListener('focus', () => {
    // If the box still has the default instruction, clear it
    if (dropZone.innerText.includes("Aye Drop your text")) {
        dropZone.innerText = "";
    }
});

// Optional: If the user clicks away and the box is empty, put the instructions back
dropZone.addEventListener('blur', () => {
    if (dropZone.innerText.trim() === "") {
        dropZone.innerText = "Aye Drop your text/HTML file here or Paste words!";
    }
});