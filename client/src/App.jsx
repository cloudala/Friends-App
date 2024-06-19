import { Routes, Route } from 'react-router-dom';
import ImageClassificationPage from './pages/ImageClassificationPage.jsx';
import EpisodesPage from './pages/EpisodesPage.jsx';
import Header from './components/Header.jsx';
import Footer from './components/Footer.jsx';
import EpisodeDetailsPage from './pages/EpisodeDetailsPage.jsx';

function App() {
  return (
    <>
      <Header/>
        <Routes>
          <Route path='/' element={<ImageClassificationPage/>}/>
          <Route path='/episodes' element={<EpisodesPage/>}/>
          <Route path='/episodes/:season/:episode_number' element={<EpisodeDetailsPage/>}/>
        </Routes>
      <Footer/>
    </>
  )
}

export default App;
