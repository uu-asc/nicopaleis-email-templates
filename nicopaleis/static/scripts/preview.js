// RENDER MESSAGES
for (let language of ['nl', 'en']) {
    let body = document.getElementById(valueName + '_' + language);
    body.onkeyup = () => render(language);
}

function render (language) {
    let body = document.getElementById(valueName + '_' + language);
    let preview = document.getElementById('preview_' + language);
    preview.innerHTML = marked(prime(body.value, language));
};

function prime (string, language) {
    // let stack = [parameters[language], snippets[language]];
    for (let item of stack) {
        let keys = Object.keys(item[language]);
        keys.sort();
        keys.reverse();
        for (let key of keys) {
            let regex = new RegExp('\\$' + key, 'g');
            string = string.replace(regex, item[language][key]);
        };
    };
    return string;
};
