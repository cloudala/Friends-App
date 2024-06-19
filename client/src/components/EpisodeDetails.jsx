/* eslint-disable react/prop-types */
import EpisodeWordCloud from "./EpisodeWordCloud"
import EpisodeTags from "./EpisodeTags"
import EpisodeEmotionsExtended from "./EpisodeEmotionsExtended"
import RecommendedEpisodes from "./RecommendedEpisodes"

function EpisodeDetails({episode}) {
    return (
        <div className="bg-black py-2 px-2 text-white">
            <div className="flex gap-10 w-7/8">
                <div className="w-3/4 rounded-t-lg">
                    <EpisodeWordCloud season={episode.season} episode={episode.episode_number}/>
                </div>
                <div>
                    <p className="mt-2 text-xl font-bold">{episode.episode_title}</p>
                    <p className="mt-2 text-gray-400">Season: {episode.season} Episode: {episode.episode_number}</p>
                    <div className="mt-10">
                        <p className="mt-2 text-gray-400">The One About ...</p>
                        <EpisodeTags episode={episode}/>
                    </div>
                    <div className="mt-10">
                        <p className="mt-2 text-gray-400">The One With Feelings Of ...</p>
                        <EpisodeEmotionsExtended episode={episode}/>
                    </div>
                </div>
            </div>
            <div className="w-7/8 mt-5">
                <p className="text-xl text-center text-gray-200">The Ones Similar to {episode.episode_title} ...</p>
                <RecommendedEpisodes episode={episode}/>
            </div>
        </div>
    )
}

export default EpisodeDetails