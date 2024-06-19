import {useState} from 'react';
import MyDropzone from '../components/MyDropZone.jsx';

function ImageClassificationPage() {
    const [file, setFile] = useState(null);
    return (
        <div className={`min-h-custom flex justify-center items-center ${file ? 'bg-purple' : 'bg-hero bg-cover bg-center'}`}>
            <MyDropzone file={file} setFile={setFile}/>
        </div>
    );
}

export default ImageClassificationPage