// document.addEventListener("DOMContentLoaded",main)
// function main(){
    
//     console.log("loaded")
//     let clock = document.getElementById("clock");
//     let playPause = document.getElementById("play-pause")
//     let durationInput = document.getElementById("durationInput")
//     let hours,minutes,seconds;
//     durationInput.value="00:00:00"  
//     console.log(clock,playPause)
//     playPause.addEventListener("click",function(){
//         console.log(durationInput.value)
//         hours = durationInput.value.split(':').map(Number)[0];
//         minutes = durationInput.value.split(':').map(Number)[1];
//         seconds = durationInput.value.split(':').map(Number)[2];

//         // Start the countdown
//         startCountdown();
//     })
//     function startCountdown() {
//         // Update the clock every second
//         let countdownInterval = setInterval(function () {
//             if (hours === 0 && minutes === 0 && seconds === 0) {
//                 // Stop the countdown when it reaches zero
//                 clearInterval(countdownInterval);
//                 console.log("Countdown finished!");
//             } else {
//                 // Update the clock and decrement the time
//                 clock.innerText = formatTime(hours, minutes, seconds);
//                 decrementTime();
//             }
//         }, 1000);
//     }

//     function formatTime(hours, minutes, seconds) {
//         // Format the time as HH:MM:SS
//         return `${padZero(hours)}:${padZero(minutes)}:${padZero(seconds)}`;
//     }

//     function decrementTime() {
//         // Decrement the time by one second
//         if (seconds > 0) {
//             seconds--;
//         } else {
//             if (minutes > 0) {
//                 minutes--;
//                 seconds = 59;
//             } else {
//                 if (hours > 0) {
//                     hours--;
//                     minutes = 59;
//                     seconds = 59;
//                 }
//             }
//         }
//     }

//     function padZero(number) {
//         // Add leading zero if the number is less than 10
//         return number < 10 ? `0${number}` : number;
//     }
// }
document.addEventListener("DOMContentLoaded", main);

function main() {
    console.log("loaded");
    let clock = document.getElementById("clock");
    let playPause = document.getElementById("play-pause");
    let durationInput = document.getElementById("durationInput");
    let hours, minutes, seconds;
    let countdownInterval;
    // Set initial value
    durationInput.value = "00:10:00";
    let paused=false;
    let started = false;
    durationInput.addEventListener("input",function(){
        clearInterval(countdownInterval);
                countdownInterval = null;
                started=false;
                paused=false;
    })
    playPause.addEventListener("click", function () {
        console.log(paused,started)
        // // Get hours, minutes, and seconds from input value
        // if(!started){
        //     started=true;
        //     [hours, minutes, seconds] = durationInput.value.split(':').map(Number);
        // }
        

        // // Toggle between play and pause
        // if (!paused && started) {
        //     // If countdown is running, pause it
        //     clearInterval(countdownInterval);
        //     countdownInterval = null;
        //     paused=true;
        //     [hours, minutes, seconds] = durationInput.value.split(':').map(Number);
        // } else {
        //     // If countdown is not running, start it
        //     startCountdown();  
        // }
        if(!started&&!paused){ //Start
            [hours, minutes, seconds] = durationInput.value.split(':').map(Number);
            started=true;
            paused=false;
            startCountdown();
        }else if (started&&!paused){ //Pause
            paused=true;
            started=true;
            clearInterval(countdownInterval);
            countdownInterval = null;
        }else if(started&&paused){ //Resume
            startCountdown();
            paused=false;
            started=true;
        }
    });

    function startCountdown() {
        // Update the clock every second
        countdownInterval = setInterval(function () {
            if (hours === 0 && minutes === 0 && seconds === 0) {
                // Stop the countdown when it reaches zero
                clearInterval(countdownInterval);
                countdownInterval = null;
                started=false;
                paused=false;
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




