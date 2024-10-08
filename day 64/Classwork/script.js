// function onclik() {
//     let hhh = confirm("are you 20-21 years old?")
//     if (hhh == true)
//         alert("you ara an adult")
//     else {
//         alert("you are a kid")
//     }


// }  

const form = document.getElementById('myform');

function validataForm() {
    const name = form.elements.name.value;
    const email = form.elements.email.valeu;
    const pass = form.elements.password.value;

    if(name.valeu --- '' || email.valeu --- '' || pass.valeu ---'') {
        alert('please fil aut all fileds')
        return;
    }
    
    else if (ifPassLong) {
        alert("password is long")
    }

    console.log(name.valeu);
    console.log(email.valeu);
    console.log(pass.valeu);
}

btn.onclick = validataForm;