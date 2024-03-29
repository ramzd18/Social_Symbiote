import './App.css';
import AccountC from './componets/AccountC';
import Alias from './componets/Alias';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Signin from './componets/Signin';
import Workplace from './componets/Workplace';
import Invite from './componets/Invite';
import Home from './componets/Home';
import Person from './componets/Person';
import Popup from './componets/Popup';
import Interviews from './componets/Interviews';
import Interface from './componets/Interface';
import Report from './componets/Report';
import ReportPopup from './componets/ReportPopup';
import Usabillity from './componets/Usability';




function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path='/' element={<Alias />}></Route>
          <Route path='/accountcreation' element={<AccountC />}></Route>
          <Route path='/signin' element={<Signin />}></Route>
          <Route path='/workplace' element={<Workplace />}></Route>
          <Route path='/invite' element={<Invite />}></Route>
          <Route path='/home' element={<Home />}></Route>
          <Route path='/person' element={<Person />}></Route>
          <Route path='/popup' element={<Popup />}></Route>
          <Route path='/interviews' element={<Interviews />}></Route>
          <Route path='/interface' element={<Interface />}></Route>
          <Route path='/reports' element={<Report />}></Route>
          <Route path='/reportpopup' element={<ReportPopup />}></Route>
          <Route path='/testing' element={<Usabillity />}></Route>



        </Routes>
      </Router>
    </div>


  );
}

export default App;
