
chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
	var tab = tabs[0];
	var url = tab.url;
	// alert(url);

	const el = document.getElementById("site_score");
const el2 = document.getElementById("site_msg");
// responseText.innerText="Results will appear here"
fetch('http://localhost:5000/post', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded'
  },
  body: `URL=${url}`
})
.then(response => response.text())
.then(data => {
  console.log('Server response:', data);
  if (parseInt(data) == 1 ) {
	//alert('⚠️ WARNING ⚠️: Suspicious');
	console.log('1');
	  el.textContent = 'Suspicious';
	  el2.textContent = '⚠️ WARNING ⚠️:This site has been flagged as suspicious. Proceed with EXTREME caution!';
	  el.style.background = "linear-gradient(45deg, #a64812, #e1e354);";
	  el.style.transform = "translateZ(25px)";
	  var element = document.querySelector('.rounded-circle');
	  element.style.background = "#ffa500";

	
  } else if (parseInt(data) == 0 ) {
	//alert('Safe');
	console.log('0');
	el.textContent = 'Safe';
	el2.textContent = '✅ This website is safe to use';
	el.style.background = "linear-gradient(45deg, #00db2f, #06678b)";
	el.style.transform = "translateZ(25px)";
	
  } else if (parseInt(data) == -1 ) {
	//alert('⚠️ WARNING ⚠️: Phishing');
	console.log('-1');
	el.textContent = 'Phishing'
	el2.textContent = '⚠️ WARNING ⚠️: This site has been identified as a phishing site. Do not proceed further!';
	el.style.background = "linear-gradient(45deg, #900000, #6d6f08);";
	el.style.transform = "translateZ(25px)";
	var element = document.querySelector('.rounded-circle');
    element.style.background = "#ff0000";
  }
})
.catch(error => {
  console.error('Fetch error:', error);
});
    });
