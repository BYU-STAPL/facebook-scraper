var usernameEl = document.getElementById("username");
var passwordEl = document.getElementById("password");
var formEl = document.getElementById("form");

var username = '';
var password = '';

usernameEl.addEventListener('change', (event)=>{
    username = event.target.value;
})

passwordEl.addEventListener('change', (event)=>{
    password = event.target.value;
})

formEl.addEventListener('submit', (event)=>{
    event.preventDefault();
    fetch('/api/login', { 
        method:'POST', 
        headers: { 'Content-Type':'application/json' },
        body: JSON.stringify({ username, password })
    })
    .then((response)=>response.json())
    .then((data)=>console.log(data))
})

