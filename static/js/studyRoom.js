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
        [hours, minutes, seconds] = durationInput.value.split(':').map(Number);

        // Start the countdown
        startCountdown();
    })
    function startCountdown() {
        // Update the clock every second
        let countdownInterval = setInterval(function () {
            if (hours === 0 && minutes === 0 && seconds === 0) {
                // Stop the countdown when it reaches zero
                clearInterval(countdownInterval);
                console.log("Countdown finished!");
            } else {
                // Update the clock and decrement the time
                clock.innerText = formatTime(hours, minutes, seconds);
                decrementTime();
            }
        }, 1000);
    }

    function formatTime(hours, minutes, seconds) {
        // Format the time as HH:MM:SS
        return `${padZero(hours)}:${padZero(minutes)}:${padZero(seconds)}`;
    }

    function decrementTime() {
        // Decrement the time by one second
        if (seconds > 0) {
            seconds--;
        } else {
            if (minutes > 0) {
                minutes--;
                seconds = 59;
            } else {
                if (hours > 0) {
                    hours--;
                    minutes = 59;
                    seconds = 59;
                }
            }
        }
    }

    function padZero(number) {
        // Add leading zero if the number is less than 10
        return number < 10 ? `0${number}` : number;
    }
}