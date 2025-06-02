import React, { useEffect } from "react";

const STRINGS = [
"트랄라레오 트랄라라라",
"리릴리 라릴라",
"퉁퉁퉁퉁퉁퉁퉁퉁퉁 사후르",
"brrBBrrrrr 파타핌",
"붐바르딜로 크로코딜로",
"라 바카 사투르노 사투르니타",
"프리고 카멜로",
"카푸치노 아사시노",
"침판지니 바나니니",
"보네카 암발라부"
];

function getRandomInt(min, max) {
return Math.floor(Math.random() * (max - min) + min);
}

const App = () => {
useEffect(() => {
const style = document.createElement("style");
style.innerHTML = `
body {
margin: 0;
overflow: hidden;
background: black;
position: relative;
height: 100vh;
}
  .crazy-text {
    position: absolute;
    font-size: 6rem;
    font-weight: bold;
    white-space: nowrap;
    pointer-events: none;
    user-select: none;
    z-index: 9999;
  }

  @keyframes colorChange {
    0%   { color: red; }
    20%  { color: orange; }
    40%  { color: yellow; }
    60%  { color: green; }
    80%  { color: blue; }
    100% { color: violet; }
  }

  @keyframes sizePulse {
    0%, 100% { transform: scale(1); }
    50%      { transform: scale(2); }
  }

  @keyframes rotateCrazy {
    0%   { transform: rotate(0deg); }
    25%  { transform: rotate(90deg); }
    50%  { transform: rotate(180deg); }
    75%  { transform: rotate(270deg); }
    100% { transform: rotate(360deg); }
  }
`;
document.head.appendChild(style);

STRINGS.forEach((text) => {
  const el = document.createElement("div");
  el.className = "crazy-text";
  el.textContent = text;
  el.style.left = getRandomInt(0, window.innerWidth - 300) + "px";
  el.style.top = getRandomInt(0, window.innerHeight - 100) + "px";
  el.style.animation = `
    colorChange ${getRandomInt(1, 4)}s infinite alternate,
    sizePulse ${getRandomInt(1, 4)}s infinite alternate,
    rotateCrazy ${getRandomInt(2, 5)}s infinite linear
  `;
  document.body.appendChild(el);

  let x = getRandomInt(0, window.innerWidth);
  let y = getRandomInt(0, window.innerHeight);
  let dx = (Math.random() - 0.5) * 10;
  let dy = (Math.random() - 0.5) * 10;

  function move() {
    x += dx;
    y += dy;
    if (x < 0 || x > window.innerWidth - el.offsetWidth) dx *= -1;
    if (y < 0 || y > window.innerHeight - el.offsetHeight) dy *= -1;
    el.style.left = x + "px";
    el.style.top = y + "px";
    requestAnimationFrame(move);
  }

  move();
});

return () => {
  const elements = document.querySelectorAll(".crazy-text");
  elements.forEach((el) => el.remove());
  style.remove();
};
}, []);

return <></>;
};

export default App;