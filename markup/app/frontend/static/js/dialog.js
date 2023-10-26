document.addEventListener('keydown', function (event){
    if (event.key === 'F5') {
        event.preventDefault();
    }
});

function showPopup(){
    document.getElementById('overlay').style.display = 'block';
    document.getElementById('popup').style.display = 'block';
}

function hidePopup(){
    document.getElementById('overlay').style.display = 'none';
    document.getElementById('popup').style.display = 'none';
}

Object.assign(window, {
  showPopup: showPopup,
  hidePopup: hidePopup,
});
