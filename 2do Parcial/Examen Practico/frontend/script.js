document.addEventListener('DOMContentLoaded', () => {
    // Definimos paleta de colores para gráficos
    const colors = [
        'rgba(56, 189, 248, 0.8)',
        'rgba(139, 92, 246, 0.8)',
        'rgba(244, 114, 182, 0.8)',
        'rgba(52, 211, 153, 0.8)',
        'rgba(251, 191, 36, 0.8)',
        'rgba(248, 113, 113, 0.8)'
    ];

    const borderColors = colors.map(c => c.replace('0.8', '1'));

    // Configuración global para Chart.js oscura
    Chart.defaults.color = '#94a3b8';
    Chart.defaults.borderColor = 'rgba(255, 255, 255, 0.1)';

    // --- CARGAR ESTADÍSTICAS (Media, Mediana, Moda) ---
    fetch('/api/statistics')
        .then(res => res.json())
        .then(data => {
            if (data.Price) {
                document.getElementById('mean-price').textContent = `$${data.Price.mean}`;
                document.getElementById('median-price').textContent = `$${data.Price.median}`;
                document.getElementById('mode-price').textContent = `$${data.Price.mode}`;
            }
            if (data.Rating) {
                document.getElementById('mean-rating').textContent = `${data.Rating.mean} ★`;
                document.getElementById('median-rating').textContent = `${data.Rating.median} ★`;
                document.getElementById('mode-rating').textContent = `${data.Rating.mode} ★`;
            }
        });

    // --- CARGAR FRECUENCIAS CATEGÓRICAS (Barras y Pastel) ---
    fetch('/api/categorical-frequencies')
        .then(res => res.json())
        .then(data => {
            const labels = data.map(d => d.label);
            const absoluteData = data.map(d => d.absolute);
            const relativeData = data.map(d => d.relative.toFixed(2));

            // Gráfica de Barras (Frecuencias Absolutas)
            new Chart(document.getElementById('barChart'), {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Cantidad de Libros',
                        data: absoluteData,
                        backgroundColor: 'rgba(56, 189, 248, 0.8)',
                        borderColor: 'rgba(56, 189, 248, 1)',
                        borderWidth: 1,
                        borderRadius: 4
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        y: { beginAtZero: true }
                    }
                }
            });

            // Gráfica de Pastel (Frecuencias Relativas)
            new Chart(document.getElementById('pieChart'), {
                type: 'polarArea', // El examen sugiere pastel o polar
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Porcentaje (%)',
                        data: relativeData,
                        backgroundColor: colors,
                        borderColor: borderColors,
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false
                }
            });
        });

    // --- CARGAR FRECUENCIAS CONTINUAS (Líneas y Área) ---
    fetch('/api/continuous-frequencies')
        .then(res => res.json())
        .then(data => {
            const labels = data.map(d => d.label);
            const absoluteData = data.map(d => d.absolute);
            const cumulativeData = data.map(d => d.cumulative);

            // Polígono de Frecuencias (Absolutas) y Frecuencias Acumuladas
            new Chart(document.getElementById('lineChart'), {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [
                        {
                            label: 'Frecuencia Acumulada',
                            data: cumulativeData,
                            backgroundColor: 'rgba(139, 92, 246, 0.2)',
                            borderColor: 'rgba(139, 92, 246, 1)',
                            borderWidth: 2,
                            fill: true,
                            tension: 0.4
                        },
                        {
                            label: 'Polígono de Frecuencia',
                            data: absoluteData,
                            backgroundColor: 'transparent',
                            borderColor: 'rgba(56, 189, 248, 1)',
                            borderWidth: 2,
                            pointBackgroundColor: 'rgba(56, 189, 248, 1)',
                            pointRadius: 4,
                            fill: false,
                            tension: 0.1
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    interaction: {
                        mode: 'index',
                        intersect: false,
                    },
                    scales: {
                        y: { beginAtZero: true }
                    }
                }
            });
        });
});
