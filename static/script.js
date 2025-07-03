let socket;

function connect() {
    const username = document.getElementById("username").value;
    if (!username) return alert("Inserisci un nome");

    socket = new WebSocket(`ws://${location.host}/ws/${username}`);

    socket.onopen = () => {
        document.getElementById("login").style.display = "none";
        document.getElementById("main").style.display = "block";
    };

    socket.onmessage = (event) => {
        const data = JSON.parse(event.data);

        if (data.type === "user_list") {
            const list = document.getElementById("userList");
            list.innerHTML = "";
            data.users.forEach(user => {
                const li = document.createElement("li");
                li.textContent = user;
                list.appendChild(li);
            });
        }
    };

    socket.onclose = () => {
        alert("Connessione chiusa");
        document.location.reload();
    };
}
