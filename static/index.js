document.getElementById('match-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const jobDescription = document.getElementById('job-description').value;
    const source = document.getElementById('source').value;
    
    fetch('/match', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ job_description: jobDescription, source: source })
    })
    .then(response => response.json())
    .then(data => {
        const resultsContainer = document.getElementById('results');
        resultsContainer.innerHTML = '';
        
        data.split('-------------------------').forEach(profileText => {
            if (profileText.trim()) {
                const profileDiv = document.createElement('div');
                profileDiv.className = 'profile';
                
                profileText.split('\n').forEach(line => {
                    const p = document.createElement('p');
                    p.textContent = line;
                    profileDiv.appendChild(p);
                });
                
                resultsContainer.appendChild(profileDiv);
            }
        });
    })
    .catch(error => console.error('Error:', error));
});
