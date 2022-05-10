// import playerService from "../services/playerService";
import { useFormik } from 'formik'
import { useEffect } from 'react'
import { useLocation } from 'react-router-dom';
import * as React from 'react';

export default function Index() {

    const state=useLocation()
    useEffect(() => {
        console.log(state);
//   debugger
      },[]);
    
    // let link = PlayerService.createGame();
    return (
        <div>
            <div><a href={"mailto:"+state.state.data['link']}>{state.state.data['link']}</a></div>
           <div> <p>name:</p>{state.state.data['name']}</div>
           <div> <p>role:</p> {state.state.data['role']}</div>
           <div> <p>id:</p>{state.state.data['id']}</div>


            {/* <form onSubmit={myFormik.handleSubmit}>
                <h1>שחקנים</h1>

                <button onClick={SetName} className="btn btn-primary" type="submit">צור משחק</button>
            </form> */}
        </div>
    )



};