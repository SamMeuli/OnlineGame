from django.shortcuts import render, get_object_or_404, redirect
from .models import Sprite, Bullet, Enemy
from pynput import keyboard
from threading import Thread
from django.http import HttpResponse

# Create your views here.


def start(request):
    return render(request, 'blog/start.html', {})

def step(request, key):
    posx = Sprite.posx
    posy = Sprite.posy
    if key == 'up' or key == 'w':
        posy -= -1
    elif key == 'down' or key == 's':
        posy += 1
    elif key == 'right' or key == 'd':
        posx -= 1

    elif key == 'left' or key == 'a':
        posx += 1
    Sprite.posx = posx
    Sprite.posy = posy
    return render(request, 'blog/game_frames', {'sprite_posx': posx, 'sprite_posy': posy})


def game_frames(request):

    captured_keys=''

    key=captured_keys
    posx = Sprite.posx
    posy = Sprite.posy
    if key == 'up' or key == 'w':
        posy -= -1
        print('Hi: ', key)
    elif key == 'down' or key == 's':
        posy += 1
        print('Hi: ', key)
    elif key == 'right' or key == 'd':
        posx -= 1
        print('Hi: ', key)
    elif key == 'left' or key == 'a':
        posx += 1
        print('Hi: ', key)
    Sprite.posx = posx
    Sprite.posy = posy
    print(Sprite.posx, Sprite.posy)

    return render(request, 'blog/game_frames.html', {'sprite_posx': posx, 'sprite_posy': posy})


def on_press(key):
    if key == keyboard.Key.esc:
        return False
    try:
        k = key.char
    except:
        k = key.name
    if k in ['a', 's', 'd', 'w', 'up', 'down', 'left', 'right', 't']:
        captured_keys = k
        print(captured_keys)
        return captured_keys
    else:
        return None


def capture_keys():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
if not capture_keys:
    key_capture_thread = Thread(target=capture_keys)
    key_capture_thread.start()
