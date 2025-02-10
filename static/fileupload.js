document.getElementById('form1').addEventListener('submit', function(x){
    x.preventDefault();
    const myFile = document.getElementById("uploadInput").files[0];
    const myData = new FormData();
    const csrfToken = document.querySelector('input[name="csrf_token"]').value;
    
    for (const file of uploadInput.files) {
        myData.append("file", file);
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