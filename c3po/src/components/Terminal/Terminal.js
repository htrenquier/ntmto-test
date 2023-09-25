import React, { useState } from 'react';
import './Terminal.css';

function Terminal({messages}) {

  return (
    <div className='Terminal'>
      {messages.map((message, index) => {
        return (
          <div className='Line' key={index}>
            <span>MilleniumFalcon$ {message}</span>
          </div>
        );
      })
    }
        <div className='Line'>
            <span>MilleniumFalcon$</span>
        </div>
    </div>
  );
}

export default Terminal;
