import { useState } from 'react'
import { useFormik } from 'formik'
import axios from "axios";
import { useNavigate, useParams } from 'react-router-dom'
import * as React from 'react';
export default function board() {
    // useState[roleid,role]
    const parmurl=useParams()

  const  sendRequest=()=>{
        axios({
            method: "POST",
            url: "http://192.168.49.42:8000/getBoard"
        })
            .then((response) => {
                console.log('response')
                console.log(response.data)
               
                
            
              
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
        <button onClick={sendRequest}>gfffffffffffff</button>
        {/* <p>{roleid}</p> */}
        </div>
    )


}
