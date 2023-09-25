import React, { useState } from 'react';
import './FileUploader.css';
import {FiUpload} from 'react-icons/fi';
import {AiOutlineFileAdd} from 'react-icons/ai';

function FileUploader({setMessages}) {
  const [empirefile, setEmpireFile] = useState(null);
  const [falconfile, setFalconFile] = useState(null);

  const handleFileChange = (tag, file) => {
    switch (tag) {
      case 'empire':
        setEmpireFile(file);
        break;
      case 'falcon':
        setFalconFile(file);
        break;
      default:
        break;
    }
  };

  const getOdds = async (formData) => {
    const response = await fetch('http://localhost:8000/mfalcon/upload/', {
        method: 'POST',
        body: formData,
        });
        const {message} = await response.json();
        setMessages( (messages) => {
          return [...messages, message];
        });
  };
  const handleUpload = async () => {
    if (empirefile && falconfile) {

      const formData = new FormData();
      formData.append('empire', empirefile);
      formData.append('falcon', falconfile);
      getOdds(formData);
    } else {
      // todo jolify
      if (empirefile) {
        setMessages( (messages) => {
          return [...messages, 'Falcon file missing.'];
        });
      } else if (falconfile) {
        setMessages( (messages) => {
          return [...messages, 'Empire file missing.'];
        });
      } else {
        setMessages( (messages) => {
          return [...messages, 'Both files missing.'];
        });
      }
      
    }
  };

  return (
    <div className='FileUploader'>
      <div className='ButtonContainer'>
        <span>Empire</span>
        <input type="file" id='empirefile' accept=".json" onChange={(e) => handleFileChange('empire', e.target.files[0])} />
        <label htmlFor='empirefile' className={empirefile?'UploadedFile':''}><AiOutlineFileAdd/></label>
        <div/>
      </div>
      <div className='ButtonContainer'>
        <span>Falcon</span>
        <input type="file" id='falconfile' accept=".json" onChange={(e) => handleFileChange('falcon', e.target.files[0])} />
        <label htmlFor='falconfile' className={falconfile?'UploadedFile':''}><AiOutlineFileAdd/></label>
        <div/>
      </div>
      <div className='ButtonContainer'>
        <button onClick={handleUpload}><FiUpload/></button>
      </div>
    </div>
  );
}

export default FileUploader;
