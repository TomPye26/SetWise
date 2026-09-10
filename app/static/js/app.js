
// dom elements

const home = document.getElementById("home");
const startWorkout = document.getElementById("start-workout");
const activeWorkout = document.getElementById("active-workout");
const exercisePicker = document.getElementById("exercise-picker");


// users

const userScreen =
    document.getElementById("user-screen");

const userList =
    document.getElementById("user-list");

const usernameInput =
    document.getElementById("username-input");

const createUserButton =
    document.getElementById("create-user-button");

const startWorkoutButton =
    document.getElementById("start-workout-button");


    const workouts =
    document.getElementById("workouts");

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

const activeWorkoutLabel =
    document.getElementById("active-workout-label");

const activeBackButton =
    document.getElementById("active-back-button");

const addExerciseButton =
    document.getElementById("add-exercise-button");

const exercisePickerBackButton =
    document.getElementById("exercise-picker-back-button");

const exerciseList =
    document.getElementById("exercise-list");

const activeExercises =
    document.getElementById("active-exercises");

const finishWorkoutButton =
    document.getElementById("finish-workout-button");

const workoutDetails =
    document.getElementById("workout-details");

const workoutDetailsBackButton =
    document.getElementById("workout-details-back-button");

const workoutDetailsTitle =
    document.getElementById("workout-details-title");

const workoutDetailsTime =
    document.getElementById("workout-details-time");

const workoutDetailsExercises =
    document.getElementById("workout-details-exercises");


// app state

let activeSession = null;
let activeSessionExercises = [];
let viewingWorkout = null;


// initialise app
initialiseUser();
initialiseStartWorkout();
initialiseActiveWorkout();
initialiseWorkoutDetails();

if (currentUser) {
    initialiseHome();
} else {
    initialiseUserScreen();
}
