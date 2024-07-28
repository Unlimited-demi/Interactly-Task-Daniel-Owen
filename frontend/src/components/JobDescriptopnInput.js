import React from 'react';

function JobDescriptionInput({ jobDescription, setJobDescription }) {
    return (
        <textarea
            value={jobDescription}
            onChange={(e) => setJobDescription(e.target.value)}
            placeholder="Enter job description"
        />
    );
}

export default JobDescriptionInput;
