document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function(x){
        x.preventDefault();
        const uploadInput = this.querySelector('input[type="file"]');
        const myData = new FormData();
        const csrfToken = this.querySelector('input[name="csrf_token"]').value;
        
        for (const file of uploadInput.files) {
            myData.append("file", file, file.webkitRelativePath || file.name);
        }
        myData.append("csrf_token", csrfToken);
        
        fetch('/upload', {
            method: "POST",
            body: myData
        })
        .then(response => {
            if (!response.ok) {
                return response.text().then(text => {
                    throw new Error(`Upload failed: ${text}`);
                });
            }
            return response.json();
        })
        .then(finalData => {
            console.log("File has been uploaded successfully");
        })
        .catch(err => {
            console.log("Error Found:", err);
        });
    });
});