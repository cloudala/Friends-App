/* eslint-disable react/prop-types */
function EpisodeEmotionsExtended({episode}) {
    return (
        <div className="flex justify-evenly gap-2 my-1 w-full -ml-6">
            <p className="flex flex-col items-center"><span>joy</span><span>🥳</span> <span>{episode.joy.toFixed(2)}</span></p>
            <p className="flex flex-col items-center"><span>surprise</span><span>😲</span> <span>{episode.surprise.toFixed(2)}</span></p>
            <p className="flex flex-col items-center"><span>sadness</span><span>😔</span> <span>{episode.sadness.toFixed(2)}</span></p>
            <p className="flex flex-col items-center"><span>neutral</span><span>😐</span> <span>{episode.neutral.toFixed(2)}</span></p>
            <p className="flex flex-col items-center"><span>fear</span><span>😨</span> <span>{episode.fear.toFixed(2)}</span></p>
            <p className="flex flex-col items-center"><span>anger</span><span>😡</span> <span>{episode.anger.toFixed(2)}</span></p>
            <p className="flex flex-col items-center"><span>disgust</span><span>🤢</span> <span>{episode.disgust.toFixed(2)}</span></p>
        </div>
    )
}

export default EpisodeEmotionsExtended