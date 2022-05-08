import playerService from "../services/playerService";
import { useRef } from "react";

export default function Index() {

    // const refInpName=useRef();

    const sendData=(object)=>{
        // let name=refInpName.current.value
        <navigate></navigate>
       let res =await playerService.addPalyerForGame(object);
    }
    const myFormik = useFormik({
        playerValues: {
            guid: "",
            id: "",
            role: "",
            name: ""
        },
        onSubmit: sendData
    })

    const [player, setPlayer] = useState();









    
    return (
        <form onSubmit={myFormik.handleSubmit}>
            <h1>יצירת משחק</h1>
            <div className="form-group">
                <label>שם</label>
                <input  className="form-control" onChange={myFormik.handleChange} id="name" name="name"></input>
            </div>
            <div className="form-group">
                <label>תואר</label>
                <input  className="form-control" onChange={myFormik.handleChange} id="role" name=":role" role="role"></input>
            </div>
            <br />
            <button className="btn btn-primary" type="submit">צור משחק</button>
        </form>
  
    )
  }