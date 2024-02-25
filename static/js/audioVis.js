// var audio = document.getElementById('audioPlayer');
// var playButton = document.getElementById('playButton');
// var pauseButton = document.getElementById('pauseButton');

// // Get the canvas element and its 2D rendering context
// //const canvas = document.getElementById('visualizer');
// // const ctx = canvas.getContext('2d');

// // Set up audio context and analyzer
// const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
// const analyser = audioCtx.createAnalyser();

// // Function to draw visualizer
// function draw() {
//     requestAnimationFrame(draw);

//     // Copy frequency data to dataArray
//     analyser.getByteFrequencyData(dataArray);

//     // Clear canvas
//     ctx.fillStyle = 'black';
//     ctx.fillRect(0, 0, canvas.width, canvas.height);

//     // Draw visualizer
//     const barWidth = (canvas.width / bufferLength) * 2.5;
//     let x = 0;
//     for(let i = 0; i < bufferLength; i++) {
//         const barHeight = dataArray[i] / 2;
//         const r = barHeight + (25 * (i/bufferLength));
//         const g = 250 * (i/bufferLength);
//         const b = 50;
//         ctx.fillStyle = 'rgb(' + r + ',' + g + ',' + b + ')';
//         ctx.fillRect(x, canvas.height - barHeight, barWidth, barHeight);
//         x += barWidth + 1;
//     }
// }

// // Connect audio source to analyzer
// const audioSource = audioCtx.createMediaElementSource(audio);
// audioSource.connect(analyser);
// audioSource.connect(audioCtx.destination);

// // Set up analyzer properties
// analyser.fftSize = 2048;
// const bufferLength = analyser.frequencyBinCount;
// const dataArray = new Uint8Array(bufferLength);

// // Call draw function
// draw();

// playButton.addEventListener('click', function() {
//     audio.play();
// });

// pauseButton.addEventListener('click', function() {
//     audio.pause();
// });
