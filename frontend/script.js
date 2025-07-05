document.getElementById('projectForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const backendLanguage = document.getElementById('backend_language').value;
    const databaseType = document.getElementById('database_type').value;
    const expectedTraffic = document.getElementById('expected_traffic').value;
    const dataSize = document.getElementById('data_size').value;

    try {
        console.log('Submitting payload', { lang: backendLanguage, db: databaseType, expected_traffic: expectedTraffic, data_size: dataSize });
        const response = await fetch('/api/projects/recommend/', {  // fixed endpoint path
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                lang: backendLanguage,
                db: databaseType,
                expected_traffic: expectedTraffic,
                data_size: dataSize
            })
        });
        console.log('Response status:', response.status);
        if (!response.ok) {
            const text = await response.text();
            console.error('Response text:', text);
            throw new Error('Failed to fetch recommendations');
        }

        const data = await response.json();
        console.log('Received data', data);
        const recommendationList = document.getElementById('recommendationList');
        recommendationList.innerHTML = '';

        const debugElem = document.getElementById('debugReceived');
        if (debugElem) {
            debugElem.textContent = JSON.stringify(data.received || {}, null, 2);
        }

        if (!data.recommendations || data.recommendations.length === 0) {
            const li = document.createElement('li');
            li.textContent = 'No recommendations found for the given parameters.';
            recommendationList.appendChild(li);
            return;
        }

        data.recommendations.forEach(rec => {
            const li = document.createElement('li');
            li.textContent = `${rec.name}: ${rec.description} (Score: ${rec.score})`;
            recommendationList.appendChild(li);
        });
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while fetching recommendations. See console for details.');
    }
});

// Update slider value displays
const expectedTraffic = document.getElementById('expected_traffic');
const expectedTrafficValue = document.getElementById('expected_traffic_value');
expectedTraffic.addEventListener('input', function() {
    expectedTrafficValue.textContent = expectedTraffic.value;
});

const dataSize = document.getElementById('data_size');
const dataSizeValue = document.getElementById('data_size_value');
dataSize.addEventListener('input', function() {
    dataSizeValue.textContent = dataSize.value;
});
