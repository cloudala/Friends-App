/* eslint-disable react/prop-types */
import { Link } from 'react-router-dom'
import EpisodeWordCloud from './EpisodeWordCloud';
import EpisodeEmotions from './EpisodeEmotions';
import EpisodeTags from './EpisodeTags';

function EpisodeCard({ episode }) {
    return (
        <Link to={`/episodes/${episode.season}/${episode.episode_number}`}>
            <div className="flex flex-col items-start p-4 border-2 border-slate-700 rounded-lg shadow-md bg-black text-white cursor-pointer h-full">
                <EpisodeWordCloud season={episode.season} episode={episode.episode_number} />
                <p className="mt-2 text-xl font-bold">{episode.episode_title}</p>
                <p className="mt-1 text-gray-400">Season: {episode.season} Episode: {episode.episode_number}</p>
                <EpisodeTags episode={episode}/>
                <EpisodeEmotions episode={episode}/>
            </div>
        </Link>
    );
}

export default EpisodeCard;