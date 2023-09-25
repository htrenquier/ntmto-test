import './App.css';
import FileUploader from './components/FileUploader/FileUploader';
import Terminal from './components/Terminal/Terminal';
import { useState } from 'react';

function App() {
  const [messages, setMessages] = useState(['Please upload files to compute odds...']);
  return (
    <div className="AppContainer">
        <FileUploader setMessages={setMessages}/>
        <Terminal messages={messages}/>
    </div>
    
    
  );
}

export default App;