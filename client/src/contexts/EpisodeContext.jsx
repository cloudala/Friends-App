import { createContext, useEffect, useState } from 'react';
import useFetch from '../hooks/useFetch';
export const EpisodeContext = createContext();

// eslint-disable-next-line react/prop-types
export const EpisodeProvider = ({ children }) => {
    const { data, loading, error } = useFetch(
      'http://localhost:5000/episodes'
    );
    
    const [episodes, setEpisodes] = useState([]);

    useEffect(() => {
      if (!loading && !error) {
        setEpisodes(data);
      }
    }, [loading, error, data]);

    return (
    <EpisodeContext.Provider
        value={{
        episodes,
        setEpisodes,
        loading,
        error
        }}
    >
        {children}
    </EpisodeContext.Provider>
    );
};