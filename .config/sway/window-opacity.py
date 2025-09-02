import i3ipc

ipc = i3ipc.Connection()
prev_focused = None

# Initial setup: set opacity for all existing windows
for window in ipc.get_tree():
    if window.focused:
        prev_focused = window
    else:
        window.command('opacity 0.8') # Unfocused windows are semi-transparent

def on_window_focus(ipc, focused):
    global prev_focused
    if focused.container.id != prev_focused.id:
        # Set focused window to opaque
        focused.container.command('opacity 0.96')
        # Set previously focused window to semi-transparent
        prev_focused.command('opacity 0.9')
        prev_focused = focused.container

ipc.on("window::focus", on_window_focus)
ipc.main()

