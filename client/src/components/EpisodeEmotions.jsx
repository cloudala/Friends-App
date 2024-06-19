/* eslint-disable react/prop-types */
function EpisodeEmotions({episode}) {
    return (
        <div className="flex justify-around gap-2 my-4 w-full">
            <p className="flex flex-col items-center"><span>🥳</span> <span>{episode.joy.toFixed(2)}</span></p>
            <p className="flex flex-col items-center"><span>😲</span> <span>{episode.surprise.toFixed(2)}</span></p>
            <p className="flex flex-col items-center"><span>😔</span> <span>{episode.sadness.toFixed(2)}</span></p>
            <p className="flex flex-col items-center"><span>😐</span> <span>{episode.neutral.toFixed(2)}</span></p>
            <p className="flex flex-col items-center"><span>😨</span> <span>{episode.fear.toFixed(2)}</span></p>
            <p className="flex flex-col items-center"><span>😡</span> <span>{episode.anger.toFixed(2)}</span></p>
            <p className="flex flex-col items-center"><span>🤢</span> <span>{episode.disgust.toFixed(2)}</span></p>
        </div>
    )
}

export default EpisodeEmotions