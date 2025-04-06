let map = L.map('map').setView([-7.146985813276585, -34.84807889999999], 13);

// Adiciona a camada de tiles do OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);


function updateButtonText(year) {
    const button = document.getElementById('yearDropdown');
    button.textContent = year;
}

function updateMap(year) {
    // Remove todos os marcadores do mapa
    map.eachLayer(function(layer) {
        if (layer instanceof L.Marker) {
            map.removeLayer(layer);
        }
    });

    fetch(`/dados/${year}`)
        .then(response => response.json())
        .then(data => {
            // Adiciona novos marcadores no mapa com base nos dados retornados. Sendo zonas de calor
            data.forEach(point => {
                L.marker([point.Latitude, point.Longitude], {
                    icon: L.icon({
                        title: point.Bairro,
                        riseOnHover: true,
                        interactive: true,
                        iconUrl: 'https://cdn-icons-png.flaticon.com/512/5610/5610989.png',
                        iconSize: [15, 15]
                    })
                }).bindPopup("Assalto").addTo(map);
            });
            updateButtonText(year);
        })
        .catch(error => console.error('Erro ao carregar dados: ', error));
}