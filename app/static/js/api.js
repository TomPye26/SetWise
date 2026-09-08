
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

    if (!response.ok) {
        throw new Error("Failed to get active workout");
    }

    return await response.json();
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
