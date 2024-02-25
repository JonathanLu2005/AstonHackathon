var audio = document.getElementById('audioPlayer');
var playButton = document.getElementById('playButton');
var pauseButton = document.getElementById('pauseButton');

playButton.addEventListener('click', function() {
    audio.play();
});

pauseButton.addEventListener('click', function() {
    audio.pause();
});