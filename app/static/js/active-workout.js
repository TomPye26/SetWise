
// initialise active workout

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


// exercise management

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

            activeSessionExercises.push(exercise);

            const exerciseCard = createExerciseCard(exercise);

            activeExercises.appendChild(exerciseCard);

            showScreen(activeWorkout);
        });

        exerciseList.appendChild(exerciseButton);
    }
}


// exercise card UI

function createExerciseCard(exercise) {
    const card = document.createElement("div");
    card.classList.add("exercise-card");

    const title = document.createElement("h3");
    title.textContent = exercise.name;

    const table = document.createElement("table");

    const header = document.createElement("tr");

    const setHeader = document.createElement("th");
    setHeader.textContent = "Set";

    const inputHeader = document.createElement("th");
    inputHeader.textContent = getInputHeader(exercise);

    const actionHeader = document.createElement("th");
    actionHeader.textContent = "";

    header.appendChild(setHeader);
    header.appendChild(inputHeader);
    header.appendChild(actionHeader);

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


function getInputHeader(exercise) {
    if (exercise.exercise_type === "weighted") {
        return "Weight / Reps";
    }

    if (exercise.exercise_type === "bodyweight") {
        return "Reps";
    }

    if (exercise.exercise_type === "assisted") {
        return "Assistance / Reps";
    }

    if (exercise.exercise_type === "duration") {
        return "Duration";
    }

    return "Value";
}


// set management

function addSetRow(table, exercise) {
    const setNumber = table.rows.length;

    const row = document.createElement("tr");

    const setCell = document.createElement("td");
    setCell.textContent = setNumber;

    const inputCell = document.createElement("td");

    const actionCell = document.createElement("td");

    const saveButton = document.createElement("button");
    saveButton.textContent = "Add";

    const inputs = createSetInputs(exercise);

    for (const input of inputs) {
        inputCell.appendChild(input);
    }

    saveButton.addEventListener("click", async () => {
        await saveSet(
            exercise,
            setNumber,
            inputs,
            row,
        );
    });

    actionCell.appendChild(saveButton);

    row.appendChild(setCell);
    row.appendChild(inputCell);
    row.appendChild(actionCell);

    table.appendChild(row);
}


async function saveSet(
    exercise,
    setNumber,
    inputs,
    row,
) {
    const setData = buildSetData(
        exercise,
        setNumber,
        inputs,
    );

    if (!setData) {
        return;
    }

    const set = await addExerciseSet(
        activeSession.id,
        exercise.id,
        setData,
    );

    console.log("Saved set:", set);

    row.classList.add("completed");
}


function buildSetData(exercise, setNumber, inputs) {
    if (exercise.exercise_type === "weighted") {
        const weight = inputs[0].value;
        const reps = inputs[1].value;

        if (!weight || !reps) {
            return null;
        }

        return {
            set_number: setNumber,
            weight: Number(weight),
            weight_unit: "kg",
            reps: Number(reps),
        };
    }

    if (exercise.exercise_type === "bodyweight") {
        const reps = inputs[0].value;

        if (!reps) {
            return null;
        }

        return {
            set_number: setNumber,
            reps: Number(reps),
        };
    }

    if (exercise.exercise_type === "assisted") {
        const assistanceWeight = inputs[0].value;
        const reps = inputs[1].value;

        if (!assistanceWeight || !reps) {
            return null;
        }

        return {
            set_number: setNumber,
            assistance_weight: Number(assistanceWeight),
            assistance_weight_unit: "kg",
            reps: Number(reps),
        };
    }

    if (exercise.exercise_type === "duration") {
        const duration = inputs[0].value;

        if (!duration) {
            return null;
        }

        return {
            set_number: setNumber,
            duration_seconds: Number(duration),
        };
    }

    return null;
}


// input helpers

function createSetInputs(exercise) {
    const inputs = [];

    if (exercise.exercise_type === "weighted") {
        inputs.push(
            createInput("number", "kg", "0", "0.5"),
            createInput("number", "reps", "1", "1"),
        );
    }

    if (exercise.exercise_type === "bodyweight") {
        inputs.push(
            createInput("number", "reps", "1", "1"),
        );
    }

    if (exercise.exercise_type === "assisted") {
        inputs.push(
            createInput("number", "assistance kg", "0", "0.5"),
            createInput("number", "reps", "1", "1"),
        );
    }

    if (exercise.exercise_type === "duration") {
        inputs.push(
            createInput("number", "seconds", "1", "1"),
        );
    }

    return inputs;
}


function createInput(type, placeholder, min, step) {
    const input = document.createElement("input");

    input.type = type;
    input.placeholder = placeholder;
    input.min = min;
    input.step = step;

    return input;
}
