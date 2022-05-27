import { useState } from 'react'
import { useFormik } from 'formik'
import axios from "axios";
import { useNavigate } from 'react-router-dom'
import * as React from 'react';
export default function board() {

    useEffect(() => {
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
    return(
        aaaaa
    )
}
