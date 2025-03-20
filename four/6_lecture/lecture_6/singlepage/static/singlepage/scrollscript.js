window.onscroll = () =>
{
    // Check if we are at the bottom

    if (window.innerHeight + window.scrollY >= document.body.offsetHeight)
    {
        // Change color to green
        document.querySelector('body').style.background = "green";
    }
    else
    {
        document.querySelector('body').style.background = 'white';
    }
}