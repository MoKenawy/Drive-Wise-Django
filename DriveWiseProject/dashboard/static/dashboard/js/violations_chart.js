document.addEventListener('DOMContentLoaded', function() {
    const ctx = document.getElementById('violationsChart').getContext('2d');
    const speedViolationCount = parseInt(document.getElementById('speedViolationCount').textContent, 10);
    const distanceViolationCount = parseInt(document.getElementById('distanceViolationCount').textContent, 10);
    const drowsinessViolationCount = parseInt(document.getElementById('drowsinessViolationCount').textContent, 10);

    const violationsChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Speed Violations', 'Distance Violations', 'Drowsiness Violations'],
            datasets: [{
                label: 'Number of Violations',
                data: [speedViolationCount, distanceViolationCount, drowsinessViolationCount],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(75, 192, 192, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(75, 192, 192, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});
