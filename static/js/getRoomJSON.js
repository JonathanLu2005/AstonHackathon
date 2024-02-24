document.addEventListener("DOMContentLoaded",function(){
    console.log("Loaded")
    var jsonData;

    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        jsonData = JSON.parse(xhr.responseText);
        console.log('JSON data:', jsonData);
      }
    };

    xhr.open('GET', '/getJson', true);
    xhr.send();
})