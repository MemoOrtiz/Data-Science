async function hacerPrediccionRegresion() {
    // Capturar valores del formulario
    const edad = parseInt(document.getElementById('edad').value);
    const sexo = parseInt(document.getElementById('sexo').value);
    const escuela = parseInt(document.getElementById('escuela').value);
    const beca = parseInt(document.getElementById('beca').value);
    const trabajo = parseInt(document.getElementById('trabajo').value);
    const actividad = parseInt(document.getElementById('actividad').value);
    const pareja = parseInt(document.getElementById('pareja').value);
    const salario = parseInt(document.getElementById('salario').value);
    const transporte = parseInt(document.getElementById('transporte').value);
    const alojamiento = parseInt(document.getElementById('alojamiento').value);
    const educacionMadre = parseInt(document.getElementById('educacion_madre').value);
    const educacionPadre = parseInt(document.getElementById('educacion_padre').value);
    const hermanos = parseInt(document.getElementById('hermanos').value);
    const estadoParental = parseInt(document.getElementById('estado_parental').value);
    const ocupacionMadre = parseInt(document.getElementById('ocupacion_madre').value);
    const ocupacionPadre = parseInt(document.getElementById('ocupacion_padre').value);
    const horasEstudio = parseInt(document.getElementById('horas_estudio').value);
    const lecturaNoCientifica = parseInt(document.getElementById('lectura_no_cientifica').value);
    const lecturaCientifica = parseInt(document.getElementById('lectura_cientifica').value);
    const asistenciaSeminarios = parseInt(document.getElementById('asistencia_seminarios').value);
    const impactoProyectos = parseInt(document.getElementById('impacto_proyectos').value);
    const asistenciaClases = parseInt(document.getElementById('asistencia_clases').value);
    const preparacionExamen1 = parseInt(document.getElementById('preparacion_examen1').value);
    const preparacionExamen2 = parseInt(document.getElementById('preparacion_examen2').value);
    const tomarApuntes = parseInt(document.getElementById('tomar_apuntes').value);
    const escucharClases = parseInt(document.getElementById('escuchar_clases').value);
    const discusionMejora = parseInt(document.getElementById('discusion_mejora').value);
    const flipClassroom = parseInt(document.getElementById('flip_classroom').value);
    const promedioActual = parseInt(document.getElementById('promedio_actual').value);
    const promedioEsperado = parseInt(document.getElementById('promedio_esperado').value);

    // Crear el array de características en el orden correcto
    const features = [
        edad,                     // 1. Edad del estudiante
        sexo,                     // 2. Sexo
        escuela,                  // 3. Tipo de escuela secundaria
        beca,                     // 4. Tipo de beca
        trabajo,                  // 5. Trabajo adicional
        actividad,                // 6. Actividad artística o deportiva
        pareja,                   // 7. Tiene pareja
        salario,                  // 8. Salario total
        transporte,               // 9. Transporte a la universidad
        alojamiento,              // 10. Tipo de alojamiento en Chipre
        educacionMadre,           // 11. Educación de la madre
        educacionPadre,           // 12. Educación del padre
        hermanos,                 // 13. Número de hermanos
        estadoParental,           // 14. Estado parental
        ocupacionMadre,           // 15. Ocupación de la madre
        ocupacionPadre,           // 16. Ocupación del padre
        horasEstudio,             // 17. Horas de estudio semanales
        lecturaNoCientifica,      // 18. Frecuencia de lectura (libros/journals no científicos)
        lecturaCientifica,        // 19. Frecuencia de lectura (libros/journals científicos)
        asistenciaSeminarios,     // 20. Asistencia a seminarios/conferencias
        impactoProyectos,         // 21. Impacto de proyectos/actividades
        asistenciaClases,         // 22. Asistencia a clases
        preparacionExamen1,       // 23. Preparación para exámenes parciales 1
        preparacionExamen2,       // 24. Preparación para exámenes parciales 2
        tomarApuntes,             // 25. Tomar apuntes en clases
        escucharClases,           // 26. Escuchar en clases
        discusionMejora,          // 27. Discusión mejora interés y éxito
        flipClassroom,            // 28. Flip-classroom
        promedioActual,           // 29. Promedio de calificaciones acumulado del último semestre
        promedioEsperado          // 30. Promedio de calificaciones acumulado esperado en la graduación
    ];

    console.log("Datos enviados:", features); // Debugging

    try {
        // Enviar los datos al servidor
        const response = await fetch('/regresion', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ features: features })
        });

        if (!response.ok) {
            throw new Error(`Servidor respondió con estado ${response.status}`);
        }

        const resultado = await response.json();

        console.log("Respuesta del servidor:", resultado); // Debugging

        // Actualizar el HTML con el resultado
        // Asumiendo que el servidor devuelve un campo 'prediction' con el valor de la regresión
        const prediccion = resultado.prediction;
        document.getElementById('resultado-texto-regresion').innerText = prediccion;

    } catch (error) {
        console.error('Error en la predicción:', error);
        document.getElementById('resultado-texto-regresion').innerText = 'Error al obtener el resultado';
    }
}