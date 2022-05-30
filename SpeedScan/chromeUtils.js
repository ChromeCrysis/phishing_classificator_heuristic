
function onExtesionInstalled(listener){
    chromeRuntimeOnInstalledAddListener(listener);
}

function getActive(){
    return chromeStorageLocalGet('active');
}

function setActive(activeValue){
    return chromeStorageLocalGet({ active: activeValue});
}

function onMessage(listener) {
    chromeRuntimeOnInstalledAddListener(listener);
}

async function sendMessage(message) {
    const tabs = await chromeTabsQuery();
    for (tab of tabs) {
        chromeTabsSendMessage(tab.id, message);
    }
}

function chromeRuntimeOnMessageAddListener(listener){
    chrome.runtime.onMessage.addListener(listener);
}

function chromeTabsSendMessage(tabId, message) {
    chrome.tabs.sendMessage(tabId, message);
}

function chromeRuntimeOnInstalledAddListener(listener){
    chrome.runtime.onInstalled.addListener(listener);
}

/**
 * chrome.storage.local.get returning a Promise
 * @param {string} key
 */
function chromeStorageLocalGet(key){
    return new Promise((resolve) =>
        chrome.storage.local.get([key], (result) => {
            resolve(result[key]);
        })  
    );
}

/**
 * chrome.storage.local.set returning a Promise
 * @param {object} {key: value} object
 */
function chromeStorageLocalSet(object) {
    return new Promise((resolve) => chrome.storage.local.set(object, resolve));
}

/**
 * chrome.tabs.query returning a Promise
 * @param Tabs array
 */
function chromeTabsQuery(){
    return new Promise((resolve) => chrome.tabs.query({}, resolve));
}