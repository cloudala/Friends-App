/* eslint-disable react/prop-types */
const bgColorList = ['#FF4238', '#FFDC00', '#42A2D6', '#9A0006', '#FFF480'];

function EpisodeTags({episode}) {
    return (
        <div className="mt-2 flex flex-wrap gap-2">
        {episode.tags.map((tag, index) => (
            <span 
                key={index} 
                className="px-3 py-1 rounded-full text-black"
                style={{ backgroundColor: bgColorList[index % bgColorList.length] }}
            >
                {tag}
            </span>
        ))}
    </div>
    )
}

export default EpisodeTags