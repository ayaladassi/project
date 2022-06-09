import { useState } from 'react'
import { useFormik } from 'formik'
import axios from "axios";
import { useNavigate, useParams } from 'react-router-dom'
import * as React from 'react';
export default function board() {
    useState[roleid,role]
    const parmurl=useParams()
    ביוזאפקט מכניסה לסטייט
    useEffect((values) => {
        const interval = setInterval(() => {
            // const navigate = useNavigate();
            getPlayers(values);

        }, 2000);
        return () => clearInterval(interval);
    }, []);
    return(
      <p>{roleid}</p>
    )


}
