async function hacerPrediccionClasificacion() {
    // Capturar valores del formulario
    const genero = document.getElementById('genero').value;
    const age = parseFloat(document.getElementById('age').value);
    const hypertension = document.getElementById('hypertension').value;
    const heart_disease = document.getElementById('heart_disease').value;
    const ever_married = document.getElementById('ever_married').value;
    const residence_type = document.getElementById('residence_type').value;
    const avg_glucose_level = parseFloat(document.getElementById('avg_glucose_level').value);
    const bmi = parseFloat(document.getElementById('bmi').value);

    // Desglosar opciones seleccionadas (Tipo de Trabajo y Estado de Fumador)
    const work_type = document.getElementById('work_type').value.split(',').map(Number);
    const smoking_status = document.getElementById('smoking_status').value.split(',').map(Number);

    // Crear el array de características
    const features = [
        parseInt(genero), age, parseInt(hypertension), parseInt(heart_disease), 
        parseInt(ever_married), parseInt(residence_type),
        avg_glucose_level, bmi,
        ...work_type,
        ...smoking_status
    ];

    console.log("Datos enviados:", features); // Debugging

    try {
        // Enviar los datos al servidor
        const response = await fetch('/clasificacion', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ features: features })
        });

        const resultado = await response.json();

        // Actualizar el HTML con el resultado
        const resultadoTexto = resultado.prediction[0] === 1 ? 'Sí' : 'No';
        document.getElementById('resultado-texto').innerText = resultadoTexto;

    } catch (error) {
        console.error('Error en la predicción:', error);
        document.getElementById('resultado-texto').innerText = 'Error al obtener el resultado';
    }
}