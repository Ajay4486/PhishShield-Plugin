chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  var prediction = request.prediction;
  console.log(prediction)
  if (prediction == 1){
      alert("⚠️ WARNING ⚠️: This site has been flagged as suspicious. Proceed with EXTREME caution!");
  }
  else if (prediction == -1){
      alert("⚠️ WARNING ⚠️: This site has been identified as a phishing site. Do not proceed further!");
  }
  else if (prediction == 0){
      alert("✅ This site is safe to visit.");
  }
});
