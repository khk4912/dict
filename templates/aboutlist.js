let wordList = [];
const WORD_LS = 'wordlist';
const list = document.querySelector(".list");

/*function delword(event){ // 낱개로 지우기 추가 예정
    const btn = event.target;
    const li = btn.parentNode;
    list.removeChild(li);
    wordList = wordList.splice(li.id);
    localStorage.setItem(WORD_LS, JSON.stringify(wordList));
    alert("단어를 삭제했습니다.")
}*/

function paintList(wtext, mtext){ // 리스트 구성
    const li = document.createElement("li");
    //const delBtn = document.createElement("button");
    const span = document.createElement("span"); 
    //delBtn.innerText = "삭제하기";
    //delBtn.addEventListener("click", delword);
    span.innerText = wtext+mtext
    li.appendChild(span);
    //li.appendChild(delBtn);
    list.appendChild(li);
}

function load_list(){ // 단어 로드
    const loadList = localStorage.getItem(WORD_LS); 
    if (loadList == null) {
        const div = document.createElement("div");
        div.innerText = "추가된 단어가 없습니다.";
        list.appendChild(div);
    }
    else {
        const parseList = JSON.parse(loadList);
        console.log(parseList)
        parseList.forEach(function(array) {
            paintList(array.word, array.mean);
        });
    }     
}

function reset() { // 단어 초기화
    localStorage.removeItem(WORD_LS);
    wordList = [];
    alert("리셋 완료!")
    location.reload(true)
}

function init() {
    load_list();
}

init();