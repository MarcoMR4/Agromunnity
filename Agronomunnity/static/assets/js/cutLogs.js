document.addEventListener('DOMContentLoaded', function() {
    // Obtener los checkboxes, el botón y el elemento de alerta
    var checkboxes = document.querySelectorAll('input[name="seleccion[]"]');
    var botonGenerar = document.getElementById('genDoc');
    var alertaSinSeleccion = document.getElementById('alerta-sin-seleccion');

    // Función para mostrar u ocultar el botón y la alerta
    function mostrarBotonYAlerta() {
        var filasSeleccionadas = document.querySelectorAll('input[name="seleccion[]"]:checked');
        if (filasSeleccionadas.length === 0) {
            botonGenerar.style.display = 'none';
            alertaSinSeleccion.style.display = '';
        } else {
            botonGenerar.style.display = '';
            alertaSinSeleccion.style.display = 'none';
        }
    }

    // Actualizar el campo con las filas seleccionadas al cargar la página
    var filasSeleccionadas = document.querySelectorAll('input[name="seleccion[]"]:checked');
    var contenidoFilasSeleccionadas = Array.from(filasSeleccionadas).map(function(checkbox) {
        return checkbox.value;
    }).join(',');

    document.getElementById('filas-seleccionadas-contenido').value = contenidoFilasSeleccionadas;

    // Asignar el evento change a los checkboxes
    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            var filasSeleccionadas = document.querySelectorAll('input[name="seleccion[]"]:checked');
            var contenidoFilasSeleccionadas = Array.from(filasSeleccionadas).map(function(checkbox) {
                return checkbox.value;
            }).join(',');

            document.getElementById('filas-seleccionadas-contenido').value = contenidoFilasSeleccionadas;
            mostrarBotonYAlerta();
        });
    });

    // Verificar si se debe mostrar u ocultar el botón y la alerta al cargar la página
    mostrarBotonYAlerta();
});
