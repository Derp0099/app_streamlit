import streamlit as st
from streamlit.components.v1 import html

st.title("Permainan Ular")

# Full HTML/CSS/JS embedded as a single string. This is a self-contained webpage.
html_code = r'''<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Snake - Nokia Style</title>
  <style>
    :root{--bg:#0b1220;--panel:#071426;--accent:#16a085;--muted:#9aa5b1}
    html,body{height:100%;margin:0;background:linear-gradient(180deg,var(--bg),#071426);font-family:Inter,Roboto,Arial}
    .wrap{display:flex;flex-direction:column;align-items:center;gap:12px;padding:12px}
    .game-card{background:rgba(255,255,255,0.03);border-radius:12px;padding:12px;box-shadow:0 6px 20px rgba(2,6,23,0.6);width:100%;max-width:520px}
    canvas{display:block;background:#111827;border-radius:8px;width:100%;height:auto}
    .info{display:flex;justify-content:space-between;align-items:center;color:var(--muted);margin-top:8px}
    .controls{display:flex;justify-content:space-around;gap:8px;margin-top:10px}
    .btn{background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.04);padding:8px 12px;border-radius:8px;color:white}
    .hud{display:flex;gap:8px}
    .big{font-weight:700;color:var(--accent)}
    /* on-screen directional pad for mobile */
    .dpad{width:220px;margin:10px auto;display:grid;grid-template-columns:64px 64px 64px;grid-template-rows:64px 64px;gap:6px;justify-content:center}
    .dpad button{width:64px;height:64px;border-radius:8px;border:none;background:rgba(255,255,255,0.04);font-size:20px}
    .dpad .up{grid-column:2/3;grid-row:1/2}
    .dpad .left{grid-column:1/2;grid-row:2/3}
    .dpad .right{grid-column:3/4;grid-row:2/3}
    .dpad .down{grid-column:2/3;grid-row:2/3}
    .small{font-size:12px;color:var(--muted)}
    @media(min-width:700px){.dpad{display:none}}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="game-card">
      <canvas id="game" width="420" height="420"></canvas>
      <div class="info">
        <div class="hud">Score: <span id="score" class="big">0</span></div>
        <div class="small">Level: <span id="level">1</span></div>
      </div>
      <div class="controls">
        <button id="startBtn" class="btn">Start / Restart</button>
        <button id="pauseBtn" class="btn">Pause</button>
        <button id="speedBtn" class="btn">Speed</button>
      </div>
      <div style="text-align:center;margin-top:8px;color:var(--muted);font-size:13px">Gunakan tombol panah atau swipe di HP.</div>
      <div class="dpad" id="dpad">
        <button class="up">↑</button>
        <button class="left">←</button>
        <button class="right">→</button>
        <button class="down">↓</button>
      </div>
    </div>
    <div style="max-width:520px;color:var(--muted);font-size:13px;text-align:center">Klasik — Ular tumbuh setiap kali memakan buah. Jika menabrak dinding atau tubuh sendiri, permainan berakhir.</div>
  </div>

<script>
(() => {
  const canvas = document.getElementById('game');
  const ctx = canvas.getContext('2d');
  const scoreEl = document.getElementById('score');
  const levelEl = document.getElementById('level');
  const startBtn = document.getElementById('startBtn');
  const pauseBtn = document.getElementById('pauseBtn');
  const speedBtn = document.getElementById('speedBtn');
  const dpad = document.getElementById('dpad');

  const gridSize = 20; // ukuran kotak
  const cols = Math.floor(canvas.width / gridSize);
  const rows = Math.floor(canvas.height / gridSize);

  let snake = [{x: Math.floor(cols/2), y: Math.floor(rows/2)}];
  let dir = {x:1,y:0};
  let food = null;
  let score = 0;
  let level = 1;
  let running = false;
  let speed = 7; // langkah per detik
  let lastFrame = 0;

  function reset(){
    snake = [{x: Math.floor(cols/2), y: Math.floor(rows/2)}];
    dir = {x:1,y:0};
    placeFood();
    score = 0; level = 1; speed = 7;
    running = true;
    updateHUD();
  }

  function placeFood(){
    while(true){
      const x = Math.floor(Math.random()*cols);
      const y = Math.floor(Math.random()*rows);
      if(!snake.some(s => s.x===x && s.y===y)){
        food = {x,y}; break;
      }
    }
  }

  function updateHUD(){
    scoreEl.textContent = score;
    levelEl.textContent = level;
  }

  function gameOver(){
    running = false;
    alert('Game Over! Skor: ' + score);
  }

  function step(){
    const head = {x: snake[0].x + dir.x, y: snake[0].y + dir.y};
    // wall collision (classic Nokia wraps? We'll make walls kill)
    if(head.x < 0 || head.x >= cols || head.y < 0 || head.y >= rows){
      return gameOver();
    }
    // self collision
    if(snake.some(s => s.x===head.x && s.y===head.y)) return gameOver();
    snake.unshift(head);
    // eat food
    if(food && head.x===food.x && head.y===food.y){
      score += 10;
      if(score % 50 === 0){ level++; speed += 1; }
      placeFood();
      updateHUD();
    } else {
      snake.pop();
    }
  }

  function draw(){
    // clear
    ctx.fillStyle = '#071426';
    ctx.fillRect(0,0,canvas.width,canvas.height);

    // draw grid (subtle)
    ctx.strokeStyle = 'rgba(255,255,255,0.02)';
    for(let x=0;x<=canvas.width;x+=gridSize){ ctx.beginPath(); ctx.moveTo(x,0); ctx.lineTo(x,canvas.height); ctx.stroke(); }
    for(let y=0;y<=canvas.height;y+=gridSize){ ctx.beginPath(); ctx.moveTo(0,y); ctx.lineTo(canvas.width,y); ctx.stroke(); }

    // draw food
    if(food){
      drawCell(food.x, food.y, '#e74c3c');
      // small shine
      ctx.fillStyle = 'rgba(255,255,255,0.12)';
      ctx.fillRect(food.x*gridSize + gridSize*0.2, food.y*gridSize + gridSize*0.15, gridSize*0.25, gridSize*0.25);
    }

    // draw snake
    snake.forEach((s,i)=>{
      const shade = i===0 ? '#16a085' : '#0fb07a';
      drawCell(s.x, s.y, shade);
    });
  }

  function drawCell(cx, cy, color){
    ctx.fillStyle = color;
    ctx.fillRect(cx*gridSize + 1, cy*gridSize + 1, gridSize-2, gridSize-2);
  }

  function loop(ts){
    if(!lastFrame) lastFrame = ts;
    const elapsed = ts - lastFrame;
    const msPerStep = 1000 / speed;
    if(running && elapsed >= msPerStep){
      step();
      draw();
      lastFrame = ts;
    }
    requestAnimationFrame(loop);
  }

  // keyboard controls
  window.addEventListener('keydown', e => {
    if(!running) return;
    if(e.key === 'ArrowUp') tryChangeDir(0,-1);
    if(e.key === 'ArrowDown') tryChangeDir(0,1);
    if(e.key === 'ArrowLeft') tryChangeDir(-1,0);
    if(e.key === 'ArrowRight') tryChangeDir(1,0);
  });

  function tryChangeDir(x,y){
    // prevent reversing
    if(snake.length>1 && snake[0].x + x === snake[1].x && snake[0].y + y === snake[1].y) return;
    dir = {x,y};
  }

  // buttons
  startBtn.addEventListener('click', ()=>{ reset(); draw(); });
  pauseBtn.addEventListener('click', ()=>{ running = !running; pauseBtn.textContent = running ? 'Pause' : 'Resume'; });
  speedBtn.addEventListener('click', ()=>{ speed = Math.min(20, speed+1); speedBtn.textContent = 'Speed: ' + speed; });

  // dpad buttons for mobile
  dpad.addEventListener('click', e => {
    const t = e.target;
    if(t.classList.contains('up')) tryChangeDir(0,-1);
    if(t.classList.contains('down')) tryChangeDir(0,1);
    if(t.classList.contains('left')) tryChangeDir(-1,0);
    if(t.classList.contains('right')) tryChangeDir(1,0);
  });

  // touch swipe detection
  let touchStart = null;
  canvas.addEventListener('touchstart', (e)=>{ const t = e.touches[0]; touchStart = {x:t.clientX, y:t.clientY}; });
  canvas.addEventListener('touchend', (e)=>{
    if(!touchStart) return;
    const t = e.changedTouches[0];
    const dx = t.clientX - touchStart.x; const dy = t.clientY - touchStart.y;
    const absx = Math.abs(dx); const absy = Math.abs(dy);
    if(Math.max(absx,absy) < 20) { touchStart = null; return; }
    if(absx > absy){ if(dx>0) tryChangeDir(1,0); else tryChangeDir(-1,0); }
    else { if(dy>0) tryChangeDir(0,1); else tryChangeDir(0,-1); }
    touchStart = null;
  });

  // initial setup
  reset();
  draw();
  requestAnimationFrame(loop);

})();
</script>
</body>
</html>
'''

# Render the HTML inside Streamlit using components.html
# Height: set to 720 so the canvas and controls fit comfortably on desktop and mobile.
html(html_code, height=720, scrolling=True)

st.markdown('---')

