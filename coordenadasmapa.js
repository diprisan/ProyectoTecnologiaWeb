function initMap() {
    var pyrmont = { lat: -2.168773, lng: -79.917083 };
    var panel = document.getElementById('mapa'); //$('mapa');
    map = new google.maps.Map(panel, {
        center: pyrmont,
        zoom: 6
    });
    createMarker(-2.188050, -79.891388, "Gye");
    createMarker(-2.890007, -79.031678, "Ptv");
    createMarker(-0.1859053, -78.710745, "Uio");
}


function createMarker(latitud, longiutd, codigo) {
    var uluru1 = { lat: latitud, lng: longiutd };
    var marker = new google.maps.Marker({
        position: uluru1,
        map: map
    });

    google.maps.event.addListener(marker, 'click', function() {
        alert(codigo);
    });
}