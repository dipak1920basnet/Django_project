document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');

  // Send email:
  document.querySelector("#compose-form").addEventListener("submit",send_email);
  // load_mailbox('sent');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3  id='option_box'>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  fetch(`/emails/${mailbox}`)
.then(response => response.json())
.then(emails => {
    // Print emails
    console.log(emails);

    // ... do something else with emails ...
    loaded_email = document.createElement('div')
    loaded_email.setAttribute('id','emails')
    loaded_email.style.border = 'solid grey'
    document.querySelector("#emails-view").append(loaded_email);
    emails.forEach(display_email);
});
}

function send_email(event)
{
  event.preventDefault();

  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: document.querySelector("#compose-recipients").value,
        subject: document.querySelector("#compose-subject").value,
        body: document.querySelector("#compose-body").value,
    })
  })
  .then(response => response.json())
  .then(result => {
      // Print result
      console.log(result);
  }).then(()=>{
    load_mailbox('inbox')});
  
}

function display_email(contents){
  // Create a button, set class and then set text content 
  const view_email = document.createElement('div');
  view_email.setAttribute('class',"view_email")
  //Each email appears with border
  view_email.style.border = 'solid grey'
  
  view_email.style.margin = '10px'
  view_email.style.padding = '20px'
  view_email.innerHTML = `Sender: ${contents.sender}, Title: ${contents.subject},  Time: ${contents.timestamp} `
  document.querySelector("#emails").append(view_email);
  

    // adds functionality of clicking and view email
  view_email.addEventListener('click', function() {
    view_email_detail(contents.id)
  
}
)
// Change the color to  grey when email has been clicked to read
if (contents.read == false)
  {
    view_email.style.backgroundColor = 'white'
  }
  else{
    view_email.style.backgroundColor = 'grey'
  }}


// Adds feature to reply to email:
// function reply_email (sender, timestamp, subject, body){
  function reply_email(email){
  reply = document.querySelectorAll('.reply')
  reply.forEach(function(button) {
    
    button.onclick = function()
    {
      const sender = email.sender
      const subject = email.subject
      // Show the compose box and hide other views
      document.querySelector('#emails-view').style.display = 'none';
      document.querySelector('#compose-view').style.display = 'block';
      document.querySelector('#compose-recipients').value = sender;
      document.querySelector('#compose-subject').value = subject;
//       document.querySelector('#compose-body').value = `On ${timestamp} ${sender} wrote: ${body}
// .......`
document.querySelector('#compose-body').value = `On ${email.timestamp} ${sender} wrote: ${email.body}
.......`
    }
  })
}

// Adds feature to view email in detail:

function view_email_detail(id){
  document.querySelector('#emails-view').style.display = 'none';
  
  // title.textContent = contents.subject
  // console.log("Hello WORld")
      fetch(`/emails/${id}`)
    .then(response => response.json())
    .then(email => {
        // Print email
        console.log(email);

        // ... do something else with email ...
        const view_detail = document.createElement('div');
        view_detail.setAttribute('class',"view_detail")
        const title = document.createElement('h1')
        title.textContent = `${email.subject}`

        // See content of email
        const content = document.createElement('div')
        content.setAttribute('class','email_content')

        // add archive button
        const option_heading = document.querySelector("#option_box")
        // Check if the email is sent by user 
        if (option_heading.textContent != "Sent")
        {
            // add reply button to email
          const reply_button = document.createElement('button')
          reply_button.setAttribute('class','reply')
          reply_button.textContent = "Reply"
          content.append(reply_button)
           
          // if the email is sent by user then usen can't archive so archive option is not available
          const archive_button = document.createElement('button')
          archive_button.setAttribute('class','archive')
          if (option_heading.textContent == "Archive")
            {archive_button.textContent = "UnArchive"}
          else
          {
            archive_button.textContent = "Archive"
          }
          content.append(archive_button)
        }

        view_detail.append(title, content)

        document.querySelector("#emails-view").append(view_detail);
        document.querySelector("#emails").style.display = 'none';
        document.querySelector('#emails-view').style.display = 'block';

        // change email from unread to read
        fetch(`/emails/${id}`, {
          method: 'PUT',
          body: JSON.stringify({
              read: true
          })
        })
        reply_email(email)
        archive_email(id)
    });
    
  }

// Adds feature to archive email:

function archive_email(id)
{
  let archived_email = document.querySelector('.archive')
  archived_email.addEventListener('click', ()=>{
    if (archived_email.textContent == "Archive" ){
      archived_email.textContent = "UnArchive"
      // archive email
      fetch(`/emails/${id}`, {
        method: 'PUT',
        body: JSON.stringify({
            archived: true
        })
      })
      .then(()=>{
        load_mailbox('inbox')
      })
    }
    else{
      archived_email.textContent = "Archive"
            // archive email
            fetch(`/emails/${id}`, {
              method: 'PUT',
              body: JSON.stringify({
                  archived: false
              })
            })
            .then(()=>{
              load_mailbox('inbox')
            })
    }
  })
}
