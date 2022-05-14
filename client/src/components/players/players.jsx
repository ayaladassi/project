// import playerService from "../services/playerService";
import { useFormik } from 'formik'
import { useEffect } from 'react'
import { useLocation } from 'react-router-dom';
import * as React from 'react';
import axios from "axios";
import { useNavigate } from 'react-router-dom'


export default function Index() {

    useEffect(() => {
        const interval = setInterval(() => {
           // const navigate = useNavigate();
            const getPlayers = (values) => {
                debugger
                console.log(values)
                debugger
                axios({
                    method: "GET",
                    url: "http://10.0.0.5:8000/getPlayer",
                    data: state.state.data['guid']
                })
                    .then((response) => {
                        console.log(response.data)
                        debugger
                        alert(response.data)
                    }).catch((error) => {
                        if (error.response) {
                            console.log(error.response)
                            console.log(error.response.status)
                            console.log(error.response.headers)
                        }
                    })
            }
        }, 2000);
        return () => clearInterval(interval);
    }, []);

    const state = useLocation()
    useEffect(() => {
        console.log(state);
         debugger
    }, []);
    const navigate = useNavigate();


    // let link = PlayerService.createGame();
    return (
        <div>
        
            <div><p>link: http://localhost:3000/JoinPlayer</p></div>
            {/* <div><a href={"mailto:" + state.state.data['link']}>{state.state.data['link']}</a></div> */}
            <div> <p>name: {state.state.data['name']}</p></div>
            <div> <p>role: {state.state.data['role']}</p></div>
            <div> <p>id: {state.state.data['id']}</p></div>
            <div><p>guid: {state.state.data['guid']} </p></div>
            <div><button>התחל משחק</button></div>


            {/* <form onSubmit={myFormik.handleSubmit}>
                <h1>שחקנים</h1>

                <button onClick={SetName} className="btn btn-primary" type="submit">צור משחק</button>
            </form> */}
        </div>
    )



};