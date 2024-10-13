const ctx = document.getElementById('radarChart').getContext('2d');
const radarChart = new Chart(ctx, {
    type: 'radar',
    data: {
        labels: ['Washing Machine', 'Game Gadgets', 'Sony Speakers', 'Dell Laptop', 'sonic LED'],
        datasets: [{
            label: 'Top 5 Products' ,
            data: [200, 100, 50, 40, 150],
            backgroundColor: 'rgba(228,218,253,0.54)',
            borderColor: 'rgb(228,218,253)',
            borderWidth: 2,
            pointBackgroundColor: 'rgba(225,14,51,0.54)',
        }]
    },
    options: {
        scales: {
            r: {
                beginAtZero: true,
                max: 250,
                pointLabels: {
                    font: {
                        size: 10 // Kích thước chữ nhỏ hơn
                    }
                },
                ticks: {
                    font: {
                        size: 8  // Kích thước chữ nhỏ hơn cho các số liệu
                    }
                }

            }
        },
        plugins: {
            legend: {
                display: false
            }
        }
    }
});