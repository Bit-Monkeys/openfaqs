function checkPass()
	{
		var pass1 = document.getElementById('password1') 
		var pass2 = document.getElementById('password2') 

		var pass1div = document.getElementById('passwordDiv1') 
		var pass2div = document.getElementById('passwordDiv2')

		var pass2help = document.getElementById('password2help') 

		if (pass1.value == pass2.value) {
			pass1div.className = 'col-xs-10 has-success'
			pass2div.className = 'col-xs-10 has success'
			pass2help.innerHTML = 'Passwords match' 
		}
		else { 
			pass1div.className = 'col-xs-10 has-warning'
			pass2div.className = 'col-xs-10 has-warning'
			pass2help.innerHTML = "Passwords do not match."
	}
}

function checkUsername() {
    var username = document.getElementById("username").value
    $.get("http://localhost:5000/ajax/checkusername", {
        username: username
    }, function(resp) {
    if (resp == "False") {
        document.getElementById('usernameDiv').className = 'col-xs-10 has-warning';
        document.getElementById('usernamehelp').innerHTML = 'Username is not available.'
    }
    else {
        document.getElementById('usernameDiv').className = 'col-xs-10 has-success';
        document.getElementById('usernamehelp').innerHTML = 'Username is available.'
    }
    });
}