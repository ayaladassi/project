import { useState } from 'react'
import axios from "axios";
import logo from './logo.svg';
import './App.css';
 
function App() {

  //const [profileData, setProfileData] = useState(null)
  function getfromserver(){
   axios.get('http://192.168.49.42:8000/createGame?playerName=dassi').then((response)=>{
     alert(response.data.name)
     alert(response.data.message)})
  }
  return (
    <div className="App">
      <button onClick={getfromserver}>click here to get response from server</button>
    </div>
  );
}
 
export default App;

