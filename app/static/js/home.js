
function initialiseHome() {
    loadWorkoutHistory();
}


async function loadWorkoutHistory() {
    const sessions = await getWorkoutSessions(
        currentUser.id
    );

    renderWorkoutHistory(sessions);
}


function renderWorkoutHistory(sessions) {
    workouts.replaceChildren();

    const activeSessions = sessions.filter(
        (session) => session.completed_at === null
    );

    const completedSessions = sessions.filter(
        (session) => session.completed_at !== null
    );

    if (activeSessions.length > 0) {
        const activeHeading = document.createElement("h3");
        activeHeading.textContent = "Continue Workout";

        workouts.appendChild(activeHeading);

        for (const session of activeSessions) {
            workouts.appendChild(
                createWorkoutCard(session, true)
            );
        }
    }

    if (completedSessions.length > 0) {
        const historyHeading = document.createElement("h3");
        historyHeading.textContent = "Workout History";

        workouts.appendChild(historyHeading);

        for (const session of completedSessions) {
            workouts.appendChild(
                createWorkoutCard(session, false)
            );
        }
    }
}


function createWorkoutCard(session, isActive) {
    const card = document.createElement("div");
    card.classList.add("workout-card");

    const title = document.createElement("h3");
    title.textContent = session.label || "Workout";

    const date = document.createElement("p");
    date.textContent = formatWorkoutTime(session);

    card.appendChild(title);
    card.appendChild(date);

    if (!isActive) {
        const duration = document.createElement("p");
        duration.textContent = formatWorkoutDuration(session);

        card.appendChild(duration);

        const summary = document.createElement("p");
        summary.textContent =
            `${session.exercise_count} exercises · ` +
            `${session.set_count} sets`;

        card.appendChild(summary);

        const viewButton = document.createElement("button");
        viewButton.textContent = "View Workout";

        viewButton.addEventListener("click", async () => {
            await openWorkoutDetails(session);
        });

        card.appendChild(viewButton);
    }

    if (isActive) {
        const continueButton = document.createElement("button");
        continueButton.textContent = "Continue";

        continueButton.addEventListener("click", async () => {
            await openWorkoutSession(session);
        });

        card.appendChild(continueButton);
    }

    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";

    deleteButton.addEventListener("click", async () => {
        await deleteWorkout(session.id);
    });

    card.appendChild(deleteButton);

    return card;
}

function formatWorkoutTime(session) {
    const start = new Date(session.started_at);

    const date = start.toLocaleDateString("en-GB", {
        day: "numeric",
        month: "short",
        year: "numeric",
    });

    const startTime = start.toLocaleTimeString("en-GB", {
        hour: "2-digit",
        minute: "2-digit",
    });

    if (!session.completed_at) {
        return `${date} · Started ${startTime}`;
    }

    const end = new Date(session.completed_at);

    const endTime = end.toLocaleTimeString("en-GB", {
        hour: "2-digit",
        minute: "2-digit",
    });

    return `${date} · ${startTime}–${endTime}`;
}


function formatWorkoutDuration(session) {
    const start = new Date(session.started_at);
    const end = new Date(session.completed_at);

    const durationMinutes = Math.round(
        (end - start) / 60000
    );

    if (durationMinutes < 60) {
        return `${durationMinutes} min`;
    }

    const hours = Math.floor(durationMinutes / 60);
    const minutes = durationMinutes % 60;

    if (minutes === 0) {
        return `${hours} hr`;
    }

    return `${hours} hr ${minutes} min`;
}


async function deleteWorkout(sessionId) {
    const confirmed = confirm(
        "Delete this workout? " +
        "All exercises and sets recorded in this workout will be deleted."
    );

    if (!confirmed) {
        return;
    }

    await deleteWorkoutSession(sessionId);

    await loadWorkoutHistory();
}

function formatWorkoutDate(dateString) {
    const date = new Date(dateString);

    return date.toLocaleString("en-GB", {
        day: "numeric",
        month: "short",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit",
    });
}