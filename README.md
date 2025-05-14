# Game-dev

### **CORE GAME DEV CONCEPTS (NO ENGINE VERSION)**

---

#### 1. **Game Title & Metadata**

* What your game is called
* Author info, version, icon, etc.

---

#### 2. **Game Window & Screen Settings**

* Resolution (e.g., 800x600)
* Fullscreen or windowed
* VSync (sync to monitor refresh)
* Aspect Ratio (for pixel-perfect games)

---

#### 3. **Game Loop**

*The heart. The microwave of PhoneWave.*

```text
while game_running:
    handle_input()
    update_logic()
    render_screen()
```

* Runs until player quits
* Controls timing, updates, rendering

---

#### 4. **FPS & Delta Time**

* **FPS** = Frames per second. How fast you draw/update the game.
* **Delta Time (`dt`)** = Time between frames.

  * Used to make movement smooth and **frame-rate independent**.

```python
position += velocity * delta_time
```

---

#### 5. **Sprites**

* 2D images representing objects (player, enemies, bullets)
* Usually organized in a **sprite sheet**
* Drawn at x/y positions on the screen

---

#### 6. **Input / Event System**

* Keyboard
* Mouse
* Gamepad
* Events like QUIT, KEYDOWN, KEYUP

---

#### 7. **Collision Detection**

* **AABB (Axis-Aligned Bounding Box)** – simplest
* **Pixel-perfect** (slower)
* Used to detect hits, overlaps, physics, damage

---

#### 8. **State Machine**

* Controls **game flow**
* Examples:

  * Menu
  * Gameplay
  * Pause
  * Game Over
* Each state has its own logic and rendering

---

#### 9. **Game Objects / Entities**

* Everything in the game is an object/entity:

  * Has position, velocity, health, etc.
* Organized using **OOP** or ECS (Entity Component System)

---

#### 10. **Timers / Delays / Cooldowns**

* For shooting intervals, enemy spawns, animations
* Controlled via delta time or system clocks

---

#### 11. **Camera System**

* Follows player or focus point
* Adds scroll effect in bigger maps

---

#### 12. **Animations**

* Change sprites every frame or based on time
* Usually tied to actions (walk, jump, die)

---

#### 13. **Physics (Basic)**

* Gravity
* Acceleration
* Velocity updates
* Friction or drag

---

#### 14. **Sound System**

* Play sound effects on events
* Loop background music
* Volume controls

---

#### 15. **UI / HUD**

* Score, lives, health bar
* Buttons, menus
* Input feedback (like selected menu item)

---

#### 16. **Save / Load System (optional)**

* Store progress
* Use files (JSON, txt, binary)

---

#### 17. **Game Over / Restart Logic**

* Detect end conditions
* Reset or send to menu

---
