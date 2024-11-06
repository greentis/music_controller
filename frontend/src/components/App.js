import React, { Component } from "react";
import { render } from "react-dom";

function Test() {
    return (
        <div>
            <h1>Test</h1>
        </div>
    )
}

export default function App(){
    return (
        <Test/>
    )
}

const appDiv = document.getElementById("app");
render(<App/>, appDiv);