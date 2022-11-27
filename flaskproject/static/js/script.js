const searchForm = document.getElementById("search-form")

searchForm.addEventListener('submit', (e) =>{
    e.preventDefault();
    const fd = new FormData(searchForm);
    const obj = Object.fromEntries(fd);
    let character = "/" + obj.search.toLowerCase();

    const frame = document.getElementById("frame");
    const newChar = document.createElement("iframe");

    // currentIFrame = document.getElementById("iframe")
    // if (currentIFrame!= ""){
    //     frame.removeChild(currentIFrame)
    // }
    frame.innerHTML = "";
    newChar.setAttribute("src", character);
    frame.appendChild(newChar);

})
