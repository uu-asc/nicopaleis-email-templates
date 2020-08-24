const collapsibles = document.getElementsByClassName('collapsible');
function collapsePanel (element) {
    let content = element.previousElementSibling;
    if (content.style.display !== 'none'){
        content.style.display = 'none';
        element.innerHTML = '&#9654;';
    } else {
        content.style.display = 'flex';
        element.innerHTML = '&#9664;';
    };
};

for (let i = 0; i < collapsibles.length; i++) {
    collapsibles[i].addEventListener('click', function() {
        collapsePanel(this);
    });
};
