var staticCacheName = 'djangopwa-v' + new Date().getTime();
var offlinePage = '/offline/'; // Ruta de la página offline


var filesToCache = [
  '/static/css/bootstrap.min.css',
  '/static/css/login.css',
  'static/assets/img/icons/avocado.png',
  'templates/offline.html',
  'static/assets/img/icons/logo.svg',
  'static/assets/img/nocon.png'
];

const urlsToCache = [
    '/',
    '/offline/',
    '/mt/',
    '/vs/'
  ];
 
//cache install 
self.addEventListener('install', function(event) {
    event.waitUntil(
      caches.open(staticCacheName).then(function(cache) {
        return cache.addAll(urlsToCache);
      })
    );
  });


  self.addEventListener('fetch', event => {
    event.respondWith(
      caches.match(event.request)
        .then(response => response || fetch(event.request))
        .catch(() => caches.match('/offline/'))  // Redirige a la página de "No conexión" si no se puede recuperar el recurso
    );
  });














  /*
//Dejar en cache lo que regresa el servidor 
self.addEventListener("fetch", function(event){
    event.respondWith(
      fetch(event.request)
      .then(function(result){
          return caches.open(staticCacheName)
          .then(function(c){
            c.put(event.request.url, result.clone())
            return result;
          })
      })
      .catch(function(e){
          return caches.match(event.request);
      })
    )
  });

*/
/*
  self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request).then(function(response) {
  
          return fetch(event.request)
           .catch(function(rsp) {
             return response;
          });
  
  
         })
      );
   });
   */

// Guardado forzoso en cache
/*
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
  */
  
//funcion fetch normal 
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

 //Dejar en cache lo que regresa el servidor 
 /*
self.addEventListener("fetch", function(event){
    event.respondWith(
      fetch(event.request)
      .then(function(result){
          return caches.open(staticCacheName)
          .then(function(c){
            c.put(event.request.url, result.clone())
            return result;
          })
      })
      .catch(function(e){
          return caches.match(event.request);
      })
    )
  });
  */

  /*
// ActivaciÃ³n del Service Worker
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.filter(name => name !== CACHE_NAME)
          .map(name => caches.delete(name))
      );
    })
  );
});

// Escucha el evento 'fetch'
self.addEventListener('fetch', event => {
  event.respondWith(
    // Intenta realizar la solicitud de red
    fetch(event.request).catch(() => {
      // Si falla la solicitud, busca la pÃ¡gina en cachÃ© y redirige al usuario a ella
      return caches.match('/offline').then(response => {
        return response || Response.redirect('/offline', 302);
      });
    })
  );
}); */


// Evento de activación del Service Worker
/*
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
*/
