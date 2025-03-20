document.addEventListener('DOMContentLoaded',()=>
{
    let m = document.querySelectorAll('.edit button');
    m.forEach(function(button){
        button.addEventListener('click', function()
        {
            let postContainer = this.closest(".content");
            let post = postContainer.querySelector(".post");
            let edit_post = postContainer.querySelector(".edit_post");
                edit_post.style.display = "block";
            let access_form = edit_post.querySelector("textarea")
            let save_form = postContainer.querySelector(".Save_input")
            access_form.value = post.innerText.trim();
            save_form.addEventListener('click',function(event)
            {
                event.preventDefault();
                console.log(`${access_form.value}`)
                post.innerText = access_form.value;
                edit_post.style.display="none";

            });
        })
        
    });
}
)

document.addEventListener('DOMContentLoaded',()=>
{
    // Working with like button
    let like = document.querySelectorAll('.control_like');
    like.forEach(function(button){
        button.addEventListener('click', function(){
            let postContainer = this.closest(".content");
            let like_portion = postContainer.querySelector('.Like')
            let post_id = like_portion.querySelector(".control_like").getAttribute('data-id')

            let update_like = like_portion.querySelector(".update_like")
            console.log(post_id)
            const url = `/like/${post_id}`
            fetch(url, {
                method:'POST',
                body:JSON.stringify({
                    "id":post_id,
                })
            })
            .then(response => response.json())
            .then(result => {
                console.log(result)
            })


            if (like_portion.querySelector('.control_like').style.color != "red")
            {
                like_portion.querySelector('.control_like').style.color = "red"
                // press_like.innerText = `${parseInt(press_like.innerText.split(':')[1])+1}`;
                update_like.innerText = `${parseInt(update_like.innerText)+1}`;

            }
            else{
                like_portion.querySelector('.control_like').style.color = "initial";
                // press_like.innerText = `${parseInt(press_like.innerText.split(':')[1])-1}`;
                update_like.innerText = `${parseInt(update_like.innerText)-1}`;
            }
            
            
        })
    }
        
        )

})