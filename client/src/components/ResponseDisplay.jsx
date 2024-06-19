/* eslint-disable react/no-unescaped-entities */
import PropTypes from 'prop-types'

function ResponseDisplay({ response }) {
    return (
      <div className="bg-white shadow-lg rounded-lg p-6">
        <h2 className="text-xl font-semibold text-gray-800 mb-4">Ok, here's what we've got ... 🧐</h2>
        <div className="grid grid-cols-2 gap-4">
          <div>
            <p className="text-gray-600">Character:</p>
            <p className="text-gray-800 font-semibold">{response.character}</p>
          </div>
          <div>
            <p className="text-gray-600">Confidence:</p>
            <p className="text-gray-800 font-semibold">{response.confidence.toFixed(2)}</p>
          </div>
          <div>
            <p className="text-gray-600">Quote:</p>
            <p className="text-gray-800 font-semibold">{response.quote.quote}</p>
          </div>
          <div>
            <p className="text-gray-600">Episode Title:</p>
            <p className="text-gray-800 font-semibold">{response.quote.episode_title}</p>
          </div>
          <div>
            <p className="text-gray-600">Season:</p>
            <p className="text-gray-800 font-semibold">{response.quote.season}</p>
          </div>
          <div>
            <p className="text-gray-600">Episode Number:</p>
            <p className="text-gray-800 font-semibold">{response.quote.episode_number}</p>
          </div>
        </div>
      </div>
    );
  }

  ResponseDisplay.propTypes = {
    response: PropTypes.shape({
      character: PropTypes.string.isRequired,
      confidence: PropTypes.number.isRequired,
      quote: PropTypes.shape({
        episode_number: PropTypes.number.isRequired,
        episode_title: PropTypes.string.isRequired,
        quote: PropTypes.string.isRequired,
        season: PropTypes.number.isRequired,
      }).isRequired,
    }).isRequired,
  };
  
  export default ResponseDisplay;