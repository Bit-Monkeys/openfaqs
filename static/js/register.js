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
