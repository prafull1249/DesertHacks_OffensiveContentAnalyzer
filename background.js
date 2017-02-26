
//console.log("bg.js");

chrome.contextMenus.create({

	title : "Harrassment Analyser",
	contexts: ['selection'],
	onclick: myFunction 


});

//diff context menus - selection , link , image, page


function myFunction(selectedText){

	alert(selectedText.selectionText);
	//chrome.tabs.create({ url : "https://twitter.com/intent" })
	//chrome.windows.create({ url : "https://www.google.com", type: "panel"});
	//var xhttp = new XMLHttpRequest();
   // var response = JSON.parse(xhttp.responseText);
  // console.log("myFunction");
var xhr = new XMLHttpRequest();
var query = selectedText.selectionText.toString();
xhr.open("GET", "http://10.2.65.195:8081/?search="+query,false);
xhr.send();
var response = xhr.responseText;//JSON.stringify(xhr.responseText);
console.log(response)
//console.log(response);


    



}