import React, { useState } from 'react';

const FirstTimeVisitor = () => {
    const [firstTimeVisitor, setFirstTimeVisitor] = useState(false);

    const handleCheckboxChange = () => {
        setFirstTimeVisitor(!firstTimeVisitor);
    };

    const updateVisitorStatus = () => {
        fetch('http://localhost:5000/update_first_time_visitor', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ first_time_visitor: firstTimeVisitor })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                alert('Visitor status updated successfully.');
            } else {
                alert('Error updating visitor status.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    };

    return (
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'flex-start', top: '20px', left: '80px' }}>
            <label className='' style={{ display: 'flex', alignItems: 'center', justifyContent: 'flex-start', gap: '5px', padding: '5px', borderRadius: '4px', backgroundColor: 'none', color: '#fff', fontWeight: 'bold', textShadow: '-1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black, 1px 1px 0 black' }}>
                <input
                    type="checkbox"
                    checked={firstTimeVisitor}
                    onChange={handleCheckboxChange}
                />
                First Time Visitor
            </label>
        </div>
    )

};

export default FirstTimeVisitor;