/* eslint-disable react/prop-types */
import EpisodeCard from "./EpisodeCard";

function EpisodeList({ episodes }) {
    return (
        <div className="flex items-start justify-around bg-black">
            <ul className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-3 gap-4 py-3 px-2 md:px-6 lg:px-8">
            {episodes.map((episode, id) => <EpisodeCard key={id} episode={episode}/>)}
            </ul>
        </div>
    )
}

export default EpisodeList