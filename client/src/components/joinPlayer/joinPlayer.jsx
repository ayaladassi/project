import { useState } from 'react'
import { useFormik } from 'formik'
import axios from "axios";
import { useNavigate } from 'react-router-dom'
import * as React from 'react';

export default function Index() {
    const options = [
        { value: 'admin' },
        { value: 'spy' },
    ];
    const navigate = useNavigate();
    const sendData = (values) => {
        debugger
        console.log(values)
         debugger
        axios({
            method: "POST",
            url: "http://10.0.0.5:8000/JoinGame",
            data: values
        })
            .then((response) => {
                console.log(response.data)
                 debugger
                //alert(response.data)
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
            role: "spy",
            name: ""
        },
        onSubmit: sendData
    })

    const [player, setPlayer] = useState();

    return (
        <form onSubmit={myFormik.handleSubmit}>
            <h1>join game</h1>
            <div className="form-group">
                <label>name</label>
                <input className="form-control" onChange={myFormik.handleChange} id="name" name="name"></input>
            </div>
            <div className="form-group col">
                <label htmlFor="neighborhoods">your role</label>
                <select className="form-control" onChange={myFormik.handleChange} required name="role" id="role">
                    {options.map(item => {
                        return (<option value={item.value}>{item.value}</option>);
                    })}
                </select>
            </div>
            <div className="form-group">
                <label>guid</label>
                <input className="form-control" onChange={myFormik.handleChange} id="guid" name="guid"></input>
            </div>
            <br />
            <button className="btn btn-primary" type="submit">צור משחק</button>
        </form>

    )
}





