/* eslint-disable react/prop-types */
function EpisodeWordCloud({ season, episode }) {
    const imageUrl = `/season_${season}.0_episode_${episode}.0_wordcloud.png`;

    return (
        <div>
            <img src={imageUrl} alt={`Wordcloud for Season ${season}, Episode ${episode}`} />
        </div>
    );
}

export default EpisodeWordCloud;
