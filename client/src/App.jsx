import {useState} from 'react';
import MyDropzone from './MyDropZone.jsx';
import Header from './Header.jsx';
import Footer from './Footer.jsx';

function App() {
  const [file, setFile] = useState(null);
  return (
    <>
      <Header/>
      <div className={`min-h-custom flex justify-center items-center ${file ? 'bg-purple' : 'bg-hero bg-cover bg-center'}`}>
        <MyDropzone file={file} setFile={setFile}/>
      </div>
      <Footer/>
    </>
  );
}

export default App;
