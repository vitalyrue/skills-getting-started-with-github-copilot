import React from 'react';
import './ActivityCard.css';

function ActivityCard({ activity }) {
  return (
    <div className="activity-card">
      {/* Existing activity details */}
      <h2 className="activity-title">{activity.title}</h2>
      <p className="activity-description">{activity.description}</p>
      <p className="activity-date">{activity.date}</p>

      {/* Participants Section */}
      <div className="participants-section">
        <h3>Participants</h3>
        <ul className="participants-list">
          {activity.participants && activity.participants.length > 0 ? (
            activity.participants.map((p, idx) => (
              <li key={idx} className="participant-item">
                {p}
              </li>
            ))
          ) : (
            <li className="participant-item none">No participants yet.</li>
          )}
        </ul>
      </div>
    </div>
  );
}

export default ActivityCard;