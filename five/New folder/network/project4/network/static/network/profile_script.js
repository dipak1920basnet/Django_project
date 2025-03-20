document.addEventListener('DOMContentLoaded',()=>{
    m = document.querySelector('#Follow')
    user_id = m.getAttribute('data-id');
    fetch(`/follow/${user_id}`)
    .then(response => response.json())
    .then(check => 
    {
        console.log(`Lets check ${check.check_action}`)
        if (check.check_action == false){
            m.innerHTML = "Follow";
        }
        else{
            m.innerHTML = "UnFollow";
        }
    }
    )

    m.addEventListener('click',()=>
{
    let action = "unfollow"
    if (m.innerHTML == "Follow"){
        m.innerHTML = "Unfollow"
        action = "follow"

    }
    else{
        m.innerHTML = "Follow"
    }
    fetch(`/follow/${user_id}`,{
        method:'POST',
        body:JSON.stringify(
            {
                "action":action,
                "id":user_id,
            }
        )
    })
    .then(response => response.json())
    .then(result => {
        console.log(`${result}`)
    })
})
})