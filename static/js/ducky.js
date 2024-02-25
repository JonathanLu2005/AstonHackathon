const canvas = document.getElementById('myCanvasA');
const ctx = canvas.getContext('2d');

const spriteWidth = 32;
const spriteHeight = 32;
const spriteFrames = 2;
const fps = 10;

const spriteImage = new Image();
spriteImage.src='/static/assets/ducky.png';

let frameIndex = 0;
let frameCounter = 0;

spriteImage.onload = function(){
    canvas.width = window.innerWidth;
    animate();
}

function animate(){
    ctx.clearRect(0,0,canvas.width, canvas.height);

    ctx.drawImage(
        spriteImage,
        frameIndex * spriteWidth,
        0,
        spriteWidth,
        spriteHeight,
        0,
        0,
        spriteWidth*3, // Destination width
        spriteHeight*3 // Destination height
    );

    if (frameCounter % Math.round(60 / fps) === 0) {
        frameIndex = (frameIndex + 1) % spriteFrames;
    }

    frameCounter++;

    requestAnimationFrame(animate);
}

