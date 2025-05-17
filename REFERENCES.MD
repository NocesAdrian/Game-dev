## 🎮 Pygame Modules and Their Core Functions

### **1. `pygame.display`**

*Controls the display window and screen.*

* `pygame.display.set_mode()`: Initialize a window or screen for display.
* `pygame.display.set_caption()`: Set the current window caption.
* `pygame.display.get_caption()`: Get the current window caption.
* `pygame.display.set_icon()`: Change the system image for the display window.
* `pygame.display.get_surface()`: Get a reference to the currently set display surface.
* `pygame.display.flip()`: Update the full display Surface to the screen.
* `pygame.display.update()`: Update portions of the screen for software displays.
* `pygame.display.get_driver()`: Get the name of the current video driver.
* `pygame.display.Info()`: Create a video display information object.
* `pygame.display.quit()`: Uninitialize the display module.
* `pygame.display.init()`: Initialize the display module.([scuba.cs.uchicago.edu][1], [pygame.readthedocs.io][2], [ksvi.mff.cuni.cz][3], [pygame.org][4], [pygame.org][5], [pygame.org][6])

### **2. `pygame.draw`**

*Draw simple shapes to a surface.*

* `pygame.draw.rect()`: Draw a rectangle.
* `pygame.draw.polygon()`: Draw a polygon.
* `pygame.draw.circle()`: Draw a circle.
* `pygame.draw.ellipse()`: Draw an ellipse.
* `pygame.draw.arc()`: Draw an elliptical arc.
* `pygame.draw.line()`: Draw a straight line.
* `pygame.draw.lines()`: Draw multiple contiguous straight lines.
* `pygame.draw.aaline()`: Draw an anti-aliased line.
* `pygame.draw.aalines()`: Draw a sequence of anti-aliased lines.([Engineering LibreTexts][7], [pygame.readthedocs.io][2], [pygame.org][4], [GeeksforGeeks][8], [pygame.org][6])

### **3. `pygame.image`**

*Load and save images.*

* `pygame.image.load()`: Load a new image from a file.
* `pygame.image.save()`: Save an image to a file.
* `pygame.image.get_extended()`: Check if extended image formats can be loaded.([pygame.org][9])

### **4. `pygame.event`**

*Manage the event queue.*

* `pygame.event.pump()`: Internally process pygame event handlers.
* `pygame.event.get()`: Get events from the queue.
* `pygame.event.poll()`: Get a single event from the queue.
* `pygame.event.wait()`: Wait for a single event from the queue.
* `pygame.event.clear()`: Remove all events from the queue.
* `pygame.event.post()`: Place a new event on the queue.
* `pygame.event.peek()`: Check if an event type is in the queue.
* `pygame.event.set_blocked()`: Control which events are allowed on the queue.
* `pygame.event.set_allowed()`: Control which events are allowed on the queue.
* `pygame.event.get_blocked()`: Check if a specific event type is blocked.([gamedevacademy.org][10], [pygame.org][6])

### **5. `pygame.mixer`**

*Load and play sounds.*

* `pygame.mixer.init()`: Initialize the mixer module.
* `pygame.mixer.quit()`: Uninitialize the mixer module.
* `pygame.mixer.get_init()`: Get the current initialization status.
* `pygame.mixer.Sound()`: Create a new Sound object from a file or buffer.
* `pygame.mixer.music.load()`: Load a music file for playback.
* `pygame.mixer.music.play()`: Start the playback of the music stream.
* `pygame.mixer.music.stop()`: Stop the music playback.
* `pygame.mixer.music.pause()`: Temporarily stop the music playback.
* `pygame.mixer.music.unpause()`: Resume paused music playback.
* `pygame.mixer.music.rewind()`: Restart music playback from the beginning.
* `pygame.mixer.music.set_volume()`: Set the music playback volume.
* `pygame.mixer.music.get_volume()`: Get the current music playback volume.
* `pygame.mixer.music.get_busy()`: Check if music is currently playing.([inventwithpython.com][11], [TutorialsPoint][12], [Engineering LibreTexts][7])

### **6. `pygame.font`**

*Render text.*

* `pygame.font.init()`: Initialize the font module.
* `pygame.font.quit()`: Uninitialize the font module.
* `pygame.font.get_init()`: Check if the font module is initialized.
* `pygame.font.get_fonts()`: Get a list of available system fonts.
* `pygame.font.match_font()`: Find the best match for a system font.
* `pygame.font.Font()`: Create a new Font object from a file.
* `pygame.font.SysFont()`: Create a Font object from system fonts.

### **7. `pygame.time`**

*Manage timing and framerate.*

* `pygame.time.Clock()`: Create an object to help track time.
* `pygame.time.get_ticks()`: Get the number of milliseconds since pygame.init() was called.
* `pygame.time.delay()`: Pause the program for an amount of milliseconds.
* `pygame.time.wait()`: Pause the program for an amount of milliseconds.([ryanstutorials.net][13])

### **8. `pygame.key`**

*Manage keyboard input.*

* `pygame.key.get_pressed()`: Get the state of all keyboard buttons.
* `pygame.key.get_mods()`: Get the state of modifier keys.
* `pygame.key.set_mods()`: Set the state of modifier keys.
* `pygame.key.get_repeat()`: Get the keyboard repeat settings.
* `pygame.key.set_repeat()`: Set the keyboard repeat settings.
* `pygame.key.name()`: Get the name of a key identifier.([scuba.cs.uchicago.edu][14], [ryanstutorials.net][13])

### **9. `pygame.mouse`**

*Manage mouse input.*

* `pygame.mouse.get_pressed()`: Get the state of the mouse buttons.
* `pygame.mouse.get_pos()`: Get the current mouse position.
* `pygame.mouse.set_pos()`: Set the current mouse position.
* `pygame.mouse.get_rel()`: Get the relative mouse movement.
* `pygame.mouse.set_visible()`: Set the visibility of the mouse cursor.
* `pygame.mouse.get_visible()`: Get the visibility of the mouse cursor.

### **10. `pygame.transform`**

*Perform image transformations.*

* `pygame.transform.flip()`: Flip an image horizontally or vertically.
* `pygame.transform.rotate()`: Rotate an image.
* `pygame.transform.scale()`: Scale an image to a new size.
* `pygame.transform.scale2x()`: Scale an image to double its size.
* `pygame.transform.smoothscale()`: Scale an image smoothly to a new size.
* `pygame.transform.chop()`: Remove a portion of an image.
* `pygame.transform.laplacian()`: Apply a Laplacian filter to an image.
* `pygame.transform.average_color()`: Find the average color of an image.

---

[1]: https://scuba.cs.uchicago.edu/pygame/tut/DisplayModes.html?utm_source=chatgpt.com "Setting Display Modes — pygame v2.6.1 documentation - SCU:BA"
[2]: https://pygame.readthedocs.io/en/latest/2_draw/draw.html?utm_source=chatgpt.com "Drawing graphics primitives — Pygame tutorial 2019 documentation"
[3]: https://ksvi.mff.cuni.cz/~dingle/2020-1/prog_1/pygame.html?utm_source=chatgpt.com "Pygame 2.0 Quick Reference - KSVI"
[4]: https://www.pygame.org/docs/?utm_source=chatgpt.com "Pygame Front Page — pygame v2.6.0 documentation"
[5]: https://www.pygame.org/docs/tut/DisplayModes.html?utm_source=chatgpt.com "Setting Display Modes — pygame v2.6.0 documentation"
[6]: https://www.pygame.org/docs/ref/draw.html?utm_source=chatgpt.com "pygame.draw — pygame v2.6.0 documentation"
[7]: https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_Languages/Making_Games_with_Python_and_Pygame_%28Sweigart%29/03%3A_Pygame_Basics/3.14%3A_Primitive_Drawing_Functions?utm_source=chatgpt.com "3.14: Primitive Drawing Functions - Engineering LibreTexts"
[8]: https://www.geeksforgeeks.org/pygame-drawing-objects-and-shapes/?utm_source=chatgpt.com "Pygame – Drawing Objects and Shapes | GeeksforGeeks"
[9]: https://www.pygame.org/docs/ref/image.html?utm_source=chatgpt.com "pygame.image — pygame v2.6.0 documentation"
[10]: https://gamedevacademy.org/pygame-functions-tutorial-complete-guide/?utm_source=chatgpt.com "Pygame Functions Tutorial - Complete Guide - GameDev Academy"
[11]: https://inventwithpython.com/pygame/chapter2.html?utm_source=chatgpt.com "Chapter 2 - Pygame Basics - Invent with Python"
[12]: https://www.tutorialspoint.com/pygame/pygame_loading_image.htm?utm_source=chatgpt.com "Loading Images in Pygame - Tutorialspoint"
[13]: https://ryanstutorials.net/pygame-tutorial/pygame-images.php?utm_source=chatgpt.com "PyGame Images - Ryan's Tutorials"
[14]: https://scuba.cs.uchicago.edu/pygame/ref/display.html?utm_source=chatgpt.com "pygame.display - SCU:BA"
