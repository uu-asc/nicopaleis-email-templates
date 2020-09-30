// GET VALUES
entries.addEventListener('keyup', selectEntry)
entries.addEventListener('click', selectEntry)
function selectEntry(event) {
    if (event.which !== 1 && event.key !== 'Enter') return;
    let entry = event.target.closest('.entry');
    if (entry === null) return;
    let label = entry.getElementsByClassName('entry--label')[0].innerText;
    if (typeof data[label] !== 'undefined') {
        let entries = document.getElementsByClassName('entry');
        // set/remove selected
        for(let i = 0; i < entries.length; i++) {
            entries[i].classList.remove('selected');
        }
        entry.classList.add('selected');
        // load data
        for (let field of fields) {
            let input = document.getElementById(field);
            input.disabled = false;
            input.value = data[label][field];
            if (input.type === 'checkbox' && data[label][field] === 'J') {
                input.checked = true;
            };
            input.setAttribute('name', label);
        };
        // MESSAGES
        if (typeof messageLogic == 'function') {
            messageLogic();
        };
    } else {
        initValues();
    };
};


// STORE ENTRY VALUES
for (let field of fields) {
    let input = document.getElementById(field);
    input.onblur = function () {saveValue(this, field)};
};


// PAGE INIT
function initValues() {
    for (let field of fields) {
        let input = document.getElementById(field);
        input.disabled = true;
        input.field = '';
    };
};
initValues()
