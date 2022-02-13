
// contact
let name = document.querySelector("#id_name");
let phone = document.querySelector("#id_phone");
let message = document.querySelector("#id_message");

let check = '[0-9]{2}[0-9]{3}[0-9]{4}';



function ContactForm() {
    if (phone.value.match(check)) {
        let d = {
            name: name.value,
            phone: phone.value,
            message: message.value
        }
        let data = JSON.stringify(d)
        if (window.XMLHttpRequest) {
        var xhttp=new XMLHttpRequest();
        } else {  // code for IE6, IE5
            var xhttp=new ActiveXObject("Microsoft.XMLHTTP");
        }
        xhttp.onreadystatechange = function() {
        if (xhttp.readyState === 4 && xhttp.status === 200) {
            var data = JSON.parse(this.responseText);
            // console.log(data['success'])
            if (data['success'] == 200) {
                // console.log('Bu Ishladi')
                let input = document.querySelectorAll('input');
                let textarea = document.querySelectorAll('textarea');
                let success = document.querySelector('#success');
                success.classList.add('info-modal-active');
                for (let i = 0; i < input.length; i++) {
                    input[i].value = ''
                }
                for (let i = 0; i < textarea.length; i++) {
                    textarea[i].value = ''
                }
            }
            else {
                let error = document.querySelector('#error');
                error.classList.add('info-modal-active');
            }
        }else{
    
        }
        }
        var url = "/contact/new/"
        xhttp.open("GET", url+`?data=${data}`, true);
        xhttp.send();
    }
    else {
        // name.classList.add('required');
        // phone.classList.add('required');
        // name.classList.add('required');
        let error = document.querySelector('#error');
        error.classList.add('info-modal-active');
    }
    
}

// Contest Register
let contest_name_register = document.querySelector("#id_name_contest_register");
let contest_age_register = document.querySelector("#id_age_contest_register");
let contest_phone_register = document.querySelector("#id_phone_contest_register");
let contest_message_register = document.querySelector("#id_message_contest_register");
let contest_experience_register = document.querySelector("#id_experience_contest");

function ContestRegister(id) {
    if (contest_phone_register.value.match(check)) {
        let d = {
            name: contest_name_register.value,
            phone: contest_phone_register.value,
            message: contest_message_register.value,
            experience: contest_experience_register.value,
            age: contest_age_register.value,
            id: id,
        }
        let data = JSON.stringify(d)
        if (window.XMLHttpRequest) {
        var xhttp=new XMLHttpRequest();
        } else {  // code for IE6, IE5
            var xhttp=new ActiveXObject("Microsoft.XMLHTTP");
        }
        xhttp.onreadystatechange = function() {
        if (xhttp.readyState === 4 && xhttp.status === 200) {
            var data = JSON.parse(this.responseText);
            // console.log(data['success'])
            if (data['success'] == 200) {
                // console.log('Bu Ishladi')
                let input = document.querySelectorAll('input');
                let textarea = document.querySelectorAll('textarea');
                let success = document.querySelector('#success');
                success.classList.add('info-modal-active');
                for (let i = 0; i < input.length; i++) {
                    input[i].value = ''
                }
                for (let i = 0; i < textarea.length; i++) {
                    textarea[i].value = ''
                }
            }
            else {
                let error = document.querySelector('#error');
                error.classList.add('info-modal-active');
            }
        }else{
    
        }
        }
        var url = "/contest/register/"
        xhttp.open("GET", url+`?data=${data}`, true);
        xhttp.send();
    }
    else {
        // name.classList.add('required');
        // phone.classList.add('required');
        // name.classList.add('required');
        let error = document.querySelector('#error');
        error.classList.add('info-modal-active');
    }
    
}

// Contest Question
let contest_name = document.querySelector("#id_name_contest");
let contest_phone = document.querySelector("#id_phone_contest");
let contest_message = document.querySelector("#id_message_contest");
let contest_age = document.querySelector("#id_age_contest");

function ContestQuestion(id) {
    if (contest_phone.value.match(check)) {
        let d = {
            name: contest_name.value,
            phone: contest_phone.value,
            message: contest_message.value,
            age: contest_age.value,
            id: id
        }
        let data = JSON.stringify(d)
        if (window.XMLHttpRequest) {
        var xhttp=new XMLHttpRequest();
        } else {  // code for IE6, IE5
            var xhttp=new ActiveXObject("Microsoft.XMLHTTP");
        }
        xhttp.onreadystatechange = function() {
        if (xhttp.readyState === 4 && xhttp.status === 200) {
            var data = JSON.parse(this.responseText);
            // console.log(data['success'])
            if (data['success'] == 200) {
                // console.log('Bu Ishladi')
                let input = document.querySelectorAll('input');
                let textarea = document.querySelectorAll('textarea');
                let success = document.querySelector('#success');
                success.classList.add('info-modal-active');
                for (let i = 0; i < input.length; i++) {
                    input[i].value = ''
                }
                for (let i = 0; i < textarea.length; i++) {
                    textarea[i].value = ''
                }
            }
            else {
                let error = document.querySelector('#error');
                error.classList.add('info-modal-active');
            }
        }else{
    
        }
        }
        var url = "/contest/question/"
        xhttp.open("GET", url+`?data=${data}`, true);
        xhttp.send();
    }
    else {
        // name.classList.add('required');
        // phone.classList.add('required');
        // name.classList.add('required');
        let error = document.querySelector('#error');
        error.classList.add('info-modal-active');
    }
    
}


////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////


////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////


// Event Register
let event_name_register = document.querySelector("#id_name_contest_register");
let event_age_register = document.querySelector("#id_age_contest_register");
let event_phone_register = document.querySelector("#id_phone_contest_register");
let event_message_register = document.querySelector("#id_message_contest_register");
let event_experience_register = document.querySelector("#id_experience_contest");

function EventRegister(id) {
    if (event_phone_register.value.match(check)) {
        let d = {
            name: event_name_register.value,
            phone: event_phone_register.value,
            message: event_message_register.value,
            experience: event_experience_register.value,
            age: event_age_register.value,
            id: id,
        }
        let data = JSON.stringify(d)
        if (window.XMLHttpRequest) {
        var xhttp=new XMLHttpRequest();
        } else {  // code for IE6, IE5
            var xhttp=new ActiveXObject("Microsoft.XMLHTTP");
        }
        xhttp.onreadystatechange = function() {
        if (xhttp.readyState === 4 && xhttp.status === 200) {
            var data = JSON.parse(this.responseText);
            // console.log(data['success'])
            if (data['success'] == 200) {
                // console.log('Bu Ishladi')
                let input = document.querySelectorAll('input');
                let textarea = document.querySelectorAll('textarea');
                let success = document.querySelector('#success');
                success.classList.add('info-modal-active');
                for (let i = 0; i < input.length; i++) {
                    input[i].value = ''
                }
                for (let i = 0; i < textarea.length; i++) {
                    textarea[i].value = ''
                }
            }
            else {
                let error = document.querySelector('#error');
                error.classList.add('info-modal-active');
            }
        }else{
    
        }
        }
        var url = "/event/register/"
        xhttp.open("GET", url+`?data=${data}`, true);
        xhttp.send();
    }
    else {
        // name.classList.add('required');
        // phone.classList.add('required');
        // name.classList.add('required');
        let error = document.querySelector('#error');
        error.classList.add('info-modal-active');
    }
    
}

// event Question
let event_name = document.querySelector("#id_name_event");
let event_phone = document.querySelector("#id_phone_event");
let event_message = document.querySelector("#id_message_event");
let event_age = document.querySelector("#id_age_event");

function EventQuestion(id) {
    if (event_phone.value.match(check)) {
        let d = {
            name: event_name.value,
            phone: event_phone.value,
            message: event_message.value,
            age: event_age.value,
            id: id
        }
        let data = JSON.stringify(d)
        if (window.XMLHttpRequest) {
        var xhttp=new XMLHttpRequest();
        } else {  // code for IE6, IE5
            var xhttp=new ActiveXObject("Microsoft.XMLHTTP");
        }
        xhttp.onreadystatechange = function() {
        if (xhttp.readyState === 4 && xhttp.status === 200) {
            var data = JSON.parse(this.responseText);
            // console.log(data['success'])
            if (data['success'] == 200) {
                // console.log('Bu Ishladi')
                let input = document.querySelectorAll('input');
                let textarea = document.querySelectorAll('textarea');
                let success = document.querySelector('#success');
                success.classList.add('info-modal-active');
                for (let i = 0; i < input.length; i++) {
                    input[i].value = ''
                }
                for (let i = 0; i < textarea.length; i++) {
                    textarea[i].value = ''
                }
            }
            else {
                let error = document.querySelector('#error');
                error.classList.add('info-modal-active');
            }
        }else{
    
        }
        }
        var url = "/event/question/"
        xhttp.open("GET", url+`?data=${data}`, true);
        xhttp.send();
    }
    else {
        // name.classList.add('required');
        // phone.classList.add('required');
        // name.classList.add('required');
        let error = document.querySelector('#error');
        error.classList.add('info-modal-active');
    }
    
}



