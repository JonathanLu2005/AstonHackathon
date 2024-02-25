document.addEventListener("DOMContentLoaded",function(){
    console.log("Loaded")
    var jsonData; // [{"name":.. "codes"...}...] 
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
          if (xhr.status === 200) {
            jsonData = JSON.parse(xhr.responseText);
            console.log('JSON data:', jsonData);
            addToWebpage();
          } else {
            console.error('Error fetching JSON data. Status code:', xhr.status);
            // Handle error or display a message to the user
          }
        }
      };
    
      xhr.open('GET', '/getJson', true);
      xhr.send();

    let listRooms = document.getElementById("list-rooms")
    function addToWebpage() {
        for (let i = 0; i < jsonData.length; i++) {
          // Create a div element
          var roomDiv = document.createElement('div');
          roomDiv.className = 'room';
    
          // Create a paragraph element
          var paragraph = document.createElement('p');
          paragraph.textContent = 'Name: ' + jsonData[i].name + ' Code: ' + jsonData[i].codes;
    
          // Append the paragraph to the div
          roomDiv.appendChild(paragraph);
    
          // Append the div to the listRooms
          listRooms.appendChild(roomDiv);
        }
      }
    
})