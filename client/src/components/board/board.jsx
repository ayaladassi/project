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
    const [game, addGame] = useState([])
    const[wordcClue,addwordClue]=useState([])

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
                console.log(player)
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
    const clickButton = (wordClue) => {
        axios({
            method: "POST",
            url: "http://10.0.0.5:8000/clickButton",
            data:{word:wordClue,player: location.state} 
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
            method: "POST",
            url: "http://10.0.0.5:8000/nextPleyer",
            data:{player: location.state}
        })
            .then((response) => {
                console.log(response.data)
                if(response.data=="False"){
                    alert(" הבא: התור אינו שלך נא לחכות בסבלנות");
                }
                else{
                alert( "word clue "+ response.data["word"])
                debugger
                addwordClue(response.data)}
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
            data: { word: values, player: location.state }
        })
            .then((response) => {
                console.log(response.data)
                debugger
                if (response.data == "True") {
                    alert("  לוח נצבע כי שחקן מחשב שיחק עכשיו");
                    nextPlayer()
                }
                if(response.data=="False"){
                    alert("רמז: התור אינו שלך נא לחכות בסבלנות ");
                }
                if(response.data!="False" && response.data!="True") {
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
    const getClue = () => {
        axios({
            method: "GET",
            url: "http://10.0.0.5:8000/nextPleyer",
            data:{player: location.state}
        })
            .then((response) => {
                console.log(response.data)
                alert( "word clue "+ response.data["word"])
                debugger
                // addwordClue(response.data)
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
    // addBoard(game["board"].listBoard)

    return (
        <div className="body">
            <div><button onClick={getGame}>game</button></div>

            <div className="auto"> <p>id: {location.state["id"]}  role: {location.state["role"]}  name: {location.state["name"]}  color: {location.state["color"]}</p>

                <p>player now:{player.name}</p>
                <p>player now:{game["platerNow"]}</p>

            </div>

            {location.state["role"] == 'multi-spy' ?
                <form onSubmit={myFormik.handleSubmit} className="left" >
                    <div className="form-group">
                        <label>word</label>
                        <input className="form-control" onChange={myFormik.handleChange} id="word" name="word"></input>
                        <label>num</label>
                        <input className="form-control" onChange={myFormik.handleChange} id="num" name="num"></input>
                    </div>


                    <button className="btn btn-primary" type="submit">give clue</button>

                </form> : <p></p>}
                {location.state["role"] == 'spy' ?<div>
                <button onClick={getClue}>get Clue</button>;
                <p>word clue {wordcClue["word"]} number Clues {wordcClue["len"]}</p></div> : <p></p>}


            <div><button onClick={sendRequest}>board</button></div>
            <div><button onClick={nextPlayer}>next player</button></div> 
            <div className="lef"><p>score red aaa</p></div>
            <div className="right"><p>score blue</p></div>



            <div className="grid-container">{boardButton.map((item) => <button className="grid-item" >{item.word}</button>)}</div>
             {/* onDoubleClick={clickButton("item.word")} */}
        </div>
    )


}
