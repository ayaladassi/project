import { useState } from 'react'
import axios from "axios";
import logo from './logo.svg';

import { Routes, Route } from 'react-router-dom'

import './App.css';
import index from '../src/components/index/index'
import players from '../src/components/players/players'
 
function App() {
  
  return (
    <Provider store={store}>
        <div className="App">
            <div className="row justify-content-center">
                <div >

                    <Routes>
                        <Route path="/" element={<index></index>}></Route>
                        <Route path="/players" element={<players></players>}></Route>

                        <Route path="Header/" element={<Header></Header>}>
                            <Route path="Home" element={<Home></Home>}></Route>
                            <Route path="About" element={<About></About>}></Route>
                            <Route path="AllApi" element={<ApiList></ApiList>}></Route>
                            <Route path="AddApi" element={<AddApi></AddApi>}></Route>
                            <Route path="UpdateApi" element={<AddApi></AddApi>}></Route>
                        </Route>

                    </Routes>
                </div>
            </div>
        </div>

    </Provider>
);













  // //const [profileData, setProfileData] = useState(null)
  // function getfromserver(){
  //  axios.get('http://192.168.49.42:8000/createGame?playerName=dassi').then((response)=>{
  //    alert(response.data.name)
  //    alert(response.data.message)})
  // }
  // return (
  //   <div className="App">
  //     <button onClick={getfromserver}>click here to get response from server</button>
  //   </div>
  // );
}
 
export default App;

