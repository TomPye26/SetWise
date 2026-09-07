const home = document.getElementById("home");
const startWorkout = document.getElementById("start-workout");

const startWorkoutButton =
    document.getElementById("start-workout-button");

const backButton =
    document.getElementById("back-button");

const labelButtons =
    document.querySelectorAll(".label-button");

const customLabelButton =
    document.getElementById("custom-label-button");

const customLabel =
    document.getElementById("custom-label");

const confirmStartButton =
    document.getElementById("confirm-start-button");


let selectedLabel = "";


function showScreen(screen) {
    home.hidden = true;
    startWorkout.hidden = true;

    screen.hidden = false;
}


startWorkoutButton.addEventListener("click", () => {
    showScreen(startWorkout);
});


backButton.addEventListener("click", () => {
    showScreen(home);
});


for (const button of labelButtons) {
    button.addEventListener("click", () => {
        selectedLabel = button.dataset.label;

        for (const labelButton of labelButtons) {
            labelButton.classList.remove("selected");
        }

        button.classList.add("selected");

        customLabel.hidden = true;
    });
}


customLabelButton.addEventListener("click", () => {
    customLabel.hidden = false;
    customLabel.focus();

    for (const labelButton of labelButtons) {
        labelButton.classList.remove("selected");
    }

    selectedLabel = "";
});


customLabel.addEventListener("input", () => {
    selectedLabel = customLabel.value;
});



confirmStartButton.addEventListener("click", async () => {
    const response = await fetch("/api/workout-sessions/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            user_id: 1,
            label: selectedLabel || null,
        }),
    });

    const session = await response.json();

    console.log("Started workout:", session);
});