let gooseX=window.innerWidth;
var correctAnswers=0;
var qsAnswered=0;
document.addEventListener("domContentLoaded",main())


function main(){
  const demoQs = {
    "questions": [
      {
        "question": "What is the sum of the geometric series with |r| < 1?",
        "options": ["1/(1 + r)", "1/(1 - r)", "(1 - r)/r", "(1 + r)/r"],
        "answer": "1/(1 - r)"
      },
      {
        "question": "What does .a1a2a3 ... represent?",
        "options": ["An integer", "A rational number", "An irrational number", "A complex number"],
        "answer": "A rational number"
      },
      {
        "question": "How is the sum of the series Pan/10n obtained?",
        "options": ["Through Integration", "Using the Comparison Test", "Using Differentiation", "Using the Ratio Test"],
        "answer": "Using the Comparison Test"
      },
      {
        "question": "What does a terminating decimal represent?",
        "options": ["A rational number", "An irrational number", "An integer", "A prime number"],
        "answer": "A rational number"
      },
      {
        "question": "What is the repeating decimal 0.5910˙ 2 expressed as a quotient of two integers?",
        "options": ["59043/99900", "59102/99999", "59100/100000", "591/999"],
        "answer": "59043/99900"
      },
      {
        "question": "How are irrational numbers represented in decimal expansions?",
        "options": ["As repeating decimals", "As terminating decimals", "As non-repeating decimals", "As integers"],
        "answer": "As non-repeating decimals"
      },
      {
        "question": "How can the decimal expansion of an arbitrary real number be computed?",
        "options": ["Using the division algorithm", "Using long division", "Through integration", "By differentiation"],
        "answer": "Using the division algorithm"
      },
      {
        "question": "What type of numbers do terminating and repeating decimal expansions represent?",
        "options": ["Rational numbers", "Irrational numbers", "Real numbers", "Complex numbers"],
        "answer": "Rational numbers"
      },
      {
        "question": "What does the division algorithm help in computing for rational numbers?",
        "options": ["Quotient and Remainder", "Exponentiation", "Factorial", "Square root"],
        "answer": "Quotient and Remainder"
      },
      {
        "question": "What is the decimal expansion of 5/14?",
        "options": ["0.714285˙", "0.357142˙", "0.142857˙", "0.285714˙"],
        "answer": "0.357142˙"
      }
    ]
  }


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
    a1_text.innerHTML = demoQs.questions[qIndex].options[0]
    a2_text.innerHTML = demoQs.questions[qIndex].options[1]
    a3_text.innerHTML = demoQs.questions[qIndex].options[2]
    a4_text.innerHTML = demoQs.questions[qIndex].options[3]
    score_text.innerHTML=`${correctAnswers} / ${qsAnswered}`
    currentq = demoQs.questions[qIndex]
  }
  update();
  let a1_box = document.getElementById("a1-box")
  let a2_box = document.getElementById("a2-box")
  let a3_box = document.getElementById("a3-box")
  let a4_box = document.getElementById("a4-box")

  a1_box.addEventListener("click", function() {
    answerClicked(currentq.answer == currentq.options[0]);
  });
  a2_box.addEventListener("click", function() {
answerClicked(currentq.answer == currentq.options[1]);  });
  a3_box.addEventListener("click", function() {
    answerClicked(currentq.answer == currentq.options[2]);
  });
  a4_box.addEventListener("click", function() {
    answerClicked(currentq.answer == currentq.options[3]);
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