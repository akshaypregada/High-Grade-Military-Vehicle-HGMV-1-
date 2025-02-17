function sendCommand(command) {
    fetch(`http://192.168.X.X/${command}`)
        .then(response => response.text())
        .then(data => console.log(data))
        .catch(error => console.error(error));
}
