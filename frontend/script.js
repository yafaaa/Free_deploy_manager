document.getElementById('projectForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const backendLanguage = document.getElementById('backend_language').value;
    const databaseType = document.getElementById('database_type').value;
    const features = document.getElementById('features').value.split(',').map(f => f.trim());

    try {
        const response = await fetch('http://127.0.0.1:8000/api/recommend/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                lang: backendLanguage,
                db: databaseType,
                feature: features
            })
        });

        if (!response.ok) {
            throw new Error('Failed to fetch recommendations');
        }

        const data = await response.json();
        const recommendationList = document.getElementById('recommendationList');
        recommendationList.innerHTML = '';

        data.recommendations.forEach(rec => {
            const li = document.createElement('li');
            li.textContent = `${rec.name}: ${rec.description} (Score: ${rec.score})`;
            recommendationList.appendChild(li);
        });
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while fetching recommendations.');
    }
});
