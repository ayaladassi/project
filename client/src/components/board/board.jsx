import { useState } from 'react'
import { useFormik } from 'formik'
import axios from "axios";
import { useNavigate, useParams } from 'react-router-dom'
import * as React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './board.css'
import { useLocation } from 'react-router-dom';


export default function board() {
    // useState[roleid,role]
    // const parmurl = useParams()
    const [boardButton, addBoard] = useState([])
    const [player, playernow] = useState([])
    const [game,addGame]=useState([])

    const location = useLocation()
    // debugger
    const navigate = useNavigate();
    const getGame = () => {
        axios({
            method: "GET",
            url: "http://10.0.0.5:8000/getGame"
        })
            .then((response) => {
                console.log('response')
                console.log(response.data)
                debugger
                addGame(response.data)
            }).catch((error) => {
                if (error.response) {
                    console.log(error.response)
                    console.log(error.response.status)
                    console.log(error.response.headers)
                }
            })
    }

    const sendRequest = () => {
        axios({
            method: "GET",
            url: "http://10.0.0.5:8000/getBoard"
        })
            .then((response) => {
                console.log('response')
                console.log(response.data)
                debugger
                addBoard(response.data)
            }).catch((error) => {
                if (error.response) {
                    console.log(error.response)
                    console.log(error.response.status)
                    console.log(error.response.headers)
                }
            })
    }
    const clickButton = (data) => {
        axios({
            method: "POST",
            url: "http://10.0.0.5:8000/clickButton",
            data: data
        })
            .then((response) => {
                console.log('response')
                console.log(response.data)
                debugger
                addBoard(response.data)
            }).catch((error) => {
                if (error.response) {
                    console.log(error.response)
                    console.log(error.response.status)
                    console.log(error.response.headers)
                }
            })
    }
    const nextPlayer = () => {
        axios({
            method: "GET",
            url: "http://10.0.0.5:8000/nextPleyer"
        })
            .then((response) => {
                console.log(response.data)
                debugger
            }).catch((error) => {
                if (error.response) {
                    console.log(error.response)
                    console.log(error.response.status)
                    console.log(error.response.headers)
                }
            })
    }

    const Give_Clue = (values) => {
        axios({
            method: "POST",
            url: "http://10.0.0.5:8000/giveClue",
            data:{word:values,player:location.state}
        })
            .then((response) => {
                console.log(response.data)
                debugger
                if (response.data == "False") {
                    alert("שחקן מחשב שיחק עכשיו");
                    nextPlayer()
                


                }
                else {
                    alert("שחקן רגיל משחק עכשיו")
                    playernow(response.data)
                }
            }).catch((error) => {
                if (error.response) {
                    console.log(error.response)
                    console.log(error.response.status)
                    console.log(error.response.headers)
                }
            })
    }
    const myFormik = useFormik({
        initialValues: {
            word: "",
            num: 0
        },
        onSubmit: Give_Clue
    })
    // ביוזאפקט מכניסה לסטייט
    //  useEffect((values) => {
    //     const interval = setInterval(() => {
    //         // const navigate = useNavigate();
    //         getPlayers(values);

    //     }, 2000);
    //     return () => clearInterval(interval);
    // }, []);
    console.log(player)
    console.log(game)

    return (
        <div>
            <div><button onClick={getGame}>game</button></div>
            

            <div> <p>id: {location.state["id"]}</p></div>
            <div> <p>role: {location.state["role"]}</p></div>
            <div> <p>name: {location.state["name"]}</p></div>
            <div> <p>color: {location.state["color"]}</p></div>
            <div><p>player now:{player.name}</p></div>
            <div><p>player now:{game.playernow}</p></div>

            {location.state["role"] == 'multi-spy' ?
                <form onSubmit={myFormik.handleSubmit} >
                    <div className="form-group">
                        <label>word</label>
                        <input className="form-control" onChange={myFormik.handleChange} id="word" name="word"></input>
                    </div>
                    <div className="form-group">
                        <label>num</label>
                        <input className="form-control" onChange={myFormik.handleChange} id="num" name="num"></input>
                    </div>

                    <button className="btn btn-primary" type="submit">give clue</button>

                </form> :<p></p>}


            <div><button onClick={sendRequest}>board</button></div>
            <div><button onClick={nextPlayer}>next player</button></div>

            {/* <p>{roleid}</p> */}
            <div className="grid-container">{boardButton.map((item) => <button className="grid-item" >{item.word}</button>)}</div>
            {/* onDoubleClick={clickButton("item.word")} */}
        </div>
    )


}
