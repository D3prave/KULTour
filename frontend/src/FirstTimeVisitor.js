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
        <div style={{ display: 'flex', justifyContent: 'flex-start', top: '20px',   left: '80px' }}>
            <label style={{ backgroundColor: 'white', padding: '5px', borderRadius: '4px'}}>
                <input
                    type="checkbox"
                    checked={firstTimeVisitor}
                    onChange={handleCheckboxChange}
                />
                First Time Visitor
            </label>
            <button onClick={updateVisitorStatus} style={{ marginLeft: '10px' }}>OK</button>
        </div>


    )

};

export default FirstTimeVisitor;