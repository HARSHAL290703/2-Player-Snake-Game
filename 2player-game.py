import streamlit as st
import numpy as np
import random
from PIL import Image, ImageDraw

# Initialize game state
GRID_SIZE = 20
CELL_SIZE = 20

if "state" not in st.session_state:
    st.session_state.state = {
        "snake1": [(5, 5)],
        "snake2": [(15, 15)],
        "food": (10, 10),
        "direction1": (0, 1),
        "direction2": (0, -1),
        "score1": 0,
        "score2": 0,
        "game_over": False,
    }


def draw_grid(grid_size, snake1, snake2, food):
    """Create a visual representation of the grid."""
    img = Image.new("RGB", (grid_size * CELL_SIZE, grid_size * CELL_SIZE), "black")
    draw = ImageDraw.Draw(img)

    # Draw food
    fx, fy = food
    draw.rectangle(
        [fx * CELL_SIZE, fy * CELL_SIZE, (fx + 1) * CELL_SIZE, (fy + 1) * CELL_SIZE],
        fill="red",
    )

    # Draw snake 1
    for x, y in snake1:
        draw.rectangle(
            [x * CELL_SIZE, y * CELL_SIZE, (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE],
            fill="green",
        )

    # Draw snake 2
    for x, y in snake2:
        draw.rectangle(
            [x * CELL_SIZE, y * CELL_SIZE, (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE],
            fill="blue",
        )

    return img


def move_snake(snake, direction):
    """Move the snake in the given direction."""
    head_x, head_y = snake[-1]
    new_head = (head_x + direction[0], head_y + direction[1])
    snake.append(new_head)
    return snake


def check_collision(snake, grid_size):
    """Check if the snake collides with the wall or itself."""
    head = snake[-1]
    x, y = head
    if x < 0 or y < 0 or x >= grid_size or y >= grid_size:
        return True
    if head in snake[:-1]:
        return True
    return False


def check_food(snake, food):
    """Check if the snake eats the food."""
    if snake[-1] == food:
        return True
    return False


# Game update
state = st.session_state.state
snake1 = state["snake1"]
snake2 = state["snake2"]
food = state["food"]
direction1 = state["direction1"]
direction2 = state["direction2"]
score1 = state["score1"]
score2 = state["score2"]

# Control inputs
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("Up (Player 1)"):
        state["direction1"] = (-1, 0)
with col2:
    if st.button("Left (Player 1)"):
        state["direction1"] = (0, -1)
with col3:
    if st.button("Right (Player 1)"):
        state["direction1"] = (0, 1)
with col4:
    if st.button("Down (Player 1)"):
        state["direction1"] = (1, 0)

col5, col6, col7, col8 = st.columns(4)
with col5:
    if st.button("Up (Player 2)"):
        state["direction2"] = (-1, 0)
with col6:
    if st.button("Left (Player 2)"):
        state["direction2"] = (0, -1)
with col7:
    if st.button("Right (Player 2)"):
        state["direction2"] = (0, 1)
with col8:
    if st.button("Down (Player 2)"):
        state["direction2"] = (1, 0)

# Move snakes
if not state["game_over"]:
    state["snake1"] = move_snake(snake1, direction1)
    state["snake2"] = move_snake(snake2, direction2)

    # Check for collisions
    if check_collision(state["snake1"], GRID_SIZE) or check_collision(
        state["snake2"], GRID_SIZE
    ):
        state["game_over"] = True
    else:
        # Check if snakes eat food
        if check_food(state["snake1"], food):
            state["score1"] += 10
            state["food"] = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
        else:
            state["snake1"].pop(0)

        if check_food(state["snake2"], food):
            state["score2"] += 10
            state["food"] = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
        else:
            state["snake2"].pop(0)

# Display game state
grid_image = draw_grid(GRID_SIZE, state["snake1"], state["snake2"], state["food"])
st.image(grid_image, caption="Snake Game", use_column_width=True)

# Display scores
st.write(f"Player 1 Score: {state['score1']}")
st.write(f"Player 2 Score: {state['score2']}")

if state["game_over"]:
    st.write("Game Over! Reload to play again.")
