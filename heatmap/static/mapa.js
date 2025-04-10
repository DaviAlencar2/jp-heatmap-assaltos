let map = L.map('map').setView([-7.146985813276585, -34.84807889999999], 13);
let markersLayer = L.layerGroup().addTo(map);
let heatLayer = null;
let currentMapType = 'heatmap';
let currentYear = null;

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

document.addEventListener('DOMContentLoaded', function() {
    updateMap('2025'); // Deixar 2025 como padrao
});

function updateButtonText(year) {
    const button = document.getElementById('yearDropdown');
    button.textContent = year;
}

function changeMapType(type) {
    currentMapType = type;
    if (currentYear) {
        updateMap(currentYear);
    }
}

function clearLayers() {
    markersLayer.clearLayers();
    if (heatLayer) {
        map.removeLayer(heatLayer);
        heatLayer = null;
    }
}

function updateMap(year) {
    currentYear = year;
    clearLayers();

    fetch(`/dados/${year}`)
        .then(response => response.json())
        .then(data => {
            if (currentMapType === 'points') {
                showPoints(data);
            } else {
                showHeatmap(data);
            }
            updateButtonText(year);
        })
        .catch(error => console.error('Erro ao carregar dados: ', error));
}

function showPoints(data) {
    data.forEach(point => {
        L.marker([point.Latitude, point.Longitude], {
            icon: L.icon({
                title: point.Bairro,
                riseOnHover: true,
                interactive: true,
                iconUrl: 'https://cdn-icons-png.flaticon.com/512/5610/5610989.png',
                iconSize: [15, 15]
            })
        }).bindPopup("Assalto").addTo(markersLayer);
    });
}

function showHeatmap(data) {
    const heatData = data.map(point => [
        parseFloat(point.Latitude),
        parseFloat(point.Longitude),
        1 // intensidade do ponto
    ]);

    heatLayer = L.heatLayer(heatData, {
        radius: 15, // raio do ponto no mapa de calor
        blur: 10,   // quantidade de blur aplicado
        maxZoom: 15 // zoom máximo para o efeito de calor
    }).addTo(map);
}