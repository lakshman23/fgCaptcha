function validate() {
    var x = "true";
    if(document.getElementById('password').value!="trio" ||document.getElementById('admin').value!="trio"){
        document.getElementById('invalid').innerHTML = "invalid user name or password";
        x = false;
        return x;
    }
    else {
    	return x;
    }
}