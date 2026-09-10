
function initialiseUserScreen() {
    showScreen(userScreen);

    loadUsers();

    createUserButton.addEventListener(
        "click",
        async () => {
            await createNewUser();
        }
    );
}


async function loadUsers() {
    const users = await getUsers();

    userList.replaceChildren();

    for (const user of users) {
        const button = document.createElement("button");

        button.textContent = user.username;

        button.addEventListener("click", () => {
            selectUser(user);
        });

        userList.appendChild(button);
    }
}


function selectUser(user) {
    setCurrentUser(user);

    initialiseHome();
    showScreen(home);
}


async function createNewUser() {
    const username = usernameInput.value.trim();

    if (!username) {
        return;
    }

    const user = await createUser(username);

    setCurrentUser(user);

    initialiseHome();
    showScreen(home);
}
