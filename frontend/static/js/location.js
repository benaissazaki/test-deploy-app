var map =L.map('map').setView([36.76, 2.95], 13)
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
var marker = L.marker([36.76, 2.95]).addTo(map);
// get the location by clicking on it.
map.on('click', (event) => {
    console.log(event.latlng)
})
