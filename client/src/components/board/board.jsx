import { useState } from 'react'
import { useFormik } from 'formik'
import axios from "axios";
import { useNavigate, useParams } from 'react-router-dom'
import * as React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './board.css'
export default function board() {
    // useState[roleid,role]
    const parmurl=useParams()
    const [boardButton,addBoard]=useState([])

  const  sendRequest=()=>{
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
    const  clickButton=(value)=>{
        axios({
            method: "POST",
            url: "http://10.0.0.5:8000/clickButton",
            data:value
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
    // ביוזאפקט מכניסה לסטייט
    //  useEffect((values) => {
    //     const interval = setInterval(() => {
    //         // const navigate = useNavigate();
    //         getPlayers(values);

    //     }, 2000);
    //     return () => clearInterval(interval);
    // }, []);
    
    return(
        <div> 
        <button className="btn btn-primary" onClick={sendRequest}>board</button>
        {/* <p>{roleid}</p> */}
        {boardButton.map((item) =><button onClick={clickButton(item.word)}>{item.word}</button> )}
        </div>
    )


}
