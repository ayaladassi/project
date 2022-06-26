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

    const getPlayers = () => {
        axios({
            method: "GET",
            url: "http://192.168.49.42:8000/getPlayer",
        })
            .then((response) => {

                setarrPlayer(response.data)
            }).catch((error) => {
                if (error.response) {
                    console.log(error.response)
                    console.log(error.response.status)
                    console.log(error.response.headers)
                }
            })
    }
    const getStatusStart = () => {
        axios({
            method: "GET",
            url: "http://192.168.49.42:8000/checkStartGame",
        })
            .then(async(response) => {
                if(response.data=="True"){
                    await new Promise(r => setTimeout(r, 1000));

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
    const startGame = () => {
        axios({

            method: "GET",
            url: "http://192.168.49.42:8000/startGame",
        })
            .then(async(response) => {
                // alert(response.data)
                if (response.data == "True") {
                    alert('Computer players were added to the game')
                    await new Promise(r => setTimeout(r, 1000));


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

    const location = useLocation()

    useEffect(() => {
        const interval = setInterval(() => {
            getPlayers();
            getStatusStart();
            
        }, 500);
        return () => clearInterval(interval);
    }, []);

    const navigate = useNavigate();
    const getUserPlayer=()=>{
        return <div style={{color:location.state.data["color"]?location.state.data["color"]:'black'}} className="palyer-user">
                       <span>{location.state.data["name"]} | {location.state.data["role"]}</span>

            <i className="fa fa-user user" aria-hidden="true"></i>
        </div>
    }

    return (
        <div>

            <h1>Code name</h1>
            <div>
                <p>link to join</p> <input type="text" value="localhost:3000/JoinPlayer" id="link-access" size="25" readonly></input></div>

            <div>
                <p></p>
            </div>
            <div></div>
            <div style={{display:'flex',position:'relative'}}>{getUserPlayer()}</div>

            {/* <div className="auto"> <p>id: {location.state.data["id"]},   role: {location.state.data["role"]},   name: {location.state.data["name"]},   color: {location.state.data["color"]}</p></div> */}
<br></br>
<br></br>
<br></br>
<br></br>

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

            <div><button className="btn btn-primary" onClick={startGame}>התחל משחק</button></div>
        </div>
    )



};