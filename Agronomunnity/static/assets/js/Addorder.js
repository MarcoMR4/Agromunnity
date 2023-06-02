document.addEventListener('DOMContentLoaded', function() {
  const calidadSelect = document.getElementById("id_Calidad");
  const calibreSelect = document.getElementById("id_Calibre");
  const kgInput = document.getElementById("id_Kilos");
  const datos = document.getElementById("id_DatosT");
  const agregarButton = document.getElementById("agregartabla");
  const tabla = document.getElementById("tablaPedido");
  const totalKgInput = document.getElementById("id_Tkilos");
  const e1 = document.getElementById("e1");
  const e2 = document.getElementById("e2");
  const e3 = document.getElementById("e3");
  const completo = document.getElementById("completo");
  // Event listener para el botón "Agregar"
  agregarButton.addEventListener("click", function() {
    const kg = parseFloat(kgInput.value);
    const calidad = calidadSelect.value;
    const calibre = calibreSelect.value;
    if (!isNaN(kg) && !(calibre.trim().length === 0) && !(calidad.trim().length === 0)) {
      const calidad = calidadSelect.value;
      const calibre = calibreSelect.value;
      // Agregar la nueva fila a la tabla
      const row = tabla.insertRow(-1);
      const calidadCell = row.insertCell(0);
      calidadCell.innerHTML = calidad;
      const calibreCell = row.insertCell(1);
      calibreCell.innerHTML = calibre;
      const kgCell = row.insertCell(2);
      kgCell.innerHTML = kg;
      // Actualizar el total de kg
      actualizarTotalKg();
      // Eliminar la opción del select de calibre
      const calibreOption = calibreSelect.querySelector(`option[value="${calibre}"]`);
      calibreOption.remove();
      // Reiniciar los valores de los select y el input
      calidadSelect.selectedIndex = 0;
      calibreSelect.selectedIndex = 0;
      kgInput.value = "";
      const textodato = datos.value;
      const  insertardato = `${calidad},${calibre},${kg},`;
      datos.value = textodato ? textodato + insertardato : insertardato;
      // Ocultar los select y botón si no quedan opciones
      if (calibreSelect.children.length === 1) {
        calibreSelect.style.display = "none";
        calidadSelect.style.display = "none";
        kgInput.style.display="none"
        agregarButton.style.display = "none";
        e1.style.display="none";
        e2.style.display="none";
        e3.style.display="none";
      }

    }
  });

  // Función para actualizar el total de kg
  function actualizarTotalKg() {
    let total = 0;
    const filas = tabla.querySelectorAll("tr");
    for (let i = 1; i < filas.length; i++) {
      total += parseFloat(filas[i].querySelector("td:last-child").innerText);
    }
    totalKgInput.value = total;
    completo.value = "1";
  }
});