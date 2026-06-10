// Gráfico de barras - Promedio de reservas por día de la semana
new Chart(document.getElementById('reservasChart'), {
    type: 'bar',
    data: {
        labels: dias, // 👈 lista de días ["Lunes","Martes",...]
        datasets: [{
            label: 'Promedio de reservas',
            data: promedios, // 👈 lista de promedios [12, 9, 15, ...]
            backgroundColor: '#ffa384',
        }]
    },
    options: {
        responsive: true,
        plugins: {
            title: {
                display: true,
                text: 'Promedio Reservas x Día de la Semana',
                font: { size: 18, weight: 'bold' },
                color: '#f7f7f7'
            },
            legend: { display: false }
        },
        scales: {
            x: {
                ticks: {
                    color: '#f7f7f7'
                },
                grid: {
                    color: '#aaa'
                }
            },
            y: {
                beginAtZero: true,
                ticks: { stepSize: 3,
                    color: '#f7f7f7'
                },
                grid: {
                    color: '#aaa'
                }
            }
        }
    }
});

// Gráfico de torta - Estado de reservas
new Chart(document.getElementById('estadoChart'), {
    type: 'doughnut',
    data: {
        labels: Object.keys(estados),
        datasets: [{
            data: Object.values(estados),
            backgroundColor: ['#54a0ff', '#1dd1a1', '#ff6b6b']
        }]
    },
    options: {
        cutout: '60%',
        responsive: true,
        plugins: {
            title: {
                display: true,
                text: 'Estado de Reservas', // 👈 tu título
                font: {
                    size: 18,
                    weight: 'bold'
                },
                color: '#f7f7f7',
                padding: {
                    top: 10,
                    bottom: 20
                }
            },
            legend: { 
                position: 'right',
                labels: {
                    usePointStyle: true,
                    font: { size: 14 },
                    color: '#f7f7f7'
                }
            }
        }
    }
});

// Gráfico de barras - Categorías del menú
new Chart(document.getElementById('menuChart'), {
    type: 'bar',
    data: {
        labels: Object.keys(categorias), // 👈 dict con Comidas, Postres, Bebidas
        datasets: [{
            label: 'Cantidad de productos',
            data: Object.values(categorias),
            backgroundColor: ['#ff9f43', '#ee5253', '#10ac84']
        }]
    },
    options: {
        responsive: true,
        plugins: {
            title: {
                display: true,              // 👈 activa el título
                text: 'Menú de Restaurante', // 👈 texto del título
                font: {
                    size: 18,
                    weight: 'bold'
                },
                color: '#f7f7f7'               // 👈 color del texto
            },
            legend: { display: false }
        },
        scales: {
            x: {
                ticks: {
                    color: '#f7f7f7'
                },
                grid: { color: '#233338'}
            },
            y: {
                beginAtZero: true,
                ticks: { stepSize: 5, color: '#f7f7f7' },
                grid: {color: '#233338'}
            }
        }
    }
});
