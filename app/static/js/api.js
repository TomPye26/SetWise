
// users

async function getUsers() {
    const response = await fetch("/api/users/");

    if (!response.ok) {
        throw new Error("Failed to get users");
    }

    return await response.json();
}


async function createUser(username) {
    const response = await fetch("/api/users/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            username: username,
        }),
    });

    if (!response.ok) {
        throw new Error("Failed to create user");
    }

    return await response.json();
}


// workout sessions

async function createWorkoutSession(label) {
    const response = await fetch("/api/workout-sessions/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            user_id: currentUser.id,
            label: label || null,
        }),
    });

    if (!response.ok) {
        throw new Error("Failed to create workout");
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


async function deleteWorkoutSession(sessionId) {
    const response = await fetch(
        `/api/workout-sessions/${sessionId}`,
        {
            method: "DELETE",
        }
    );

    if (!response.ok) {
        throw new Error("Failed to delete workout");
    }
}


// exercises

async function getExercises() {
    const response = await fetch("/api/exercises");

    if (!response.ok) {
        throw new Error("Failed to get exercises");
    }

    return await response.json();
}


// workout session exercises

async function addExerciseToSession(
    sessionId,
    exerciseId,
    position,
) {
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

    if (!response.ok) {
        throw new Error("Failed to get session exercises");
    }

    return await response.json();
}


async function removeExerciseFromSession(
    sessionId,
    exerciseId,
) {
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


// exercise sets

async function addExerciseSet(
    sessionId,
    exerciseId,
    setData,
) {
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

    if (!response.ok) {
        throw new Error("Failed to add set");
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
}
