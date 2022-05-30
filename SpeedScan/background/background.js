onExtesionInstalled(setInitial);

function setInitial(){
    setInitialActive();
}

async function setInitialActive(){
    const active = await getActive();
    if (active == null) await setInitialActive(true);
}