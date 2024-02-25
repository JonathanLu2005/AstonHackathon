const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');

const spriteWidth = 64; // Width of each frame in the sprite
const spriteHeight = 64; // Height of each frame in the sprite
const spriteFrames = 17; // Total number of frames in the sprite

const spriteImage = new Image();
spriteImage.src = '/static/assets/BackGroundGoose.png'; // Replace with the actual path to your sprite image

let frameIndex = 0;
let frameCounter = 0;
let gooseX=window.innerWidth;
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
}else{
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
