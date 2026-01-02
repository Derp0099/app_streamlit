import streamlit as st
import random
import time
from streamlit.components.v1 import html

# Set page config
st.set_page_config(
    page_title="Game Collection",
    page_icon="🎮",
    layout="centered"
)

def main_menu():
    st.title("🎮 Koleksi Game")
    st.write("Pilih game yang ingin dimainkan:")
    
    # Create navigation using radio buttons
    game_choice = st.sidebar.radio(
        "Menu Utama",
        ["Beranda", "Escape Room", "Ular", "Gunting Batu Kertas", "Tic Tac Toe"]
    )
    
    if game_choice == "Beranda":
        show_home()
    elif game_choice == "Escape Room":
        escape_room()
    elif game_choice == "Ular":
        snake_game()
    elif game_choice == "Gunting Batu Kertas":
        suit_game()
    elif game_choice == "Tic Tac Toe":
        tic_tac_toe()

def show_home():
    st.header("Selamat Datang di Koleksi Game")
    st.write("""
    Ini adalah kumpulan game sederhana yang dibuat dengan Streamlit.
    Gunakan menu di sebelah kiri untuk memilih game yang ingin dimainkan.
    
    Daftar game yang tersedia:
    - 🗝️ Escape Room: Pecahkan teka-teki untuk keluar dari ruangan
    - 🐍 Ular: Game klasik ular dengan kontrol yang mudah
    - ✊✋✌️ Gunting Batu Kertas: Mainkan melawan komputer atau teman
    - ❌⭕ Tic Tac Toe: Mainkan Tic Tac Toe melawan AI
    """)
    st.image("https://img.freepik.com/free-vector/game-controller-icon-set_107173-233.jpg", 
             width=400, caption="Selamat Bermain!")

def escape_room():
    st.set_page_config(page_title="Escape Room", page_icon="🗝️")
    st.title("🗝️ Escape Room - Petualangan Misterius")
    st.write("Pecahkan teka-teki untuk keluar dari ruangan!")

    # Initialize state
    if "stage" not in st.session_state:
        st.session_state.stage = 1
    if "inventory" not in st.session_state:
        st.session_state.inventory = []
    if "message" not in st.session_state:
        st.session_state.message = ""

    st.subheader(f"Stage {st.session_state.stage}")
    if st.session_state.message:
        st.info(st.session_state.message)

    # Stage 1: Ruangan Awal
    if st.session_state.stage == 1:
        st.write("Kamu terbangun di sebuah ruangan yang asing. Ada **meja kayu**, **lemari tua**, dan **pintu terkunci**.")
        
        choice = st.radio(
            "Apa yang ingin kamu periksa?",
            ["Meja kayu", "Lemari tua", "Pintu terkunci"]
        )

        if st.button("Periksa"):
            if choice == "Meja kayu":
                if "kertas" not in st.session_state.inventory:
                    st.session_state.message = "Kamu menemukan selembar kertas bertuliskan '3-1-4' di bawah meja!"
                    st.session_state.inventory.append("kertas")
                else:
                    st.session_state.message = "Tidak ada yang menarik di meja."
            
            elif choice == "Lemari tua":
                if "baterai" not in st.session_state.inventory:
                    st.session_state.message = "Kamu menemukan senter dan baterai di dalam lemari!"
                    st.session_state.inventory.extend(["senter", "baterai"])
                else:
                    st.session_state.message = "Lemari sudah kosong."
            
            elif choice == "Pintu terkunci":
                if "kunci" in st.session_state.inventory:
                    st.session_state.message = "Kamu menggunakan kunci untuk membuka pintu..."
                    st.session_state.stage = 2
                else:
                    st.session_state.message = "Pintu terkunci. Mungkin ada kunci di sekitar sini."

        # Special action when player has both senter and baterai
        if "senter" in st.session_state.inventory and "baterai" in st.session_state.inventory:
            if st.button("🎮 Pasang baterai ke senter"):
                st.session_state.message = "Senter menyala! Kamu melihat sesuatu berkilat di bawah karpet."
                if "kunci" not in st.session_state.inventory:
                    st.session_state.inventory.append("kunci")
                    st.session_state.inventory.remove("senter")
                    st.session_state.inventory.remove("baterai")

    # Stage 2: Ruangan Kedua
    elif st.session_state.stage == 2:
        st.write("Kamu masuk ke ruangan yang lebih terang. Ada **brankas**, **lukisan**, dan **buku catatan** di meja.")
        
        choice = st.radio(
            "Apa yang ingin kamu lakukan?",
            ["Periksa brankas", "Lihat lukisan", "Baca buku catatan"]
        )

        if st.button("Lakukan"):
            if choice == "Periksa brankas":
                st.session_state.message = "Brankas membutuhkan kode 3 digit."
            
            elif choice == "Lihat lukisan":
                st.session_state.message = "Lukisan menunjukkan pemandangan gunung dengan matahari terbit di belakangnya."
            
            elif choice == "Baca buku catatan":
                st.session_state.message = "Tertulis: 'Angka favoritku adalah hasil dari 300 + 14'"

        # Brankas interaction
        if choice == "Periksa brankas":
            code = st.text_input("Masukkan kode brankas (3 digit):", max_chars=3)
            if st.button("Buka Brankas"):
                if code == "314":
                    st.session_state.inventory.append("kartu akses")
                    st.session_state.message = "Brankas terbuka! Kamu menemukan kartu akses."
                else:
                    st.session_state.message = "Kode salah! Coba lagi."

        # Proceed to next stage
        if "kartu akses" in st.session_state.inventory:
            if st.button("Gunakan kartu akses di pintu"):
                st.session_state.stage = 3
                st.session_state.message = "Pintu elektronik terbuka!"

    # Stage 3: Ruangan Terakhir
    elif st.session_state.stage == 3:
        st.write("Ini adalah ruangan terakhir! Ada **komputer** dan **pintu keluar** dengan pemindai sidik jari.")
        
        if "sidik jari" not in st.session_state.inventory:
            st.write("Komputer menampilkan pesan: 'Verifikasi identitas diperlukan'")
            
            password = st.text_input("Masukkan kata sandi (petunjuk: lihat catatan sebelumnya):", type="password")
            
            if st.button("Login"):
                if password == "314":
                    st.session_state.inventory.append("sidik jari")
                    st.session_state.message = "Verifikasi berhasil! Sidik jari tercetak di kartu akses."
                else:
                    st.session_state.message = "Akses ditolak. Kata sandi salah."
        else:
            st.success("Verifikasi identitas berhasil!")

        if "sidik jari" in st.session_state.inventory:
            if st.button("Tempelkan jari di pemindai"):
                st.session_state.stage = 4
                st.balloons()

    # Stage 4: Akhir Permainan
    elif st.session_state.stage == 4:
        st.balloons()
        st.success("""
        # 🎉 Selamat! 🎉
        
        Kamu berhasil keluar dari ruangan misterius!
        
        ### Item yang berhasil dikumpulkan:
        """ + "\n".join(f"- {item}" for item in st.session_state.inventory))
        
        if st.button("🔄 Main Lagi"):
            st.session_state.stage = 1
            st.session_state.inventory = []
            st.session_state.message = ""
            st.rerun()

    # Display Inventory
    st.markdown("---")
    st.subheader("🎒 Inventory Kamu")
    if st.session_state.inventory:
        for item in st.session_state.inventory:
            st.write(f"- {item}")
    else:
        st.write("Kosong")

    # Add some CSS for better appearance
    st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        margin: 0.5rem 0;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)
def snake_game():
    st.title("🐍 Permainan Ular")
    
    # Snake game HTML/JS code
    html_code = '''
    <!doctype html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Snake Game</title>
        <style>
            canvas {
                background: #000;
                display: block;
                margin: 0 auto;
            }
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: #f0f0f0;
            }
        </style>
    </head>
    <body>
        <canvas id="game" width="400" height="400"></canvas>
        <script>
            const canvas = document.getElementById('game');
            const ctx = canvas.getContext('2d');
            const gridSize = 20;
            const tileCount = canvas.width / gridSize;
            
            let snake = [{x: 10, y: 10}];
            let food = {x: 15, y: 15};
            let dx = 0;
            let dy = 0;
            let score = 0;
            let gameSpeed = 100;
            let gameLoop;
            
            function drawGame() {
                // Clear canvas
                ctx.fillStyle = 'black';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                
                // Draw snake
                ctx.fillStyle = 'lime';
                snake.forEach(segment => {
                    ctx.fillRect(segment.x * gridSize, segment.y * gridSize, gridSize-2, gridSize-2);
                });
                
                // Draw food
                ctx.fillStyle = 'red';
                ctx.fillRect(food.x * gridSize, food.y * gridSize, gridSize-2, gridSize-2);
                
                // Draw score
                ctx.fillStyle = 'white';
                ctx.font = '20px Arial';
                ctx.fillText('Score: ' + score, 10, 30);
            }
            
            function gameUpdate() {
                // Move snake
                const head = {x: snake[0].x + dx, y: snake[0].y + dy};
                snake.unshift(head);
                
                // Check if snake ate food
                if (head.x === food.x && head.y === food.y) {
                    score += 10;
                    generateFood();
                } else {
                    snake.pop();
                }
                
                // Check collision with walls
                if (head.x < 0 || head.x >= tileCount || head.y < 0 || head.y >= tileCount) {
                    gameOver();
                    return;
                }
                
                // Check collision with self
                for (let i = 1; i < snake.length; i++) {
                    if (head.x === snake[i].x && head.y === snake[i].y) {
                        gameOver();
                        return;
                    }
                }
                
                drawGame();
            }
            
            function generateFood() {
                food = {
                    x: Math.floor(Math.random() * tileCount),
                    y: Math.floor(Math.random() * tileCount)
                };
                
                // Make sure food doesn't spawn on snake
                for (let segment of snake) {
                    if (food.x === segment.x && food.y === segment.y) {
                        generateFood();
                        break;
                    }
                }
            }
            
            function gameOver() {
                clearInterval(gameLoop);
                ctx.fillStyle = 'white';
                ctx.font = '40px Arial';
                ctx.textAlign = 'center';
                ctx.fillText('Game Over!', canvas.width/2, canvas.height/2);
                ctx.font = '20px Arial';
                ctx.fillText('Score: ' + score, canvas.width/2, canvas.height/2 + 40);
                
                // Add restart button
                const button = document.createElement('button');
                button.textContent = 'Main Lagi';
                button.style.margin = '20px auto';
                button.style.display = 'block';
                button.style.padding = '10px 20px';
                button.style.fontSize = '16px';
                button.onclick = function() {
                    document.body.removeChild(button);
                    resetGame();
                };
                document.body.appendChild(button);
            }
            
            function resetGame() {
                snake = [{x: 10, y: 10}];
                dx = 0;
                dy = 0;
                score = 0;
                generateFood();
                gameLoop = setInterval(gameUpdate, gameSpeed);
                drawGame();
            }
            
            // Keyboard controls
            document.addEventListener('keydown', function(e) {
                switch(e.key) {
                    case 'w':
                        if (dy !== 1) { dx = 0; dy = -1; }
                        break;
                    case 's':
                        if (dy !== -1) { dx = 0; dy = 1; }
                        break;
                    case 'a':
                        if (dx !== 1) { dx = -1; dy = 0; }
                        break;
                    case 'd':
                        if (dx !== -1) { dx = 1; dy = 0; }
                        break;
                }
            });
            
            // Touch controls for mobile
            let touchStartX = 0;
            let touchStartY = 0;
            
            document.addEventListener('touchstart', function(e) {
                touchStartX = e.touches[0].clientX;
                touchStartY = e.touches[0].clientY;
            }, false);
            
            document.addEventListener('touchend', function(e) {
                if (!touchStartX || !touchStartY) return;
                
                const touchEndX = e.changedTouches[0].clientX;
                const touchEndY = e.changedTouches[0].clientY;
                
                const diffX = touchStartX - touchEndX;
                const diffY = touchStartY - touchEndY;
                
                // Determine the primary direction of the swipe
                if (Math.abs(diffX) > Math.abs(diffY)) {
                    // Horizontal swipe
                    if (diffX > 0 && dx !== 1) {
                        // Swipe left
                        dx = -1;
                        dy = 0;
                    } else if (diffX < 0 && dx !== -1) {
                        // Swipe right
                        dx = 1;
                        dy = 0;
                    }
                } else {
                    // Vertical swipe
                    if (diffY > 0 && dy !== 1) {
                        // Swipe up
                        dx = 0;
                        dy = -1;
                    } else if (diffY < 0 && dy !== -1) {
                        // Swipe down
                        dx = 0;
                        dy = 1;
                    }
                }
                
                touchStartX = 0;
                touchStartY = 0;
                
                // Prevent scrolling
                e.preventDefault();
            }, false);
            
            // Start the game
            resetGame();
        </script>
    </body>
    </html>
    '''
    
    # Display the game
    html(html_code, height=450)
    
    st.markdown("### Cara Bermain:")
    st.markdown("""
    - Gunakan tombol W A S D pada keyboard untuk menggerakkan ular
    - Makan makanan merah untuk menambah panjang ular dan skor
    - Hindari menabrak dinding dan tubuh ular sendiri
    - Untuk perangkat layar sentuh, gunakan sentuhan untuk mengendalikan arah ular
    """)

def suit_game():
    st.title("✊✋✌️ Gunting Batu Kertas")
    
    # Initialize session state
    if 'player_choice' not in st.session_state:
        st.session_state.player_choice = None
    if 'computer_choice' not in st.session_state:
        st.session_state.computer_choice = None
    if 'result' not in st.session_state:
        st.session_state.result = ""
    if 'score' not in st.session_state:
        st.session_state.score = {"player": 0, "computer": 0, "draw": 0}
    
    # Game mode selection
    mode = st.radio("Pilih Mode:", ["Lawan Komputer", "Dua Pemain"])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Pemain 1" if mode == "Dua Pemain" else "Anda")
        if st.button("✊ Batu", key="batu"):
            play_game("batu", mode)
        if st.button("✋ Kertas", key="kertas"):
            play_game("kertas", mode)
        if st.button("✌️ Gunting", key="gunting"):
            play_game("gunting", mode)
    
    with col2:
        if mode == "Dua Pemain":
            st.subheader("Pemain 2")
            if st.button("✊ Batu", key="batu2"):
                play_game("batu", mode, "player2")
            if st.button("✋ Kertas", key="kertas2"):
                play_game("kertas", mode, "player2")
            if st.button("✌️ Gunting", key="gunting2"):
                play_game("gunting", mode, "player2")
    
    # Display choices and result
    if st.session_state.player_choice is not None:
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Pemain 1" if mode == "Dua Pemain" else "Anda")
            if st.session_state.player_choice == "batu":
                st.markdown("<h1 style='text-align: center;'>✊</h1>", unsafe_allow_html=True)
            elif st.session_state.player_choice == "kertas":
                st.markdown("<h1 style='text-align: center;'>✋</h1>", unsafe_allow_html=True)
            else:
                st.markdown("<h1 style='text-align: center;'>✌️</h1>", unsafe_allow_html=True)
            st.write(st.session_state.player_choice.capitalize())
        
        with col2:
            st.subheader("Komputer" if mode == "Lawan Komputer" else "Pemain 2")
            if st.session_state.computer_choice == "batu":
                st.markdown("<h1 style='text-align: center;'>✊</h1>", unsafe_allow_html=True)
            elif st.session_state.computer_choice == "kertas":
                st.markdown("<h1 style='text-align: center;'>✋</h1>", unsafe_allow_html=True)
            else:
                st.markdown("<h1 style='text-align: center;'>✌️</h1>", unsafe_allow_html=True)
            st.write(st.session_state.computer_choice.capitalize())
        
        # Display result
        result_color = '#4CAF50' if st.session_state.result == 'Menang!' else '#f44336' if st.session_state.result == 'Kalah!' else '#FFC07'
        st.markdown(f"<h2 style='text-align: center; color: {result_color}'>{st.session_state.result}</h2>", unsafe_allow_html=True)
        
        # Display score
        st.markdown("### Skor")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Menang", st.session_state.score["player"])
        with col2:
            st.metric("Kalah", st.session_state.score["computer"])
        with col3:
            st.metric("Seri", st.session_state.score["draw"])
        
        if st.button("Reset Skor"):
            st.session_state.score = {"player": 0, "computer": 0, "draw": 0}
            st.experimental_rerun()
    
    # Game rules
    st.markdown("---")
    st.markdown("### Aturan Permainan")
    st.markdown("""
    - Batu mengalahkan gunting
    - Gunting mengalahkan kertas
    - Kertas mengalahkan batu
    - Pilihan yang sama berarti seri
    """)

def play_game(choice, mode, player="player1"):
    if mode == "Lawan Komputer" or player == "player1":
        st.session_state.player_choice = choice
        
        if mode == "Lawan Komputer":
            # Computer's turn
            choices = ["batu", "kertas", "gunting"]
            st.session_state.computer_choice = random.choice(choices)
            
            # Determine the winner
            if st.session_state.player_choice == st.session_state.computer_choice:
                st.session_state.result = "Seri!"
                st.session_state.score["draw"] += 1
            elif (
                (st.session_state.player_choice == "batu" and st.session_state.computer_choice == "gunting") or
                (st.session_state.player_choice == "kertas" and st.session_state.computer_choice == "batu") or
                (st.session_state.player_choice == "gunting" and st.session_state.computer_choice == "kertas")
            ):
                st.session_state.result = "Menang!"
                st.session_state.score["player"] += 1
            else:
                st.session_state.result = "Kalah!"
                st.session_state.score["computer"] += 1
    else:
        # Second player's turn
        st.session_state.computer_choice = choice
        
        # Determine the winner for two players
        if st.session_state.player_choice == st.session_state.computer_choice:
            st.session_state.result = "Seri!"
            st.session_state.score["draw"] += 1
        elif (
            (st.session_state.player_choice == "batu" and st.session_state.computer_choice == "gunting") or
            (st.session_state.player_choice == "kertas" and st.session_state.computer_choice == "batu") or
            (st.session_state.player_choice == "gunting" and st.session_state.computer_choice == "kertas")
        ):
            st.session_state.result = "Pemain 1 Menang!"
            st.session_state.score["player"] += 1
        else:
            st.session_state.result = "Pemain 2 Menang!"
            st.session_state.score["computer"] += 1

def tic_tac_toe():
    st.title("❌⭕ Tic Tac Toe")
    
    # Initialize the board
    if 'board' not in st.session_state:
        st.session_state.board = [''] * 9
    if 'current_player' not in st.session_state:
        st.session_state.current_player = 'X'
    if 'winner' not in st.session_state:
        st.session_state.winner = None
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False
    
    # Game board display
    st.markdown("""
    <style>
    button {
    width: 100% !important;
    aspect-ratio: 1 / 1 !important;
    font-size: 36px !important;
    font-weight: bold !important;
    border-radius: 8px !important;
    }
    .status {
        text-align: center;
        font-size: 24px;
        margin: 20px 0;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    # --- Tampilan papan 3x3 horizontal ---
    for row in range(3):
        cols = st.columns(3)
        for col in range(3):
            i = row * 3 + col
            cols[col].button(
                st.session_state.board[i] or " ",
                key=f'cell_{i}',
                on_click=make_move,
                args=(i,),
                disabled=st.session_state.game_over or st.session_state.board[i] != ''
            )


    
    # Game status
    if st.session_state.winner:
        st.markdown(f'<div class="status">Pemenang: {st.session_state.winner} 🎉</div>', unsafe_allow_html=True)
    elif st.session_state.game_over:
        st.markdown('<div class="status">Permainan Seri! 🤝</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="status">Giliran: {st.session_state.current_player}</div>', unsafe_allow_html=True)
    
    # Restart button
    if st.button('Mulai Ulang', key='restart_button', on_click=reset_game):
        pass  # The button action is handled by the reset_game function
    
    # Game instructions
    st.markdown("### Cara Bermain")
    st.markdown("""
    - Klik pada kotak kosong untuk menempatkan tanda X atau O
    - Pemain pertama menggunakan X, pemain kedua menggunakan O
    - Dapatkan 3 tanda berurutan (vertikal, horizontal, atau diagonal) untuk menang
    - Jika semua kotak terisi dan tidak ada pemenang, permainan berakhir seri
    """)

def make_move(i):
    if st.session_state.board[i] == '' and not st.session_state.winner and not st.session_state.game_over:
        st.session_state.board[i] = st.session_state.current_player
        
        # Check for a winner
        if check_winner(st.session_state.board, st.session_state.current_player):
            st.session_state.winner = st.session_state.current_player
            st.session_state.game_over = True
        # Check for a draw
        elif '' not in st.session_state.board:
            st.session_state.game_over = True
        else:
            # Switch players
            st.session_state.current_player = 'O' if st.session_state.current_player == 'X' else 'X'

def check_winner(board, player):
    # Check rows, columns, and diagonals
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def reset_game():
    st.session_state.board = [''] * 9
    st.session_state.current_player = 'X'
    st.session_state.winner = None
    st.session_state.game_over = False

# Run the app
if __name__ == "__main__":
    main_menu()
