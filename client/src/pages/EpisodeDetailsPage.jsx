import { useParams } from 'react-router-dom';
import useFetch from '../hooks/useFetch';
import EpisodeDetails from '../components/EpisodeDetails';
import Loading from '../components/Loading';

export default function EpisodeDetailsPage() {
  const { season, episode_number } = useParams()
  const { data: episode, loading, error } = useFetch(
    `http://localhost:5000/episodes/${season}/${episode_number}`
  );

    if (loading) {
        return <Loading />;
    }

    if (error || !episode) {
        return <p>Error fetching data</p>;
    }

    return <EpisodeDetails episode={episode} />;
}