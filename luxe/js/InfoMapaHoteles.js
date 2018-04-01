  var map;
  var myLatlng = new google.maps.LatLng(-2.168773, -79.917083);
  var beaches;
  var infowindow1;
  var infowindow2;
  var infowindow3;
  var infowindow4;
  var infowindow5;

  function initMap() {

      /* Creamos ventanas de información de las distribuidoras */

      infowindow1 = new google.maps.InfoWindow({
          content: "<h2>Guayaquil</h2> <a href='#' onclick=' cambiargraph(1);llamarGraph1(); return false;'>Ventas Por Distribuidoras 2010-2017</a><br />" +
              "<a href='#' onclick='cambiargraph(2);llamarGraph2(1,\"Guayaquil\"); return false;'>Cantidad de Carros Vendidos 2010-2017</a> <br />" +
              "<a href='#' onclick='cambiargraph(3);llamarGraph3(1,\"Guayaquil\"); return false;'>Cantidad de Carros por Vendedor 2010-2017</a> <br />"
      });
      infowindow2 = new google.maps.InfoWindow({
          content: "<h2>Manta</h2> <a href='#' onclick='cambiargraph(1);llamarGraph1(); return false;'>Ventas Por Distribuidoras 2010-2017</a><br />" +
              "<a href='#' onclick='cambiargraph(2);llamarGraph2(2, \"Manta\"); return false;'>Cantidad de Carros Vendidos 2010-2017</a> <br />" +
              "<a href='#' onclick='cambiargraph(3);llamarGraph3(2,\"Manta\"); return false;'>Cantidad de Carros por Vendedor 2010-2017</a> <br />"
      });
      infowindow3 = new google.maps.InfoWindow({
          content: "<h2>Atacames</h2> <a href='#' onclick='cambiargraph(1);llamarGraph1(); return false;'>Ventas Por Distribuidoras 2010-2017</a> <br />" +
              "<a href='#' onclick='cambiargraph(2);llamarGraph2(3, \"Atacames\"); return false;'>Cantidad de Carros Vendidos 2010-2017</a> <br />" +
              "<a href='#' onclick='cambiargraph(3);llamarGraph3(3,\" Atacames\"); return false;'>Cantidad de Carros por Vendedor 2010-2017</a> <br />"
      });
      infowindow4 = new google.maps.InfoWindow({
          content: "<h2>Salinas</h2> <a href='#' onclick='cambiargraph(1);llamarGraph1(); return false;'>Ventas Por Distribuidoras 2010-2017</a><br />" +
              "<a href='#' onclick='cambiargraph(2);llamarGraph2(4, \"Salinas\"); return false;'>Cantidad de Carros Vendidos 2010-2017</a> <br />" +
              "<a href='#' onclick='cambiargraph(3);llamarGraph3(4,\"Salinas\"); return false;'>Cantidad de Carros por Vendedor 2010-2017</a> <br />"
      });
      infowindow5 = new google.maps.InfoWindow({
          content: "<h2>Salinas</h2> <a href='#' onclick='cambiargraph(1);llamarGraph1(); return false;'>Ventas Por Distribuidoras 2010-2017</a><br />" +
              "<a href='#' onclick='cambiargraph(2);llamarGraph2(5, \"Salinas\"); return false;'>Cantidad de Carros Vendidos 2010-2017</a> <br />" +
              "<a href='#' onclick='cambiargraph(3);llamarGraph3(5,\"Salinas\"); return false;'>Cantidad de Carros por Vendedor 2010-2017</a> <br />"
      });

      /* Beaches son los puntos en el mapa de la distribuidoras */

      beaches = [
          ['Gye', -2.188050, -79.891388, 0, ''],
          ['Manta', -0.940794, -80.735451, 1, ''],
          ['Atacames', 0.890369, -79.817292, 2, ''],
          ['Salinas', -2.2001875, -80.976634, 3, '']
      ];

      map = new google.maps.Map(document.getElementById('map'), {
          center: {
              lat: -2.168773,
              lng: -79.917083
          },


          //center: { lat: -33.9, lng: 151.2 },
          zoom: 6
      });

      /* Llamamos a función para crear las marcas de las ditribuidoras en el mapa */
      setMarkers(map);

      google.maps.event.addListener(map, 'click', closeInfoWindow);
  }

  function closeInfoWindow() {

      infowindow1.close();
      infowindow2.close();
      infowindow3.close();
      infowindow4.close();
      infowindow5.close();

  }
  // Data for the markers consisting of a name, a LatLng and a zIndex for the
  // order in which these markers should display on top of each other.

  function setMarkers(map) {
      // Adds markers to the map.

      // Marker sizes are expressed as a Size of X,Y where the origin of the image
      // (0,0) is located in the top left of the image.

      // Origins, anchor positions and coordinates of the marker increase in the X
      // direction to the right and in the Y direction down.
      var image = {
          //  url: 'https://mt.googleapis.com/vt/icon/name=icons/onion/bank-dollar.png',
          //url: 'images/loc.png',
          // This marker is 20 pixels wide by 32 pixels high.
          size: new google.maps.Size(32, 32),
          // The origin for this image is (0, 0).
          origin: new google.maps.Point(0, 0),
          // The anchor for this image is the base of the flagpole at (0, 32).
          anchor: new google.maps.Point(32, 32)
      };
      // Shapes define the clickable region of the icon. The type defines an HTML
      // <area> element 'poly' which traces out a polygon as a series of X,Y points.
      // The final coordinate closes the poly by connecting to the first coordinate.

      for (var i = 0; i < beaches.length; i++) {
          var beach = beaches[i];

          if (i == 0) {
              var marker0 = new google.maps.Marker({
                  position: {
                      lat: beach[1],
                      lng: beach[2]
                  },
                  map: map,
                  //icon: image,
                  icon: 'images/loc.png',
                  title: beach[0],
                  zIndex: beach[3]
              });
              marker0.addListener('click', function() {
                  infowindow1.open(map, marker0);
                  infowindow2.close();
                  infowindow3.close();
                  infowindow4.close();
                  infowindow5.close();

              });
          }
          if (i == 1) {
              var marker1 = new google.maps.Marker({
                  position: {
                      lat: beach[1],
                      lng: beach[2]
                  },
                  map: map,
                  //  icon: image,
                  icon: 'images/loc.png',
                  title: beach[0],
                  zIndex: beach[3]
              });
              marker1.addListener('click', function() {

                  infowindow1.close();
                  infowindow3.close();
                  infowindow4.close();
                  infowindow5.close();
                  infowindow2.open(map, marker1);
              });
          }
          if (i == 2) {
              var marker2 = new google.maps.Marker({
                  position: {
                      lat: beach[1],
                      lng: beach[2]
                  },
                  map: map,
                  //  icon: image,
                  icon: 'images/loc.png',
                  title: beach[0],
                  zIndex: beach[3]
              });
              marker2.addListener('click', function() {
                  infowindow2.close();
                  infowindow1.close();
                  infowindow4.close();
                  infowindow5.close();
                  infowindow3.open(map, marker2);
              });
          }
          if (i == 3) {
              var marker3 = new google.maps.Marker({
                  position: {
                      lat: beach[1],
                      lng: beach[2]
                  },
                  map: map,
                  //  icon: image,
                  icon: 'images/loc.png',
                  title: beach[0],
                  zIndex: beach[3]
              });
              marker3.addListener('click', function() {
                  infowindow2.close();
                  infowindow3.close();
                  infowindow5.close();
                  infowindow1.close();
                  infowindow4.open(map, marker3);
              });
          }
          if (i == 4) {
              var marker4 = new google.maps.Marker({
                  position: {
                      lat: beach[1],
                      lng: beach[2]
                  },
                  map: map,
                  // icon: image,
                  icon: 'images/loc.png',
                  title: beach[0],
                  zIndex: beach[3]
              });
              marker4.addListener('click', function() {
                  infowindow2.close();
                  infowindow3.close();
                  infowindow4.close();
                  infowindow1.close();
                  infowindow5.open(map, marker4);

              });
          }
      }
  }


  function cambiargraph(id) {


      $("#graph1").empty();
      $("#graph2").empty();
      $("#graph3").empty();

      $("#graph1").hide();
      $("#graph2").hide();
      $("#graph3").hide();

      if (id == 1) {

          $("#graph1").show();
      }
      if (id == 2) {
          $("#graph2").show();
      }
      if (id == 3) {
          $("#graph3").show();
      }


  }