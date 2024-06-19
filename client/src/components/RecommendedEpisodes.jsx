/* eslint-disable react/prop-types */
import useFetch from '../hooks/useFetch';
import Loading from '../components/Loading';
import EpisodeList from './EpisodeList';

function RecommendedEpisodes({episode}) {
    const { data: episodes, loading, error } = useFetch(
        `http://localhost:5000/recommendations/${episode.season}/${episode.episode_number}`
    );

    if (loading) {
        return <Loading />;
    }

    if (error || !episode) {
        return <p>Error fetching data</p>;
    }

    return <EpisodeList episodes={episodes} />;

}

export default RecommendedEpisodes