import playerService from "../services/playerService";

export default function Index() {

    let link = PlayerService.createGame();
    return (
        <div>
            <div><a href="mailto:link"></a></div>
            <form onSubmit={myFormik.handleSubmit}>
                <h1>שחקנים</h1>

                <button onClick={SetName} className="btn btn-primary" type="submit">צור משחק</button>
            </form>
        </div>
    )



};