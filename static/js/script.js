let gooseX=window.innerWidth;
var correctAnswers=0;
var qsAnswered=0;
document.addEventListener("domContentLoaded",main())


function main(){
  demoQs=JSON.parse(document.getElementById("output").innerHTML);
  console.log(demoQs.questions)


  let qIndex=0;
  let q_text = document.getElementById("q-text");
  let a1_text = document.getElementById("a1-text")
  let a2_text = document.getElementById("a2-text")
  let a3_text = document.getElementById("a3-text")
  let a4_text = document.getElementById("a4-text")
  let score_text = document.getElementById("score-text")
  let currentq;
  function update(){
    q_text.innerHTML = demoQs.questions[qIndex].question
    a1_text.innerHTML = demoQs.questions[qIndex].answers[0]
    a2_text.innerHTML = demoQs.questions[qIndex].answers[1]
    a3_text.innerHTML = demoQs.questions[qIndex].answers[2]
    a4_text.innerHTML = demoQs.questions[qIndex].answers[3]
    score_text.innerHTML=`${correctAnswers} / ${qsAnswered}`
    currentq = demoQs.questions[qIndex]
  }
  update();
  let a1_box = document.getElementById("a1-box")
  let a2_box = document.getElementById("a2-box")
  let a3_box = document.getElementById("a3-box")
  let a4_box = document.getElementById("a4-box")

  a1_box.addEventListener("click", function() {
    answerClicked(currentq.correct_answer == currentq.answers[0]);
  });
  a2_box.addEventListener("click", function() {
answerClicked(currentq.correct_answer == currentq.answers[1]);  });
  a3_box.addEventListener("click", function() {
    answerClicked(currentq.correct_answer == currentq.answers[2]);
  });
  a4_box.addEventListener("click", function() {
    answerClicked(currentq.correct_answer == currentq.answers[3]);
  });  
  function answerClicked(isCorrect){
    qsAnswered++;
    if(isCorrect){
      correctAnswers++;
    }
    qIndex= (qIndex+1)%demoQs.questions.length;
    update();
  }
}
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');

const spriteWidth = 64; // Width of each frame in the sprite
const spriteHeight = 64; // Height of each frame in the sprite
const spriteFrames = 17; // Total number of frames in the sprite

const spriteImage = new Image();
spriteImage.src = '/static/assets/BackGroundGoose.png'; // Replace with the actual path to your sprite image

let frameIndex = 0;
let frameCounter = 0;

function animate() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Draw the current frame of the sprite
  ctx.drawImage(
    spriteImage,
    frameIndex * spriteWidth, //Source x
    0, //Source Y
    spriteWidth, //Source Width
    spriteHeight, //Source Height
    gooseX, //Destination X
    0, //Destination Y
    spriteWidth*3, //Destination Width
    spriteHeight*3 //Destination Height
  );

  // Update frame index for the next iteration
  frameIndex = (frameIndex + 1) % spriteFrames;

  // Increase the frame counter
  frameCounter++;
if(gooseX<-spriteWidth*3){
    gooseX = canvas.width;
}else if(gooseX>(canvas.width-spriteWidth*3*correctAnswers)){
    gooseX=gooseX-3;
}

  // Request the next animation frame
  requestAnimationFrame(animate);
}

// Load the sprite image and start the animation when it's loaded
spriteImage.onload = function () {
    
  animate();
  canvas.width = window.innerWidth;
  
};

var audio = document.getElementById('audioPlayer');
var playButton = document.getElementById('playButton');
var pauseButton = document.getElementById('pauseButton');

playButton.addEventListener('click', function() {
    audio.play();
});

pauseButton.addEventListener('click', function() {
    audio.pause();
});