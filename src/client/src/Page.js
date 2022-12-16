import "./page.css";
import axios from "axios";
import upload from "./upload.svg";
import {useState} from "react";

export default function Page(props) {
    const [state, setState] = useState("drop");
    const [abstract, setAbstract] = useState("");

    function postFile(event) {
        event.preventDefault();
        const file = event.target.files[0];
        const formData = new FormData();
        formData.append('file', file, {contentType: 'application/pdf'});
        console.log("post", formData);
        axios.post('http://localhost:8000/apiv1/predict', formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }).then((response) => {
            setAbstract(response.data.Abstract);
            setState("result");
        }).catch((error) => {console.log(error); setState("drop"); alert("Error: " + error)});
        setState("loading");
    }

    function drawState() {
        if (state === "drop") {
            return (
                <div className="content" onDrop={postFile}>
                    <img src={upload} style={{height: "15vh"}} alt="upload icon" id="upload-icon" />
                    <h3>Drag and drop your pdf here</h3>
                    <input type="file" id="file-input" onChange={postFile}/>
                </div>
            );
        }
        else if (state === "loading") {
            return (
                <div className="content">
                    <h2>Processing...</h2>
                </div>
            );
        }
        else {
            return (
                <div >
                    <h3>Abstract</h3>
                    <br/>
                    <p style={{color: "ghostwhite"}}>{abstract}</p>
                </div>
            )

        }
    }

    return (
        <div style={{backgroundColor:"#282c34", minHeight: "100vh"}}>
            <div id="topbar" >
                <h2>IR Front End</h2>
                {(state === "result") ? <button onClick={() => setState("drop")}>Back</button> : null}
            </div>
            {drawState()}
        </div>
    )
}
