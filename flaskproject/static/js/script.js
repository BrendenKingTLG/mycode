const searchForm = document.getElementById("search-form")

searchForm.addEventListener('submit', (e) =>{
    e.preventDefault();
    const fd = new FormData(searchForm);
    const obj = Object.fromEntries(fd);
    let character = "/" + obj.search.toLowerCase();

    const frame = document.getElementById("frame");
    const newChar = document.createElement("iframe");

    newChar.setAttribute("src", character);
    frame.appendChild(newChar);

})
