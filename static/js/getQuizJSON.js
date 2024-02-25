document.addEventListener("DOMContentLoaded",function(){
    console.log("Loaded")
    var jsonData; // [{"name":.. "codes"...}...] 
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
          if (xhr.status === 200) {
            jsonData = JSON.parse(xhr.responseText);
            console.log('JSON data:', jsonData);
            displayQuestions();
          } else {
            console.error('Error fetching JSON data. Status code:', xhr.status);
            // Handle error or display a message to the user
          }
        }
      };
    
      xhr.open('GET', '/getQuiz', true);
      xhr.send();    

      //function displayQuestions
})