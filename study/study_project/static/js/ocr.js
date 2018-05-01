Tesseract.recognize("../static/image/DEEPS_logo_color.png").then(function(result){
    const a = document.querySelector("#test1");
    a.innerHTML = result.html;
})
Tesseract.recognize("../static/image/back.png").then(function(result){
    const a = document.querySelector("#test2");
    a.innerHTML = result.html;
})
Tesseract.recognize("../static/image/sample_en.png").then(function(result){
    const a = document.querySelector("#test3");
    a.innerHTML = result.html;
})
Tesseract.recognize("../static/image/sample_jpn.png",{lang:"jpn"}).then(function(result){
    const a = document.querySelector("#test4");
    a.innerHTML = result.html;
})
Tesseract.recognize("../static/image/SPC-CB.png",{lang:"jpn"}).then(function(result){
    const a = document.querySelector("#test5");
    a.innerHTML = result.html;
})
