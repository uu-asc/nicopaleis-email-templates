const entries  = document.getElementById('entries');
const addition = document.getElementById('addition');
const search   = document.getElementById('search');
const submit   = document.getElementById('submit');
const regex    = RegExp('[^a-zA-Z_\d]+');


// SEARCH ENTRIES
search.addEventListener('keyup', filterEntries);
function filterEntries() {
    let filter = search.value.toLowerCase();
    if (entries) {
        let rows = entries.getElementsByClassName('entry');
        for (let i = 0; i < rows.length; i++) {
            let col = rows[i].getElementsByClassName('entry--label')[0].innerText.toLowerCase();
            let match;
            if (filter.startsWith('$')) {
                match = (data[col][valueName + '_nl'].includes(filter)||data[col][valueName + '_en'].includes(filter))
            } else {
                match = col.indexOf(filter) > -1
            };
            if (match) {
                rows[i].style.display = '';
            } else {
                rows[i].style.display = 'none';
            };
        };
    };
};


// SAVE ENTRIES
document.onkeydown = detectCtrlS
function detectCtrlS (event) {
    if (event.ctrlKey && event.key === 's') {
        event.preventDefault();
        sendData();
    };
};
submit.onclick = sendData
function sendData () {
    fetch(page, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(data),
        cache: "no-cache",
        headers: new Headers({"content-type": "application/json"})
    }).then(response => {
        if (response.ok) {
            displayFlash('saved...')
        };
    }).catch(function(err) {
        console.info(err + ' url: ' + url);
    });
};


// ADD ENTRIES
function addEntry () {
    // get new parameter name
    let entry = addition.value.toLowerCase();
    // test entry and add if valid
    if (entry === '') {
        displayFlash('entry cannot be an empty string...');
    } else if (regex.test(entry)) {
        displayFlash('entry may only contain the following characters: 0-9, a-z and _');
    } else if (entry in data) {
        displayFlash('entry already exists...');
    } else if (entry.length > maxchar) {
        displayFlash(`entry cannot contain more than ${maxchar} characters`);
    } else {
        let div = document.createElement('div');
        div.className = 'entry';
        div.tabIndex = '0';
        div.innerHTML = template.replace(/\?/g, entry);
        entries.insertBefore(div, entries.childNodes[0]);
        let initialization = {};
        for (let field of fields) {
            initialization[field] = '';
        };
        data[entry] = initialization;
    };
    // empty input value
    addition.value = '';
}


// REMOVE ENTRIES
function removeEntry (input) {
    let entry = input.parentNode.firstElementChild.innerText;
    delete data[entry];
    input.parentNode.remove();
}

// enter triggers input add-entry
addition.addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
        addEntry();
    };
});


// STORE ENTRY VALUES
function saveValue (element, destination) {
    let entry = element.getAttribute('name');
    if (element.type === 'checkbox') {
        if (element.checked === true) {
            data[entry][destination] = 'J';
        } else {
            data[entry][destination] = 'N';
        };
    } else {
        let value = element.value;
        data[entry][destination] = value;
    };
};
