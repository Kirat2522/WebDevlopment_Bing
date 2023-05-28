let score = 0;
let highScore = localStorage.getItem("highScore") || 0;
let timeLeft = 15;
let timerInterval;

document.getElementById("myButton").onclick = function () {
    // Start the timer on the first click
    if (!timerInterval) {
        timerInterval = setInterval(function () {
            timeLeft--;
            document.getElementById("timer").innerHTML = "Time left: " + timeLeft;

            // Stop the game when the time runs out
            if (timeLeft === 0) {
                clearInterval(timerInterval);
                document.getElementById("myButton").disabled = true;

                // Update the high score
                if (score > highScore) {
                    highScore = score;
                    localStorage.setItem("highScore", highScore);

                    // Update the high score text and change its color to green
                    let highScoreElement = document.getElementById("highScore");
                    highScoreElement.innerHTML = "High Score: " + highScore;
                    highScoreElement.style.color = "green";

                    // Change the color back to white after 5 seconds
                    setTimeout(function () {
                        highScoreElement.style.color = "white";
                    }, 5000);
                }
            }
        }, 1000);
    }

    // Increase the score
    score++;
    document.getElementById("score").innerHTML = "Score: " + score;
};

document.getElementById("restartButton").onclick = function () {
    // Reset the score
    score = 0;
    document.getElementById("score").innerHTML = "Score: " + score;

    // Reset the timer
    timeLeft = 15;
    document.getElementById("timer").innerHTML = "Time left: " + timeLeft;

    // Enable the "Click me!" button
    document.getElementById("myButton").disabled = false;

    // Clear any existing timer interval
    clearInterval(timerInterval);
    timerInterval = null;
};

// Update the high score text on page load
document.getElementById("highScore").innerHTML = "High Score: " + highScore;
