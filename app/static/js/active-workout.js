
async function loadExercises() {
    const exercises = await getExercises();

    exerciseList.replaceChildren();

    for (const exercise of exercises) {
        const exerciseButton = document.createElement("button");

        exerciseButton.textContent = exercise.name;

        exerciseButton.addEventListener("click", async () => {
            const sessionExercises =
                await getSessionExercises(activeSession.id);

            const position = sessionExercises.length + 1;

            await addExerciseToSession(
                activeSession.id,
                exercise.id,
                position
            );

            showScreen(activeWorkout);

            await loadSessionExercises();
        });

        exerciseList.appendChild(exerciseButton);
    }
}


async function loadSessionExercises() {
    const sessionExercises =
        await getSessionExercises(activeSession.id);

    const exercises = await getExercises();

    activeExercises.replaceChildren();

    for (const sessionExercise of sessionExercises) {
        const exercise = exercises.find(
            (exercise) => exercise.id === sessionExercise.exercise_id
        );

        if (!exercise) {
            continue;
        }

        const exerciseCard = createExerciseCard(exercise);

        activeExercises.appendChild(exerciseCard);
    }
}


function createExerciseCard(exercise) {
    const card = document.createElement("div");
    card.classList.add("exercise-card");

    const title = document.createElement("h3");
    title.textContent = exercise.name;

    const table = document.createElement("table");

    const header = document.createElement("tr");

    const setHeader = document.createElement("th");
    setHeader.textContent = "Set";

    const weightHeader = document.createElement("th");
    weightHeader.textContent = "Weight";

    const repsHeader = document.createElement("th");
    repsHeader.textContent = "Reps";

    header.appendChild(setHeader);
    header.appendChild(weightHeader);
    header.appendChild(repsHeader);

    table.appendChild(header);

    const addSetButton = document.createElement("button");
    addSetButton.textContent = "+ Add Set";

    addSetButton.addEventListener("click", () => {
        addSetRow(table, exercise);
    });

    card.appendChild(title);
    card.appendChild(table);
    card.appendChild(addSetButton);

    return card;
}

function addSetRow(table, exercise) {
    const setNumber = table.rows.length;

    const row = document.createElement("tr");

    const setCell = document.createElement("td");
    setCell.textContent = setNumber;

    const weightCell = document.createElement("td");
    const weightInput = document.createElement("input");

    weightInput.type = "number";
    weightInput.placeholder = "kg";
    weightInput.min = "0";
    weightInput.step = "0.5";

    weightCell.appendChild(weightInput);

    const repsCell = document.createElement("td");
    const repsInput = document.createElement("input");

    repsInput.type = "number";
    repsInput.placeholder = "reps";
    repsInput.min = "1";

    repsCell.appendChild(repsInput);

    row.appendChild(setCell);
    row.appendChild(weightCell);
    row.appendChild(repsCell);

    table.appendChild(row);
}


function initialiseActiveWorkout() {
    activeBackButton.addEventListener("click", () => {
        showScreen(home);
    });


    addExerciseButton.addEventListener("click", async () => {
        await loadExercises();

        showScreen(exercisePicker);
    });


    exercisePickerBackButton.addEventListener("click", () => {
        showScreen(activeWorkout);
    });
}
