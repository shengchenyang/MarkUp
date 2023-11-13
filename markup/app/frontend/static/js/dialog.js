document.addEventListener('keydown', function (event) {
    if (event.key === 'F5') {
        event.preventDefault();
    }
});

const iframe = document.querySelector('iframe');
iframe.setAttribute('sandbox', 'allow-same-origin allow-scripts allow-popups allow-forms allow-top-navigation-by-user-activation');
iframe.setAttribute('src', '');

function showPopup() {
    document.getElementById('overlay').style.display = 'block';
    document.getElementById('popup').style.display = 'block';
}

function hidePopup() {
    document.getElementById('overlay').style.display = 'none';
    document.getElementById('popup').style.display = 'none';
}

Object.assign(window, {
    showPopup: showPopup,
    hidePopup: hidePopup,
});
