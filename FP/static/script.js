const dropArea = document.getElementById("drop-zone");
const inputFile = document.getElementById("input-file");
const imageView = document.getElementById("img-view");

dropArea.addEventListener("dragover", function(e) {
    e.preventDefault();
});

dropArea.addEventListener("drop", function(e){
    e.preventDefault();
    inputFile.files = e.dataTransfer.files;
});

document.getElementById("form").onchange = function() {
    document.getElementById("form").submit();
};

inputFile.addEventListener("change", uploadImage);

function uploadImage(){
    let imgLink = URL.createObjectURL(inputFile.files[0]);
    imageView.style.backgroundImage = 'url(${imgLink})';
};

['dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, highlight, false)
});

['drop'].forEach(eventName => {
    dropArea.addEventListener(eventName,unhighlight,false)
})

function highlight(e) {
    dropArea.classList.add('highlight')
}

function highlight(e) {
    dropArea.classList.remove('highlight')
}

