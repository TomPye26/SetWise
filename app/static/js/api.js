
async function createWorkoutSession(label) {
    const response = await fetch("/api/workout-sessions/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            user_id: 1,
            label: label || null,
        }),
    });

    return await response.json();
}


async function getExercises() {
    const response = await fetch("/api/exercises");

    return await response.json();
}


async function addExerciseToSession(sessionId, exerciseId, position) {
    const response = await fetch(
        `/api/workout-session-exercises/session/${sessionId}`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                exercise_id: exerciseId,
                position: position,
            }),
        }
    );

    if (!response.ok) {
        throw new Error("Failed to add exercise");
    }

    return await response.json();
}


async function getSessionExercises(sessionId) {
    const response = await fetch(
        `/api/workout-session-exercises/session/${sessionId}`
    );

    return await response.json();
}

async function addExerciseSet(sessionId, exerciseId, setData) {
    const response = await fetch(
        `/api/exercise-sets/session/${sessionId}`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                exercise_id: exerciseId,
                ...setData,
            }),
        }
    );

    return await response.json();
}

async function getSessionSets(sessionId) {
    const response = await fetch(
        `/api/exercise-sets/session/${sessionId}`
    );

    return await response.json();
}


async function getActiveWorkoutSession(userId) {
    const response = await fetch(
        `/api/workout-sessions/user/${userId}/active`
    );

    if (response.status === 404) {
        return null;
    }

    if (!response.ok) {
        throw new Error("Failed to get active workout");
    }

    active_workout_sessions = await response.json();

    return active_workout_sessions;
}

async function getSessionSets(sessionId) {
    const response = await fetch(
        `/api/exercise-sets/session/${sessionId}`
    );

    if (!response.ok) {
        throw new Error("Failed to get session sets");
    }

    return await response.json();
}


async function finishWorkoutSession(sessionId) {
    const response = await fetch(
        `/api/workout-sessions/${sessionId}`,
        {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                completed_at: new Date().toISOString(),
            }),
        }
    );

    if (!response.ok) {
        throw new Error("Failed to finish workout");
    }

    return await response.json();
}

async function getWorkoutSessions(userId) {
    const response = await fetch(
        `/api/workout-sessions/user/${userId}`
    );

    if (!response.ok) {
        throw new Error("Failed to get workout sessions");
    }

    return await response.json();
}

async function deleteExerciseSet(setId) {
    const response = await fetch(
        `/api/exercise-sets/${setId}`,
        {
            method: "DELETE",
        }
    );

    if (!response.ok) {
        throw new Error("Failed to delete set");
    }

    return await response.json();
}

async function updateExerciseSet(setId, setData) {
    const response = await fetch(
        `/api/exercise-sets/${setId}`,
        {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(setData),
        }
    );

    if (!response.ok) {
        throw new Error("Failed to update set");
    }

    return await response.json();
}

async function removeExerciseFromSession(sessionId, exerciseId) {
    const response = await fetch(
        `/api/workout-session-exercises/session/${sessionId}/${exerciseId}`,
        {
            method: "DELETE",
        }
    );

    if (!response.ok) {
        throw new Error("Failed to remove exercise");
    }
}
