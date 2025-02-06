async function getCurTab() {
  return (await chrome.tabs.query({ active: true, currentWindow: true }))[0];
}

async function main() {
  let curTab = await getCurTab();

  chrome.scripting.executeScript({
    target: { tabId: curTab.id },
    func: () => alert("Hello from the content script!"),
  });
}

main();
