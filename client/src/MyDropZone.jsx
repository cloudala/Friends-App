/* eslint-disable react/prop-types */
import { useCallback, useState } from 'react';
import { useDropzone } from 'react-dropzone';
import ResponseDisplay from './ResponseDisplay';

function MyDropzone({file, setFile}) {
  const apiUrl = 'http://localhost:5000/classify';
  // const [file, setFile] = useState(null);
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const onDrop = useCallback(acceptedFiles => {
    // Only take the first file
    setFile(acceptedFiles[0]);
  }, []);

  const { getRootProps, getInputProps } = useDropzone({ onDrop });

  const handleReset = () => {
    setFile(null);
    setResponse(null);
  };

  const handleSubmit = async () => {
    try {
      setLoading(true);
      const base64String = await readFileAsBase64(file);
      const data = { image_data: base64String };
      const response = await postData(apiUrl, data);
      setResponse(response);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={`flex gap-2 justify-center w-3/4 ${file && 'my-3'}`}>
      <div className={`flex flex-col ${!response && 'w-full'}`}>
        <div
          {...getRootProps()}
          className={`border-2 border-gray-300 border-dashed rounded-lg cursor-pointer p-5 flex flex-col justify-center items-center min-h-60 bg-opacity-60 ${
            response && 'pt-1'
          } ${file ? 'bg-opacity-100 bg-white border-none' : 'bg-gray-50'}`}
        >
          <input {...getInputProps()} />
          <p className={`text-lg text-gray-500 mb-4 ${file && 'hidden'}`}>Drag and drop an image, or click to select image file</p>
          {file && (
            <div className="mt-4">
              <h4 className="text-lg font-semibold text-gray-800 text-center">Chosen image:</h4>
              <div className="mt-2">
                <img src={URL.createObjectURL(file)} alt={file.name} style={{ width: 400 }} className="rounded-lg shadow-md" />
              </div>
            </div>
          )}
        </div>
        {file && (
          <div className="flex self-end gap-1">
            <button onClick={handleReset} className="bg-white text-black w-fit px-6 py-3 rounded-lg mt-4 hover:bg-gray-100 transition-colors duration-300">Remove Image</button>
            <button onClick={handleSubmit} className={`bg-violet-800 text-white w-fit px-6 py-3 rounded-lg mt-4 ${response && 'hidden'} hover:bg-purple-700 transition-colors duration-300`}>
              {loading ? "Magic in progress ..." : "Submit"}
            </button>
          </div>
        )}
      </div>
      {response && <ResponseDisplay response={response} />}
    </div>
  );

  async function readFileAsBase64(file) {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = () => {
        resolve(reader.result);
      };
      reader.onerror = reject;
      reader.readAsDataURL(file);
    });
  }

  async function postData(url, data) {
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    } catch (error) {
      console.error('Error:', error);
    }
  }
}

export default MyDropzone;
