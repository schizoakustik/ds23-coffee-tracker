var colors = {yellow: "#FFE8A1", red: "#FFBDA1", blue: "#A7D7FF"}
var body = document.getElementsByTagName("body")[0];
var boxes = document.getElementById("boxes");

var data = {currentLocation: 'red'}

const response = await fetch('http://localhost:5000/location', {method: "GET"})
data = await response.json()


body.style.background = colors[data.currentLocation];

for (const [key, value] of Object.entries(colors)) {
    var div = document.createElement('div')
    div.id = key
    div.style.width = '5em'
    div.style.height = '5em'
    div.style.border = '1px solid black'
    div.style.borderRadius = '5px'
    div.style.background = value
    boxes.style.opacity = .6
    div.style.cursor = 'pointer'
    div.addEventListener('click', (e) => {
        set_color(e.target.id)
    })
    boxes.append(div)
};

function set_color(loc) {
    var newLocation = loc
    body.style.background = colors[newLocation]
    fetch(
        'http://localhost:5000/location', 
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({currentLocation: newLocation})
        }
    ).then()
}