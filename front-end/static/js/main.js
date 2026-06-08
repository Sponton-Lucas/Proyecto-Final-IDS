
const carruseltracker= document.getElementById('carrusel-tracker');

if (carruseltracker) {
    const comentarios = document.querySelectorAll('.comentarios');
    const botonPrev = document.getElementById('prev-flecha');
    const botonNext = document.getElementById('next-flecha');

    let comentariosActual = 0; 
    const totalComentarios= comentarios.length;
    
    function moverCarrusel() {
         let desplazamiento = -(comentariosActual * 100);
         carruseltracker.style.transform = `translateX(${desplazamiento}%)`;
    }

    botonNext.addEventListener('click', () => {
         if (comentariosActual < totalComentarios - 1) {
            comentariosActual++;
        } else {
            comentariosActual = 0;
        }
        moverCarrusel();
    });

    botonPrev.addEventListener('click', () => {
         if (comentariosActual > 0) {
            comentariosActual--;
        } else {
            comentariosActual = totalComentarios - 1;
        }
        moverCarrusel();
    });
}

/*parte del admin nuevo articulo*/
const categoria = document.getElementById("categoria");

if (categoria) {
    categoria.addEventListener("change", function () {

        const comida = document.getElementById("campos-comida");
        const bebida = document.getElementById("campos-bebida");

        if (this.value === "bebida") {
            comida.style.display = "none";
            bebida.style.display = "block";
        } else {
            comida.style.display = "block";
            bebida.style.display = "none";
        }
    });
}
