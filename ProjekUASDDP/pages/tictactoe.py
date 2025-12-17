import streamlit as st

st.set_page_config(page_title="Tic Tac Toe", page_icon="❌⭕", layout="centered")


st.markdown("""
<style>
body { background-color: #f5f7fa; }
.board {
    background: white;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}
button {
    height: 90px !important;
    font-size: 36px !important;
    font-weight: bold !important;
    border-radius: 14px !important;
}
.win button {
    background-color: #22c55e !important;
    color: white !important;
}
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
}
.turn {
    text-align: center;
    margin-bottom: 15px;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)


if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.winning_line = []
    st.session_state.celebrate = False
    st.session_state.score_x = 0
    st.session_state.score_o = 0
    st.session_state.score_draw = 0


st.sidebar.title("⚙️ Pengaturan")
player_x = st.sidebar.text_input("Nama Player X", "Player X")
player_o = st.sidebar.text_input("Nama Player O / Bot", "AI Bot")
vs_bot = st.sidebar.checkbox("Lawan Bot 🤖", True)

st.sidebar.markdown("### 📊 Skor")
st.sidebar.metric(f"{player_x} (X)", st.session_state.score_x)
st.sidebar.metric(f"{player_o} (O)", st.session_state.score_o)
st.sidebar.metric("Seri", st.session_state.score_draw)


WIN_LINES = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

def check_winner(board):
    for line in WIN_LINES:
        a,b,c = line
        if board[a] == board[b] == board[c] != "":
            return board[a], list(line)
    if "" not in board:
        return "Draw", []
    return None, []

def minimax(board, is_max):
    result, _ = check_winner(board)
    if result == "O":
        return 1
    if result == "X":
        return -1
    if result == "Draw":
        return 0

    scores = []
    for i in range(9):
        if board[i] == "":
            board[i] = "O" if is_max else "X"
            scores.append(minimax(board, not is_max))
            board[i] = ""
    return max(scores) if is_max else min(scores)

def best_move():
    best_score = -999
    move = None
    for i in range(9):
        if st.session_state.board[i] == "":
            st.session_state.board[i] = "O"
            score = minimax(st.session_state.board, False)
            st.session_state.board[i] = ""
            if score > best_score:
                best_score = score
                move = i
    return move

def make_move(i):
    if st.session_state.board[i] == "" and st.session_state.winner is None:
        
        st.session_state.board[i] = st.session_state.current_player
        w, line = check_winner(st.session_state.board)
        st.session_state.winner = w
        st.session_state.winning_line = line

        
        if w is None:
            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

        
        if (
            vs_bot
            and st.session_state.current_player == "O"
            and st.session_state.winner is None
        ):
            move = best_move()
            if move is not None:
                st.session_state.board[move] = "O"
                w, line = check_winner(st.session_state.board)
                st.session_state.winner = w
                st.session_state.winning_line = line
                if w is None:
                    st.session_state.current_player = "X"



st.markdown('<div class="title">❌⭕ Tic Tac Toe </div>', unsafe_allow_html=True)
turn_name = player_x if st.session_state.current_player == "X" else player_o
st.markdown(f'<div class="turn">Giliran: <b>{turn_name} ({st.session_state.current_player})</b></div>', unsafe_allow_html=True)

st.markdown('<div class="board">', unsafe_allow_html=True)
for r in range(3):
    cols = st.columns(3)
    for c in range(3):
        idx = r * 3 + c
        cls = "win" if idx in st.session_state.winning_line else ""
        with cols[c]:
            st.markdown(f'<div class="{cls}">', unsafe_allow_html=True)
            st.button(st.session_state.board[idx] or " ", key=idx, on_click=make_move, args=(idx,), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)


if st.session_state.winner and not st.session_state.celebrate:
    st.session_state.celebrate = True
    if st.session_state.winner == "Draw":
        st.info("🤝 Permainan Seri!")
        st.session_state.score_draw += 1
    elif st.session_state.winner == "X":
        st.success(f"🎉 {player_x} Menang!")
        st.session_state.score_x += 1
        st.balloons()
        st.toast("Kemenangan diraih! 🎊")
    else:
        st.success(f"🤖 {player_o} Menang!")
        st.session_state.score_o += 1
        st.balloons()
        st.toast("AI memenangkan permainan!")


if st.button("🔄 Reset Game"):
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.winning_line = []
    st.session_state.celebrate = False
