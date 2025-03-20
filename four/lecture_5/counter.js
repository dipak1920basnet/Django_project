function new_hello()
    {
        alert('Hello, world!')
    }
let counter = 0;
function count()
    {
        counter ++;
        if (counter % 10 === 0)
        {
            alert(`The count has reached ${counter}`);
        }
        new_counter = document.querySelector('h2');
        new_counter.innerHTML = counter;

        document.addEventListener('DOMContentLoaded', function()
        {
            document.querySelector('button').onclick = count;
        });
        
    }
function hello()
    {
        const header = document.querySelector('h1');
        if (header.innerHTML == "Hello!")
        {
            header.innerHTML = "Goodbye!"
        }
        else
        {
            header.innerHTML = "Hello!"
        }

    }

document.addEventListener("DOMContentLoaded", function(){
        document.querySelector('form').onsubmit = function()
        {
            const name = document.querySelector('#name').value;
            alert(`Hello, ${name}`);
        };
    })

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.coloring').forEach(function(button){
        button.onclick = function(){
            document.querySelector("#hello").style.color = button.dataset.color;
        }
    })
})

// Working with Arrow functions
document.addEventListener('DOMContentLoaded', ()=>{
    document.querySelectorAll('.coloring').forEach(button => {
        button.onclick = () => {
            document.querySelector('#hello').style.color = button.dataset.color;
        }
    })
})

if (!localStorage.getItem('counter'))
{
    localStorage.setItem('counter',0);
}
new_count = ()=> {
    counter++;
    document.querySelector('h1').innerHTML = counter;
    if (counter % 10 === 0)
    {
        alert(`Count is now ${counter}`)
    }
    let counter = localStorage.getItem('counter');
    counter++;
    document.querySelector('h1').innerHTML = counter;
    localStorage.setItem('counter')

}


document.addEventListener('DOMContentLoaded', function()
{
    document.querySelector('select').onchange = function(){
        document.querySelector('#new_hello').style.color = this.value;
    }
})


document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    document.querySelector('button').onclick = count;
    // setInterval(count, 1000);
    
});

