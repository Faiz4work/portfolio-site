

email_form = document.querySelector("#email-form")
email_form.addEventListener("submit", submitForm)


function submitForm(event){
    console.log("Submitted");
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let subject = document.getElementById("subject").value;
    let message = document.getElementById("message").value;
    let submit_button = document.getElementById("submit-button");
    let loading_gif = document.getElementById("loading_gif");

    loading_gif.style.display = 'inline-block';
    submit_button.style.display = 'none';
    email_form.reset()

    const req = new XMLHttpRequest();

    req.open('POST', '/email', true);
    req.setRequestHeader("Content-Type", "application/json");

    req.send(JSON.stringify({'name':name, 'email':email, 'subject':subject, 'message':message}));
    req.onload = function(){
        console.log(this.status);
        loading_gif.style.display = 'none';
        submit_button.style.display = 'inline-block';
        document.getElementsByClassName("sent-message")[0].style.display = 'block';
    };
    event.preventDefault();
};
