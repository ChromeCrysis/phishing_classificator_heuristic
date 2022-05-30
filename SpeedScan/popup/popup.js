
const activeField = document.getElementById('active');
const saveButton = document.getElementById('save');

let initialState, state ={
    active: null
};

(async function () {
    state = await getInitialState();
    initialState = {...state}

    updateActiveField();
    addListenerActiveField();

    addListenerButton();
})();

async function getInitialState(){
    return {
        active: await getActive()
    }
}

//Active Field

function updateActiveField() {
    activeField.checked = state.active;
}

function addListenerActiveField(){
    activeField.onclick = (event) => {
        onActiveFieldClicked(event);

    }
}

function onActiveFieldClicked(event) {
    state.active = event.target.checked;
    updateActiveField();
}

//Button save

function addListenerButton(){
    saveButton.onclick = (event) => {
        onSaveButtonClick(event);
    }
}

async function onSaveButtonClick(event){
    setSavingText(event.target)
    if(state.active != initialState.active) await saveActive();
    initialState = { ...state};
}

function setSavingText(element){
    element.innerText = 'Salvando...';
    setTimeout(() => {
        element.innerText = 'Salvar';
    }, 300);
}

async function saveActive(){
    await setActive(state.active);
    if (state.active) await sendMessage('activate');
    else await sendMessage('deactivate');
}