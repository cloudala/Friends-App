import { useState, useEffect } from 'react';

export default function useFetch(api) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    fetch(api)
      .then((response) => {
        if (!response.ok) {
          setError(true);
        }
        return response.json();
      })
      .then((fetchedData) => {
        setData(fetchedData);
        setLoading(false);
        console.log(fetchedData)
      })
      // eslint-disable-next-line no-unused-vars
      .catch((err) => {
        setLoading(false);
        setError(true);
      });
  }, [api]);

  // Return the state and functions to be used by components
  return { data, loading, error };
}