import tkinter as tk
import os
import vlc
import random
from io import BytesIO
from mutagen.id3 import ID3
from mutagen.flac import FLAC
from PIL import Image, ImageTk

vlc_path = r"C:\Program Files\VideoLAN\VLC"
os.add_dll_directory(vlc_path)

instance = vlc.Instance()
player = instance.media_player_new()

MUSIC_FOLDER = os.path.expanduser("~/Music")

music_files = []
filtered_music_files = []
bar_heights = []
current_index = -1
song_widgets = []
thumbnail_cache = {}

def get_album_art(file_path):
    try:
        if file_path.lower().endswith('.mp3'):
            audio = ID3(file_path)
            for tag in audio.keys():
                if tag.startswith('APIC:'):
                    albumart = audio.getall(tag)[0].data
                    image = Image.open(BytesIO(albumart))
                    return image
        elif file_path.lower().endswith('.flac'):
            audio = FLAC(file_path)
            if audio.pictures:
                albumart = audio.pictures[0].data
                image = Image.open(BytesIO(albumart))
                return image
    except Exception as e:
        print("Error extracting album art:", e)
    return None

def load_local_files():
    music_files.clear()
    for root_dir, _, files in os.walk(MUSIC_FOLDER):
        for file in files:
            if file.lower().endswith(('.mp3', '.wav')):
                full_path = os.path.join(root_dir, file)
                music_files.append(full_path)

def filter_music_list(*args):
    query = search_var.get().lower()
    filtered_music_files.clear()

    for widget in song_widgets:
        widget.destroy()
    song_widgets.clear()

    for file in music_files:
        filename = os.path.basename(file)
        if query in filename.lower():
            filtered_music_files.append(file)
            index_in_filtered = len(filtered_music_files) - 1

            image = get_album_art(file)
            if image:
                image = image.resize((40, 40), Image.LANCZOS)
            else:
                image = Image.open("/mnt/data/e5cd9586-3178-4590-ab3e-26bd837ebd00.png").resize((40, 40), Image.LANCZOS)

            photo = ImageTk.PhotoImage(image)
            thumbnail_cache[file] = photo

            song_frame = tk.Frame(list_inner_frame, bg="#000000", pady=2)
            song_frame.pack(fill="x", padx=10)

            art_label = tk.Label(song_frame, image=photo, bg="#000000")
            art_label.image = photo
            art_label.pack(side="left")

            text_label = tk.Label(song_frame, text=filename, fg="white", bg="#000000", font=("Helvetica", 11), anchor="w")
            text_label.pack(side="left", padx=10, fill="x", expand=True)

            # Use correct index
            song_frame.bind("<Button-1>", lambda e, i=index_in_filtered: play_music_file(i))
            art_label.bind("<Button-1>", lambda e, i=index_in_filtered: play_music_file(i))
            text_label.bind("<Button-1>", lambda e, i=index_in_filtered: play_music_file(i))

            song_widgets.append(song_frame)


def play_music_file(index):
    global current_index
    current_index = index
    file = filtered_music_files[current_index]
    media = instance.media_new(file)
    player.set_media(media)
    label.config(text=f"🎵 Loading: {os.path.basename(file)}")
    animate_label(f"🎵 Now Playing: {os.path.basename(file)}")
    volume_slider.set(100)
    player.audio_set_volume(100)
    player.play()
    scroll_text()
    show_album_art(file)
    monitor_end()

def play_music(): player.play()
def pause_music(): player.pause()
def set_volume(val): player.audio_set_volume(int(val))

def animate_label(text, i=0):
    def loop():
        label.config(text=text[:i+1])
        if i+1 < len(text):
            label.after(30, lambda: animate_label(text, i+1))
    loop()

def animate_spectrum():
    volume = player.audio_get_volume()
    playing = player.is_playing()
    for i, bar in enumerate(bars):
        max_height = int((volume / 100) * 100) if playing else 5
        target_height = random.randint(20, max(30, max_height)) if playing else random.randint(1, 3)
        last = bar_heights[i]
        new_height = int(last + (target_height - last) * 0.3)
        bar_heights[i] = new_height
        spectrum_canvas.coords(bar, spectrum_canvas.coords(bar)[0], 100 - new_height, spectrum_canvas.coords(bar)[2], 100)
    delay = max(60, 200 - int((volume / 100) * 150)) if playing else 300
    root.after(delay, animate_spectrum)

def scroll_text(i=0):
    full = label.cget('text')
    if len(full) > 1:
        scroll = full[i:] + "   " + full[:i]
        label.config(text=scroll)
        label.after(200, lambda: scroll_text((i+1) % len(full)))

def pulse_background():
    vol = player.audio_get_volume()
    intensity = hex(15 + int(vol / 10))[2:]
    intensity = intensity.zfill(2)
    color = f"#00{intensity}00"
    root.configure(bg=color)
    spectrum_canvas.configure(bg=color)
    root.after(500, pulse_background)

def update_progress():
    if player.is_playing():
        length = player.get_length()
        pos = player.get_time()
        if length > 0:
            percent = (pos / length) * 100
            progress_var.set(percent)
    root.after(500, update_progress)

def seek_music(val):
    if player.is_playing() or player.get_length() > 0:
        length = player.get_length()
        seek_time = (float(val) / 100) * length
        player.set_time(int(seek_time))

def prev_music():
    if filtered_music_files:
        index = (current_index - 1) % len(filtered_music_files)
        play_music_file(index)

def next_music():
    if filtered_music_files:
        index = (current_index + 1) % len(filtered_music_files)
        play_music_file(index)

def shuffle_music():
    if filtered_music_files:
        index = random.randint(0, len(filtered_music_files) - 1)
        play_music_file(index)

def show_album_art(file):
    image = get_album_art(file)
    if image:
        image = image.resize((95, 95), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        cover_canvas.delete("all")
        cover_canvas.create_oval(10, 10, 90, 90, fill="#1DB954", outline="")
        cover_canvas.create_image(50, 50, image=photo)
        cover_canvas.image = photo
    else:
        cover_canvas.delete("all")
        cover_canvas.create_oval(10, 10, 90, 90, fill="#1DB954", outline="")
        cover_canvas.create_text(50, 50, text="🎵", font=("Helvetica", 24))

def monitor_end():
    if player.get_state() == vlc.State.Ended:
        next_music()
    else:
        root.after(1000, monitor_end)

root = tk.Tk()
root.title("Temu Spotify")
root.attributes("-fullscreen", True)
root.configure(bg="#000000")
root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))

is_fullscreen = True 

def toggle_fullscreen(event=None):
    global is_fullscreen
    is_fullscreen = not is_fullscreen
    root.attributes("-fullscreen", is_fullscreen)

root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))
root.bind("<f>", toggle_fullscreen)
root.bind("<F>", toggle_fullscreen)  

spotify_green = "#1CB451"
font_title = ("Helvetica", 18, "bold")
font_label = ("Helvetica", 12)
button_style = {
    "bg": spotify_green, "fg": "black", "font": ("Helvetica", 12),
    "width": 12, "bd": 0, "relief": "flat", "activebackground": "#1aa34a"
}

search_var = tk.StringVar()

def on_entry_click(event):
    if search_entry.get() == "Search music...":
        search_entry.delete(0, "end")
        search_entry.config(fg="white")

def on_focusout(event):
    if search_entry.get() == "":
        search_entry.insert(0, "Search music...")
        search_entry.config(fg="#777777")

search_entry = tk.Entry(root, textvariable=search_var, font=("Helvetica", 12), bg="#121212", fg="#777777", insertbackground="white")
search_entry.pack(pady=(10, 0), padx=20, fill="x")
search_entry.insert(0, "Search music...")
search_entry.bind('<FocusIn>', on_entry_click)
search_entry.bind('<FocusOut>', on_focusout)

search_var.trace_add("write", filter_music_list)

frame = tk.Frame(root, bg="#000000")
frame.pack(pady=10, fill="both", expand=True)

list_canvas_frame = tk.Frame(frame, bg="#000000")
list_canvas_frame.pack(fill="both", expand=True)

list_canvas = tk.Canvas(list_canvas_frame, bg="#000000", highlightthickness=0)
scrollbar = tk.Scrollbar(list_canvas_frame, orient="vertical", command=list_canvas.yview)
list_inner_frame = tk.Frame(list_canvas, bg="#000000")

list_inner_frame.bind(
    "<Configure>",
    lambda e: list_canvas.configure(scrollregion=list_canvas.bbox("all"))
)

list_canvas.create_window((0, 0), window=list_inner_frame, anchor="nw")
list_canvas.configure(yscrollcommand=scrollbar.set)

list_canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

cover_canvas = tk.Canvas(root, width=100, height=100, bg="#000000", highlightthickness=0)
cover_canvas.create_oval(10, 10, 90, 90, fill=spotify_green, outline="")
cover_canvas.create_text(50, 50, text="🎵", font=("Helvetica", 24))
cover_canvas.pack(pady=5)

title = tk.Label(root, text="My Playlist", font=font_title, bg="#000000", fg=spotify_green, borderwidth=0, highlightthickness=0)
title.pack(pady=10)

label = tk.Label(root, text="This place is quiet...", font=font_label, bg="#000000", fg="#b3b3b3", borderwidth=0, highlightthickness=0)
label.pack(pady=5)

button_frame = tk.Frame(root, bg="#000000")
button_frame.pack(pady=10)

buttons = [
    ("⏮ Prev", prev_music),
    ("▶ Play", play_music),
    ("⏸ Pause", pause_music),
    ("⏭ Next", next_music),
    ("🔀 Shuffle", shuffle_music),
]

for idx, (text, cmd) in enumerate(buttons):
    btn = tk.Button(button_frame, text=text, command=cmd, **button_style)
    btn.grid(row=0, column=idx, padx=6)
    btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#1aa34a"))
    btn.bind("<Leave>", lambda e, b=btn: b.config(bg=spotify_green))

progress_frame = tk.Frame(root, bg="#0F1909")
progress_frame.pack(pady=10, fill="x", padx=20)

progress_var = tk.DoubleVar()
progress_slider = tk.Scale(progress_frame, variable=progress_var, from_=0, to=100, orient="horizontal",
                           showvalue=0, resolution=0.1, length=400, command=seek_music,
                           bg="#000000", fg="white", troughcolor=spotify_green, highlightthickness=0, bd=0)
progress_slider.pack()

vol_label = tk.Label(root, text="Volume", font=("Helvetica", 10), bg="#000000", fg=spotify_green, borderwidth=0, highlightthickness=0)
vol_label.pack(pady=(10, 2))

volume_slider = tk.Scale(root, from_=0, to=100, orient="horizontal", command=set_volume,
                         bg="#000000", fg="white", troughcolor=spotify_green, highlightthickness=0, bd=0)
volume_slider.set(100)
volume_slider.pack()

spectrum_canvas = tk.Canvas(root, width=400, height=100, bg="#000000", highlightthickness=0)
spectrum_canvas.pack(pady=10)
bars = []

bar_count = 20
bar_width = 15
spacing = 5
for i in range(bar_count):
    x0 = i * (bar_width + spacing)
    x1 = x0 + bar_width
    bar = spectrum_canvas.create_rectangle(x0, 100, x1, 100, fill=spotify_green, width=0)
    bars.append(bar)
    bar_heights.append(1)

footer = tk.Label(root, text="Made By Mikayil in Python", font=("Helvetica", 9), bg="#000000", fg="#555555")
footer.pack(side="bottom", pady=10)

load_local_files()
search_var.set("")
filter_music_list()
animate_spectrum()
pulse_background()
update_progress()
root.mainloop()
