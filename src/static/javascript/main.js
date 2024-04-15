function generatePassword() {
    var form = document.getElementById("passwordForm");
    var formData = new FormData(form);
    
    fetch('/generate', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(password => {
        document.getElementById("passwordDisplay").textContent = password;
        document.getElementById("message").textContent = "Password generated!";
        setTimeout(function() {
            document.getElementById("message").textContent = "";
        }, 3000);
    });
}

function copyToClipboard() {
    var passwordText = document.getElementById("passwordDisplay");
    var textarea = document.createElement("textarea");
    textarea.value = passwordText.textContent;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand("copy");
    document.body.removeChild(textarea);
    alert("Password copied to clipboard!");
}

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("length").addEventListener("input", function() {
        document.getElementById("lengthOutput").textContent = this.value;
    });

    document.getElementById("generateBtn").addEventListener("click", generatePassword);
});
