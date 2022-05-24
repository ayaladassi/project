import playerService from "../services/playerService";
import { useRef } from "react";
// import * as Yup from 'yup'
import { useState } from 'react'
import { useFormik } from 'formik'
import axios from "axios";
import { useNavigate } from 'react-router-dom'
import * as React from 'react';
import './index.css'

export default function Index() {
    const options = [
        { value: 'multi-spy' },
        { value: 'spy' },
    ];
    const optionsColor = [
        { value: 'red' },
        { value: 'blue' },
    ];

    // const sendData=(object)=>{
    //     // let name=refInpName.current.value
    //     <navigate></navigate>
    //    let res =await playerService.addPalyerForGame(object);
    // }
    const navigate = useNavigate();
    const sendData = (values) => {
        debugger
        console.log(values)
         debugger
        axios({
            method: "POST",
            url: "http://192.168.49.42:8000/createGame",
            data: values
        })
            .then((response) => {
                console.log(response.data)
                //  debugger
                alert(response.data)
                navigate('../players', { state: { data: response.data } })
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
            guid: "",
            id: "",
            role: "multi-spy",
            name: "",
            color:"red"
        },
        onSubmit: sendData
    })

    const [player, setPlayer] = useState();

    return (
        <form onSubmit={myFormik.handleSubmit}>
            <h1>Create Game</h1>
            <div className="form-group">
                <label>Name</label>
                <input className="form-control" onChange={myFormik.handleChange} id="name" name="name"></input>
            </div>
            <div className="form-group col">
                <label htmlFor="neighborhoods">Role</label>
                <select className="form-control" onChange={myFormik.handleChange} required name="role" id="role">
                    {options.map(item => {
                        return (<option value={item.value}>{item.value}</option>);
                    })}
                </select>
            </div>
            <div className="form-group col">
                <label htmlFor="neighborhoods">Group Color</label>
                <select className="form-control" onChange={myFormik.handleChange} required name="color" id="color">
                    {optionsColor.map(item => {
                        return (<option value={item.value}>{item.value}</option>);
                    })}
                </select>
            </div>
            {/* <div className="form-group">
                <label>תואר</label>
                <input className="form-control" onChange={myFormik.handleChange} id="role" name="role"></input>
            </div> */}
            <br />
            <button className="btn btn-primary" type="submit">צור משחק</button>
        </form>

    )
}





