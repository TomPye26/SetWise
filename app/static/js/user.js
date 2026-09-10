let currentUser = null;


function initialiseUser() {
    const savedUser = localStorage.getItem("setwise_user");

    if (!savedUser) {
        return;
    }

    currentUser = JSON.parse(savedUser);
}


function setCurrentUser(user) {
    currentUser = user;

    localStorage.setItem(
        "setwise_user",
        JSON.stringify(user),
    );
}
