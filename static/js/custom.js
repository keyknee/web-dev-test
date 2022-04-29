function getUsername() {
    var x = document.getElementById("username").value;
}


/*
User Account menu button controls
*/
var usr_mnu = document.getElementById('user-menu');

function toggleUserMenu() {
    usr_mnu.classList.toggle('user-menu');
}

document.getElementById('user-dropdown-button').addEventListener('click', toggleUserMenu);