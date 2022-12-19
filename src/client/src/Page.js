import "./page.css";
import axios from "axios";
import upload from "./upload.svg";
import {useState} from "react";

export default function Page(props) {
    const [state, setState] = useState("drop");
    const [abstract, setAbstract] = useState("");

    function postFile() {
        const file = document.getElementById("file-input").files[0]
        const index = document.getElementById("summary-value").value
        const formData = new FormData();
        formData.append('file', file, {contentType: 'application/pdf'});
        console.log("post", formData);
        axios.post('http://localhost:8000/apiv1/predict/' + index, formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }).then((response) => {
            setAbstract(response.data.Abstract);
            setState("result");
        }).catch((error) => {console.log(error); setState("drop"); alert("Error: " + error)});
        setState("loading");
    }

    function postJaccard() {
        const file = document.getElementById("file-input").files[0]
        const index = document.getElementById("summary-value").value
        const formData = new FormData();
        formData.append('file', file, {contentType: 'application/pdf'});
        console.log("post", formData);
        axios.post('http://localhost:8000/apiv1/train/' + index, formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }).then((response) => {
            setAbstract(response.data.Jaccard);
            console.log(response.data);
            setState("Jaccard");
        }).catch((error) => {console.log(error); setState("drop"); alert("Error: " + error)});
        setState("loading");
    }

    function drawState() {
        if (state === "drop") {
            return (
                <div className="content" onDrop={postFile}>
                    <img src={upload} style={{height: "15vh"}} alt="upload icon" id="upload-icon" />
                    <h3>Drag and drop your pdf here</h3>
                    <input type="file" id="file-input" />
                    <br/>
                    <label htmlFor="summary-value">Summary amount:</label>
                    <input type="text" name="summary-value" id="summary-value" defaultValue="0.2"/>
                    <br/>
                    <div style={{display: "flex"}}>
                        <button style={{margin: "10px"}} onClick={() => postFile()}>Abstract</button>
                         <button style={{margin: "10px"}} onClick={() => postJaccard()}>Jaccard</button>
                    </div>
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
        else if (state === "Jaccard") {
            return (
                <div className="content">
                    <h2>Jaccard index</h2>
                    <br/>
                    <p style={{color: "ghostwhite", display: 'initial'}}>{abstract}</p>
                </div>
            )
        }
        else {
            return (
                <div style={{position: 'absolute', top: "10vh", left: "10vw", width: "80vw"}}>
                    <h2 style={{color: "ghostwhite"}}>Abstract</h2>
                    <br/>
                    <p style={{color: "ghostwhite", display: 'initial'}}>{abstract}</p>
                </div>
            )

        }
    }

    return (
        <div style={{backgroundColor:"#282c34", minHeight: "100vh"}}>
            <div id="topbar" >
                <h2>Information Retrieval: Paper summarizer</h2>
                {(state === "result" || state === "Jaccard") ? <button onClick={() => setState("drop")}>Back</button> : null}
            </div>
            {drawState()}
        </div>
    )
}
