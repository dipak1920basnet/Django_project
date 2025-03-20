// Working With Variables
var age = 20;
// let counter = 1;
const PI = 3.14;

// let counter = 0;
if (!localStorage.getItem('counter'))
{
    localStorage.setItem('counter',0);
}
function count()
{
    let counter = localStorage.getItem('counter');
    counter ++;
    //Why do I need two manipulation of h1 here 
    document.querySelector('h1').innerHTML = counter;
    localStorage.setItem('counter',counter);
    if (counter % 10 == 0)
{
    alert(` Count is now ${counter}`)
}
}

document.addEventListener('DOMContentLoaded', function(){
    // and here manipulation here??
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    document.querySelector('button').onclick = count;
    // setInterval(count,1000);
})




// Counter using arrow functions 

// count = () =>
// {
//     counter ++;
//     document.querySelector('h1').innerHTML = counter;

//     if (counter % 10 === 0){
//         alert(`Count is now ${counter}`)
//     }
// }


// let counter = 0
// function count()
// {
//     counter ++;
//     document.querySelector('h1').innerHTML = counter;
// }

// document.addEventListener('DOMContentLoaded', function()
// {
//     document.querySelector('button').onclick = count;
//     setInterval(count,1000);
// })

