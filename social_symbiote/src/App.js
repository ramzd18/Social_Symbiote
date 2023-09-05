import logo from './logo.svg';
import './App.css';
import ProfileList from './components/ProfileList.js'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Sidebar from './components/Sidebar';
function App() {
  return (
    <div>
      <Router>
        <Sidebar />
        <Routes>
          <Route path='/' exact component={ProfileList} />
          <Route path='/reports' component={ProfileList} />
          <Route path='/products' component={ProfileList} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
