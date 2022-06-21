// import playerService from "../services/playerService";
import { useFormik } from 'formik'
import { useEffect } from 'react'
import { useLocation } from 'react-router-dom';
import * as React from 'react';
import axios from "axios";
import { useNavigate } from 'react-router-dom'
import AddItem from './addItem'
import { useState } from 'react';
import "./players.css"
import 'bootstrap/dist/css/bootstrap.min.css';




export default function Index() {

    const [arrPlayer, setarrPlayer] = useState([])



    // useEffect(() => {
    //     const intervalId = setInterval(() => {
    //         setCountRemaining(countRemaining - 1);
    //     }, 1000)

    //     return () => {
    //         clearInterval(intervalId);
    //     }
    // })
    const getPlayers = () => {
        axios({
            method: "GET",
            url: "http://10.0.0.5:8000/getPlayer",
        })
            .then((response) => {

                console.log(response.data)
                debugger
                alert(response.data)
                setarrPlayer(response.data)
            }).catch((error) => {
                if (error.response) {
                    console.log(error.response)
                    console.log(error.response.status)
                    console.log(error.response.headers)
                }
            })
    }
    const startGame = () => {
        debugger
        axios({

            method: "GET",
            url: "http://10.0.0.5:8000/startGame",
        })
            .then((response) => {
                debugger
                alert(response.data)
                if (response.data == "True") {

                    navigate('../board', { state: location.state.data })
                }

            }).catch((error) => {
                if (error.response) {
                    console.log(error.response)
                    console.log(error.response.status)
                    console.log(error.response.headers)
                }
            })

    }

    // useEffect((values) => {
    //     const interval = setInterval(() => {
    //         // const navigate = useNavigate();
    //         getPlayers();

    //     }, 2000);
    //     return () => clearInterval(interval);
    // }, []);
    debugger
    const location = useLocation()
    // useEffect(() => {
    //     console.log(state);
    //     debugger
    // }, []);
    const navigate = useNavigate();




    // let link = PlayerService.createGame();
    return (
        <div>

            <h1>Code name</h1>
            <div>
                <p>link to join</p> <input type="text" value="localhost:3000/JoinPlayer" id="link-access" size="25" readonly></input></div>
            {/* <div>
            <p>guid</p> <input type="text" value={location.state.data[0]["guid"]} id="link-access" size="50" readonly></input></div>
           <div> <p>id: {location.state.data['id']}</p></div> */}
            {/* <div>
                <input type="text" value="link: localhost:3000/JoinPlayer" id="link-access" size="80" readonly></input>
                    <img class="d-inline-block align-top" src="../../../copy.png" onclick="datatable.copyLink()" />
            </div> */}

            {/* <div><p>link: localhost:3000/JoinPlayer </p></div> */}
            {/* <div><a href={"mailto:" + state.state.data['link']}>{state.state.data['link']}</a></div> 
            <div> <p>name: {location.state.data['name']}</p></div>
            <div> <p>role: {location.state.data['role']}</p></div>
            <div> <p>id: {location.state.data['id']}</p></div> */}
            {/* <div><p>guid: {location.state.data[0]["guid"]} </p></div> */}
            <div>
                <p></p>
            </div>
            <div><button className="btn btn-primary" onClick={getPlayers}>get players</button></div>
            <div></div>

            {/* <div> <p>id: {location.state.data["0"]["id"]}</p></div> */}
            <div> <p>id: {location.state.data["id"]}</p></div>
            <div> <p>name: {location.state.data["name"]}</p></div>
            <div> <p>role: {location.state.data["role"]}</p></div>
            <div> <p>color: {location.state.data["color"]}</p></div>




            {/* <div> <p>role: {location.state.data["0"]["role"]}</p></div> */}

            <table className="table table-dark">
                <thead>
                    <tr className="table-active">
                        <th scope="col">id</th>
                        <th scope="col">name</th>
                        <th scope="col">role</th>
                        <th scope="col">color</th>


                    </tr>
                </thead>
                <tbody>
                    {arrPlayer.map((item) => <AddItem Item={item}></AddItem>)}

                </tbody>
            </table>


            {/* <form onSubmit={myFormik.handleSubmit}>
                <h1>שחקנים</h1>

                <button onClick={SetName} className="btn btn-primary" type="submit">צור משחק</button>
            </form> */}
            <div><button className="btn btn-primary" onClick={startGame}>התחל משחק</button></div>
        </div>
    )



};