// import playerService from "../services/playerService";
import { useFormik } from 'formik'
import { useEffect } from 'react'
import { useLocation } from 'react-router-dom';
import * as React from 'react';
import axios from "axios";
import { useNavigate } from 'react-router-dom'
import AddItem from './addItem'
import { useState } from 'react';




export default function Index() {

  const [arrPlayer, setarrPlayer]=useState([])



    // useEffect(() => {
    //     const intervalId = setInterval(() => {
    //         setCountRemaining(countRemaining - 1);
    //     }, 1000)

    //     return () => {
    //         clearInterval(intervalId);
    //     }
    // })
    const getPlayers = (values) => {
        
        console.log(values)
        
        axios({
            method: "GET",
            url: "http://10.0.0.5:8000/getPlayer",
            data: location.state.data['guid']
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

    useEffect((values) => {
        const interval = setInterval(() => {
            // const navigate = useNavigate();
            getPlayers(values);

        }, 2000);
        return () => clearInterval(interval);
    }, []);

    const location = useLocation()
    // useEffect(() => {
    //     console.log(state);
    //     debugger
    // }, []);
    const navigate = useNavigate();


    // let link = PlayerService.createGame();
    return (
        <div>
             debugger
            <div><p>link: localhost:3000/JoinPlayer</p></div>
            {/* <div><a href={"mailto:" + state.state.data['link']}>{state.state.data['link']}</a></div> */}
            <div> <p>name: {location.state.data['name']}</p></div>
            <div> <p>role: {location.state.data['role']}</p></div>
            <div> <p>id: {location.state.data['id']}</p></div>
            <div><p>guid: {location.state.data['guid']} </p></div>
            <div><button>התחל משחק</button></div>
            <table className="table table-dark">
                <thead>
                    <tr className="table-active">
                        <th scope="col">name</th>
                        <th scope="col">role</th>
                        <th scope="col">id</th>
                        <th scope="col">guid</th>
                        <th scope="col">color</th>


                    </tr>
                </thead>
                <tbody>
                    {location.state.data.map((item) => <AddItem Item={item}></AddItem>)}
                </tbody>
            </table>


            {/* <form onSubmit={myFormik.handleSubmit}>
                <h1>שחקנים</h1>

                <button onClick={SetName} className="btn btn-primary" type="submit">צור משחק</button>
            </form> */}
        </div>
    )



};