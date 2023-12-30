function openModal() {
    document.getElementById('loginModal').style.display = 'block';
}

function closeModal() {
    var index = "https://dj.revelmyra.net"
    document.getElementById('loginModal').onclick = function (){
        location.href = index;
    }
}

window.onclick = function (event) {
    var modal = document.getElementById('loginModal');
    if (event.target === modal) {
        closeModal();
    }
}