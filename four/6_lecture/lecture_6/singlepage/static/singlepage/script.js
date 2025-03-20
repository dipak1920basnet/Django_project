window.onpopstate = function(event){
    console.log(event.state.section);
    showSection(event.state.section);
}
function showSection(section){
    fetch(`/sections/${section}`)
    .then(response => response.text())
    .then(text =>{
        console.log(text);
        document.querySelector("#content").innerHTML = text;
    });
}
document.addEventListener('DOMContentLoaded',function(){
    //Add a button functionality
    document.querySelectorAll('button').forEach(button => {
        button.onclick = function()
        {
            // showSection(this.dataset.section);
            const section = this.dataset.section;
            // Add the current state to the history
            history.pushState({section:section},"", `section${section}`);
            showSection(section);
        };
    });
});