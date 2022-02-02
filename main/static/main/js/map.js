ymaps.ready(init);

function init() {
    var myMap = new ymaps.Map('map-canvas', {
            center: [47.216735, 39.703829],
            zoom: 16
        }, {
            searchControlProvider: 'yandex#search'
        })
    myMap.geoObjects
        .add(new ymaps.Placemark([47.216735, 39.703829], {
            balloonContent: '<strong>пер.Халтуринский</strong> 22',
        }, {
            preset: 'islands#dotIcon',
            iconColor: '#e67e22'
        }))
}
