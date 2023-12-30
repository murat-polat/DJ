function openModal() {
    document.getElementById('registerModal').style.display = 'block';
}

function closeModal() {
    var index = "https://dj.revelmyra.net"
    document.getElementById('registerModal').onclick = function () {
        location.href = index;
}
}

window.onclick = function (event) {
    var modal = document.getElementById('registerModal');
    if (event.target === modal) {
        closeModal();
    }
}