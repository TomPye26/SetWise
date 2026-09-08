
// dom elements

const home = document.getElementById("home");
const startWorkout = document.getElementById("start-workout");
const activeWorkout = document.getElementById("active-workout");
const exercisePicker = document.getElementById("exercise-picker");

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


// app state

let activeSession = null;
let activeSessionExercises = [];


// initialise app

initialiseStartWorkout();
initialiseActiveWorkout();
restoreActiveWorkout();
