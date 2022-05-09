import playerService from "../services/playerService";
import { useRef } from "react";

export default function Index() {

    // const sendData=(object)=>{
    //     // let name=refInpName.current.value
    //     <navigate></navigate>
    //    let res =await playerService.addPalyerForGame(object);
    // }
    const navigate = useNavigate();
    const sendData = (values) => {
        console.log(values)
        debugger
        axios({
            method: "POST",
            url: "http://192.168.49.42:8000/createGame",
            data: values
        })
            .then((response) => {
                console.log(response.data)
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
                <input  className="form-control" onChange={myFormik.handleChange} id="role" name="role" role="role"></input>
            </div>
            <br />
            <button className="btn btn-primary" type="submit">צור משחק</button>
        </form>
  
    )
  }