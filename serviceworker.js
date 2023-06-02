var cacheName1 = 'djangopwa-v' + new Date().getTime();
var offlinePage = '/offline/'; // Ruta de la página offline


var filesToCache = [
  '/',
  '/static/css/bootstrap.min.css',
  '/static/css/bootstrap.min.css.map',
  '/static/css/login.css',
  '/offline/'
];
 
//cache install 
self. addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(cacheName1)
        .then(cache => {
            return cache.addAll(filesToCache);
        })
    )
})


// Evento de activación del Service Worker
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== cacheName1))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});


// Guardado forzoso en cache

self.addEventListener("fetch", function(event) {
    event.respondWidth(
        fetch(event.request)
        .then(function(result){
            return caches.open(cacheName)
            .then(function(c){
                c.put(event.request.url, result.clone())
                return result 
            })
        })
        .catch(function(e){
            return caches.match(event.request) 
        })
    )
  });
  
/*
 self.addEventListener("fetch", event => {
    event.respondWidth(
        caches.match(event.request)
        .then(response => {
            return response || fetch(event.request);
        })
        .catch(() => {
            return caches.match("/offline/");
        })
    )
 });
  */