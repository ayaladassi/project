import axios from "axios"

class PlayerService {

    addPalyerForGame(player) {

        return axios({
            method: "POST",
            url: "http://192.168.49.42:8000/createGame",
            data: player
        })
            .then((response) => {
                const res = response.data
                alert(res)
            }).catch((error) => {
                if (error.response) {
                    console.log(error.response)
                    console.log(error.response.status)
                    console.log(error.response.headers)
                }
            })
    }
    createGame = () => {
        return axios.get('http://192.168.49.42:8000/createGame')
    }
}

export default new PlayerService

