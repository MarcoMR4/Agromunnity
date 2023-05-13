var staticCacheName = 'djangopwa-v' + new Date().getTime();
var filesToCache = [
    '/offline/',
    'static/assets/bootstrap.min.css',
    'static/assets/img/icons/logo.svg',
    'static/assets/img/icons/avocado.png',
] 


self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll([
        '',
      ]);
    })
  );
});
 

/*
self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);
    if (requestUrl.origin === location.origin) {
      if ((requestUrl.pathname === '/')) {
        event.respondWith(caches.match(''));
        return;
      }
    }
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
}); 
*/

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