
let selectedLabel = "";


function initialiseStartWorkout() {
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
        const session = await createWorkoutSession(selectedLabel);

        activeSession = session;

        activeSessionExercises = [];
        activeExercises.replaceChildren();

        activeWorkoutLabel.textContent =
            session.label || "Workout";


        showScreen(activeWorkout);

        console.log("Started workout:", session);
    });
}
