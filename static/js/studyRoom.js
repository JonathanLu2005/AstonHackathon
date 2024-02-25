document.addEventListener("DOMContentLoaded",main)
function main(){
    
    console.log("loaded")
    let clock = document.getElementById("clock");
    let playPause = document.getElementById("play-pause")
    let durationInput = document.getElementById("durationInput")
    let hours,minutes,seconds=11;
    durationInput.value="00:00:00"  
    console.log(clock,playPause)
    playPause.addEventListener("click",function(){
        console.log(durationInput.value)
        [hours, minutes, seconds] = timeStr.split(':').map(Number);

        // Start the countdown
        startCountdown();
    })
}