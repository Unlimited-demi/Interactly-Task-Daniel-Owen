import React, { useState } from 'react';
import ProfileDisplay from './components/ProfileDisplay';

function App() {
    const [jobDescription, setJobDescription] = useState('');
    const [profiles, setProfiles] = useState(null);

    const handleSubmit = async () => {
        if (!jobDescription.trim()) {
            alert('Please enter a job description.');
            return;
        }

        try {
            const response = await fetch('/match', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ job_description: jobDescription }),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            setProfiles(data);
        } catch (error) {
            console.error('There was a problem with the fetch operation:', error);
            setProfiles('An error occurred while fetching the profiles.');
        }
    };

    return (
        <div className="container">
            <h1>Profile Matching System</h1>
            <textarea
                id="jobDescription"
                value={jobDescription}
                onChange={(e) => setJobDescription(e.target.value)}
                placeholder="Enter the job description here..."
            />
            <button id="submitButton" onClick={handleSubmit}>Find Matching Profiles</button>
            <ProfileDisplay profiles={profiles} />
        </div>
    );
}

export default App;
