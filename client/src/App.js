import { useState } from 'react'
import axios from "axios";
import logo from './logo.svg';
import * as React from "react";
// import { Routes, Route, Link } from "react-router-dom";
import "../node_modules/bootstrap/dist/css/bootstrap.min.css";

import { Routes, Route } from 'react-router-dom'

import './App.css';
import Index from '../src/components/index/index.jsx';
import Player from '../src/components/players/players.jsx';
import JoinPlayer from '../src/components/joinPlayer/joinPlayer.jsx';
import Board from '../src/components/board/board';
import Winner from '../src/components/winner/winner';
import Card from '../src/components/card/card'
function App() {
    
  return (
    // <Provider store={store}>
        <div className="App">
            <div className="row justify-content-center">
                <div >

                    <Routes>
                        <Route path="/" element={<Index></Index>}></Route>
                        <Route path="/players/:role" element={<Player></Player>}></Route>
                        <Route path="/JoinPlayer" element={<JoinPlayer></JoinPlayer>}></Route>
                        <Route path="/board/:role" element={<Board></Board>}></Route>
                        <Route path="/card" element={<Card></Card>}></Route>
                        <Route path="/winner" element={<Winner></Winner>}></Route>
                        

                    </Routes>
                </div>
            </div>
          
        </div>

    // </Provider>
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

