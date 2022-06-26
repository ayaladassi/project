import { useState ,useEffect} from 'react'
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
    const [player, playernow] = useState([])
    const [game, addGame] = useState([])
    const[wordcClue,addwordClue]=useState([])
    const [gameStatus, addGameStatus] = useState([])
    
    const [boardButton, addBoard] = useState([])
    const [message,setMessage]=useState('');
    const [playerNow,setplayerNow]=useState([]);
    const [word_Clue,setword_Clue]=useState([]);
    const [score_red,setscore_red]=useState();
    const [score_blue,setscore_blue]=useState();
    const [listPlayer,setListPlayer]=useState([]);




    




    const location = useLocation()
    // debugger
    const navigate = useNavigate();
    const getGame = () => {
        axios({
            method: "GET",
            url: "http://192.168.49.42:8000/getGame"
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
            url: "http://192.168.49.42:8000/getBoard"
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
    const getGameStatus = () => {
        axios({
            method: "GET",
            url: "http://192.168.49.42:8000/getGameStatus"
        })
            .then((response) => {
                const statusGame=response.data;
                addBoard(statusGame.listBoard);
                setMessage(statusGame.messages?statusGame.messages[statusGame.messages.length-1]:'');
                setplayerNow(statusGame.playerNow)
                setscore_red(statusGame.score_red)
                setword_Clue(statusGame.word_Clue)
                setscore_blue(statusGame.score_blue)
                setListPlayer(statusGame.queue);
              
                console.log(response.data)
                 addGameStatus(response.data)
            }).catch((error) => {
                if (error.response) {
                    console.log(error.response)
                    console.log(error.response.status)
                    console.log(error.response.headers)
                }
            })
    }
    const clickButton = (wordClue,index) => {
        const button=boardButton[index];
        button.status=true;
        boardButton[index]={...button};
        addBoard([...boardButton]);
        axios({
            method: "POST",
            url: "http://192.168.49.42:8000/clickButton",
            data:{word:wordClue,player: location.state} 
        })
            .then((response) => {
                console.log('response')
                console.log(response.data)
                if(response.data=="False"){
                    alert(" הבא: התור אינו שלך נא לחכות בסבלנות");
                }
                
            }).catch((error) => {
                if (error.response) {
                    console.log(error.response)
                    console.log(error.response.status)
                    console.log(error.response.headers)
                }
            })
    }
    const nextPlayer = async () => {
        axios({
            method: "POST",
            url: "http://192.168.49.42:8000/nextPleyer",
            data:{player: location.state}
        })
            .then(async (response) => {
                console.log(response.data)
                if (response.data == "True") {
                    // alert("  לוח נצבע כי שחקן מחשב שיחק עכשיו");
                    await new Promise(r => setTimeout(r, 2000));
                    nextPlayer()
                }
                if(response.data=="False"){
                    alert(" הבא: התור אינו שלך נא לחכות בסבלנות");
                }
                // else{
                // // alert( "word clue "+ response.data["word"])
                // debugger
                // addwordClue(response.data)}
            }).catch((error) => {
                if (error.response) {
                    console.log(error.response)
                    console.log(error.response.status)
                    console.log(error.response.headers)
                }
            })
    }

    const Give_Clue = async (values) => {
        axios({
            method: "POST",
            url: "http://192.168.49.42:8000/giveClue",
            data: { word: values, player: location.state }
        })
            .then(async(response) => {
                console.log(response.data)
                debugger
                if (response.data == "True") {
                    alert("  לוח נצבע כי שחקן מחשב שיחק עכשיו");
                    await new Promise(r => setTimeout(r, 2000));
                    nextPlayer()
                }
                if(response.data=="False"){
                    alert("רמז: התור אינו שלך נא לחכות בסבלנות ");
                }
                // if(response.data!="False" && response.data!="True") {
                //     alert("שחקן רגיל משחק עכשיו")
                //     playernow(response.data)
                // }
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
            url: "http://192.168.49.42:8000/nextPleyer",
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
    ///ביוזאפקט מכניסה לסטייט
     useEffect(() => {
        const interval = setInterval(() => {
            getGameStatus();
        }, 2000);
        return () => clearInterval(interval);
    }, []);
 
    const getStatusPlayer=()=>{
        const arrPlayer=[];
        listPlayer.forEach(player => {
            const isPlayerNow=player.id==playerNow.id?true:false;
            arrPlayer.push
            ( <div className="con-p">
                <div className={"con-player "+(isPlayerNow?'player-now':'')}>
                <i className="fa fa-user" aria-hidden="true"></i>
                <p>{player.name}</p>
                </div>
            </div>)
        });
        return arrPlayer
    }

    const getUserPlayer=()=>{
        return <div style={{color:location.state["color"]?location.state["color"]:'black'}} className="palyer-user">
                       <span>{location.state["name"]} | {location.state["role"]}</span>

            <i className="fa fa-user user" aria-hidden="true"></i>
            <div style={{fontWeight:'bold'}}><span style={{color:'blue'}}>{score_blue}</span>&nbsp;<span style={{color:'red'}}>{score_red}</span></div>
        </div>
    }
    const getWordTitle=()=>{
        return <div>  <p>| word clue {word_Clue["word"]} number Clues {word_Clue["number"]}</p></div>
    }
    const getStyleButton=(item)=>{
     const backgroundColor=item.status?item.color:'rgba(255, 255, 255, 0.8)';
     const color=location.state["role"] == 'multi-spy' && !item.status?item.color:'black';
    //  const cursor=location.state["id"] ==playerNow["id"] ?allowed:not-allowed;
     const style= {'color':color,'backgroundColor':backgroundColor};
     return style;
    }
    return (
        <div className="body">



             <div className="tit-msg">{message}</div>


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
                <div><button onClick={nextPlayer}>next player</button></div> 

                <p  className="tit-msg">word clue {word_Clue["word"]} number Clues {word_Clue["number"]}</p></div> : <p></p>}



            <div style={{display:'flex',position:'relative'}}>{getStatusPlayer()}{getUserPlayer()}</div>
            <div className="grid-container">{boardButton.map((item,index) => <button disabled={location.state["id"] == playerNow["id"]  ? false:true}

            style={getStyleButton(item)}
            onClick={()=>{clickButton(item.word,index)}} className="grid-item" >{item.word}</button>)}</div>
             {score_blue==0?navigate('../winner',{ state: "blue" }):""}
             {score_red==0?navigate('../winner',{ state: "red" }):""}
              <div><p></p></div>
              <div><p></p></div>

        </div>
    )


}
