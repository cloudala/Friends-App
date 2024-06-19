import { useContext } from 'react';
import { EpisodeContext } from '../contexts/EpisodeContext';
import EpisodeList from '../components/EpisodeList';
import Loading from '../components/Loading';

function EpisodesPage() {
    const { episodes, loading, error } = useContext(EpisodeContext);
    return (
        <>
          {loading ? (
            <Loading/>
          ) : !error ? (
            <>
                <EpisodeList episodes={episodes}/>
            </>
          ) : (
            <p>Error fetching data</p>
          )}
        </>
      );
}

export default EpisodesPage