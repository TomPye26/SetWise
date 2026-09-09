
function initialiseWorkoutDetails() {
    workoutDetailsBackButton.addEventListener(
        "click",
        async () => {
            await loadWorkoutHistory();

            showScreen(home);
        }
    );
}


async function openWorkoutDetails(session) {
    viewingWorkout = session;

    workoutDetailsTitle.textContent =
        session.label || "Workout";

    workoutDetailsTime.textContent =
        formatWorkoutTime(session);

    workoutDetailsExercises.replaceChildren();

    const sessionExercises =
        await getSessionExercises(session.id);

    const sets =
        await getSessionSets(session.id);

    const exercises =
        await getExercises();

    for (const sessionExercise of sessionExercises) {
        const exercise = exercises.find(
            (exercise) =>
                exercise.id === sessionExercise.exercise_id
        );

        if (!exercise) {
            continue;
        }

        const exerciseSets = sets.filter(
            (set) =>
                set.exercise_id === exercise.id
        );

        const card = createWorkoutDetailsCard(
            exercise,
            exerciseSets,
        );

        workoutDetailsExercises.appendChild(card);
    }

    showScreen(workoutDetails);
}


function createWorkoutDetailsCard(
    exercise,
    sets,
) {
    const card = document.createElement("div");
    card.classList.add("exercise-card");

    const title = document.createElement("h3");
    title.textContent = exercise.name;

    const table = document.createElement("table");

    const header = document.createElement("tr");

    const setHeader = document.createElement("th");
    setHeader.textContent = "Set";

    const inputHeader = document.createElement("th");
    inputHeader.textContent =
        getInputHeader(exercise);

    header.appendChild(setHeader);
    header.appendChild(inputHeader);

    table.appendChild(header);

    for (const set of sets) {
        const row = createWorkoutDetailsSetRow(
            exercise,
            set,
        );

        table.appendChild(row);
    }

    card.appendChild(title);
    card.appendChild(table);

    return card;
}


function createWorkoutDetailsSetRow(
    exercise,
    set,
) {
    const row = document.createElement("tr");

    const setCell = document.createElement("td");
    setCell.textContent = set.set_number;

    const valueCell = document.createElement("td");

    valueCell.textContent =
        formatSetValue(exercise, set);

    row.appendChild(setCell);
    row.appendChild(valueCell);

    return row;
}


function formatSetValue(exercise, set) {
    if (exercise.exercise_type === "weighted") {
        return `${set.weight} kg × ${set.reps}`;
    }

    if (exercise.exercise_type === "bodyweight") {
        return `${set.reps} reps`;
    }

    if (exercise.exercise_type === "assisted") {
        return `${set.assistance_weight} kg assistance × ${set.reps}`;
    }

    if (exercise.exercise_type === "duration") {
        return formatDuration(set.duration_seconds);
    }

    return "";
}


function formatDuration(seconds) {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;

    if (minutes === 0) {
        return `${remainingSeconds} sec`;
    }

    if (remainingSeconds === 0) {
        return `${minutes} min`;
    }

    return `${minutes} min ${remainingSeconds} sec`;
}
