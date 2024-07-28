import React from 'react';

function ProfileDisplay({ profiles }) {
    return (
        <div className="profile-display">
            {profiles && profiles.length > 0 ? (
                profiles.map((profile, index) => (
                    <div key={index} className="profile-item">
                        <h3>Profile {index + 1}</h3>
                        <pre>{JSON.stringify(profile, null, 2)}</pre>
                    </div>
                ))
            ) : (
                <p>No profiles to display.</p>
            )}
        </div>
    );
}

export default ProfileDisplay;
