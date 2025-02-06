function rerouteRequest(details) {
  console.log("Request intercepted", details.url);
  return { redirectUrl: "https://example.com" };
}

// chrome.webRequest.onBeforeRequest.addListener(
//   rerouteRequest,
//   {
//     urls: ["https://www.avespfade.de/tiles/*/*/*.png"],
//   }
//   // ["blocking"]
// );
