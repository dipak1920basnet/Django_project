document.addEventListener('DOMContentLoaded', function()
{
    // Send a GET request to a url
    fetch('https://api.exchangeratesapi.io/latest?base=USD')
    //Put response into json form
    .then(response => response.json())
    .then(data => {
        // Log data to the console
        console.log(data);
    })
})