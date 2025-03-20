let counter = 1;
const quantity  = 20;
document.addEventListener("DOMContentLoaded",load);
window.onscroll = () =>
{
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight)
    {
        load();
    }
}

// load next set of posts

function load()
{
    // Set start and end post numbers, and update counter
    const start = counter;
    const end = start + quantity - 1;
    counter = end + 1

    // Get new posts and add posts
    fetch(`/posts?start=${start}&end=${end}`)
    .then(response => response.json())
    .then(data => {
        // console.log("Received data:", data);
        data.posts.forEach(add_post);
    })
}

// Add a new post with given contents to DOM

function add_post(contents)
{
    const post = document.createElement('div');
    post.className = 'post';
    post.innerHTML = `${contents} <button class="hide">Hide</button>`;

    // Add post to DOM
    document.querySelector('#posts').append(post);
}

// if hide button is clicked then delete the post

document.addEventListener('click', event => {
    
    // Find what was clicked on 
    const element = event.target;

    // Check if the user clicked on a hide button

    if (element.className === 'hide')
    {
        element.parentElement.style.animationPlayState = 'running';
        element.parentElement.addEventListener('animationend', () => {
            element.parentElement.remove();
        })
        
    }
})
