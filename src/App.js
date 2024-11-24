import React, { useEffect } from "react";
import axios from "axios";

const App = () => {
    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/test/")
            .then(response => console.log(response.data))
            .catch(error => console.error(error));
    }, []);

    return <div>Hello, RoomMate!</div>;
};

export default App;
