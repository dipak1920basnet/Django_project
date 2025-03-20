document.addEventListener('DOMContentLoaded', function(){
    const submit = document.querySelector('#submit');
    const newTask = document.querySelector('#task');

    // Disable submit button by default;
    submit.disabled = true;

    newTask.onkeyup = () => {
        if (newTask.value.length > 0)
        {
            submit.disabled = false;
        }
        else
        {
            submit.disabled = true;
        }
    }

    // Listen for sbumission of form
    document.querySelector('form').onsubmit = () =>
    {
        const task = newTask.value;

        const li = document.createElement('li');
        li.innerHTML = task;

        document.querySelector('#tasks').append(li);

        newTask.value = '';
        submit.disabled = true;

        return false;
    }
})