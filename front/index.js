let display = document.getElementById('display');


let flag = true;
let shouldClean = true;

doCalc = (body) => {

    const ob = {
        "expression": body
    };

    shouldClean = true;


    fetch("http://localhost:8000/solver/", {
        method: "post",

        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(ob)
    })
        .then(res => res.json())
        .then(res => {
            console.log(res["expression"]);
            display.innerText = res["expression"];

            var theDiv = document.getElementById("list");
            var content = document.createElement("div");
            content.innerHTML = res["expression"];
            theDiv.appendChild(content);
        })

}

getHistory = () => {
    var theDiv = document.getElementById("list");
    fetch("http://localhost:8000/history/", {
        method: "get",

        headers: {
            "Content-Type": "application/json"
        }
    })
        .then(res => res.json())
        .then(res => {
            for (let i = 0; i < res.length; i++) {
                var content = document.createElement("div");
                content.innerHTML = res[i]["expression"];
                theDiv.appendChild(content);
                console.log(res[i]);
            }
        })
}


getHistory();

let buttons = Array.from(document.getElementsByClassName('button'));


buttons.map(button => {
    button.addEventListener('click', (e) => {
        if(shouldClean == true){
            display.innerText = "";
            shouldClean = false;
        }

        switch (e.target.innerText) {
            case 'C':
                display.innerText = '';
                break;
            case '=':
                try {
                    doCalc(display.innerText);
                    //display.innerText = eval(display.innerText);
                } catch {
                    display.innerText = "Error"
                }
                break;
            case '←':
                if (display.innerText) {
                    display.innerText = display.innerText.slice(0, -1);
                }
                break;
            case "History":
                var theDiv = document.getElementById("list");
                flag = !flag;
                if (flag) {
                    theDiv.style.visibility = 'visible';
                } else {
                    theDiv.style.visibility = 'hidden';
                }

                break;
            default:
                display.innerText += e.target.innerText;
        }
    });
});