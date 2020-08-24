// GET VALUES
entries.addEventListener('keyup', selectEntry)
entries.addEventListener('click', selectEntry)
function selectEntry(event) {
    if (event.which !== 1 && event.key !== 'Enter') return;
    let entry = event.target.closest('.entry');
    let label = entry.getElementsByClassName('entry--label')[0].innerText;
    if (typeof data[label] !== 'undefined') {
        let entries = document.getElementsByClassName('entry');
        // set/remove selected
        for(let i = 0; i < entries.length; i++) {
            entries[i].classList.remove('selected');
        }
        entry.classList.add('selected');
        // load data
        for (let value of values) {
            let input = document.getElementById(value);
            input.disabled = false;
            input.value = data[label][value];
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
for (let value of values) {
    let input = document.getElementById(value);
    input.onblur = function () {saveValue(this, value)};
};


// PAGE INIT
function initValues() {
    for (let value of values) {
        let input = document.getElementById(value);
        input.disabled = true;
        input.value = '';
    };
};
initValues()
