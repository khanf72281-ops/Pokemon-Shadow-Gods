import json
import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.clock import Clock
from kivy.core.window import Window

Window.size = (800, 450)

class ShadowGodsGame(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hp = 100
        self.boss_hp = 1000
        self.player_pos = [150, 200]
        self.boss_pos = [600, 200]
        self.orbs = []
        self.score = 0

        # HUD Labels
        self.status_label = Label(
            text="BHARAT REGION: Eternal Void Raid | HP: 100 | Boss HP: 1000",
            pos_hint={'x': 0, 'top': 1},
            size_hint=(1, 0.1),
            bold=True
        )
        self.add_widget(self.status_label)

        # Virtual Controls for Galaxy J7 Nxt
        btn_up = Button(text="UP", pos_hint={'x': 0.08, 'y': 0.22}, size_hint=(0.1, 0.12))
        btn_down = Button(text="DOWN", pos_hint={'x': 0.08, 'y': 0.05}, size_hint=(0.1, 0.12))
        btn_atk = Button(text="SOUL BLAST", pos_hint={'right': 0.95, 'y': 0.12}, size_hint=(0.18, 0.16), background_color=(0.2, 0.6, 1, 1))
        btn_splice = Button(text="DNA SPLICE", pos_hint={'right': 0.75, 'y': 0.12}, size_hint=(0.18, 0.16), background_color=(0.8, 0.2, 0.9, 1))

        btn_up.bind(on_press=lambda x: self.move_player(0, 35))
        btn_down.bind(on_press=lambda x: self.move_player(0, -35))
        btn_atk.bind(on_press=lambda x: self.attack_boss(60, "Soul Blast"))
        btn_splice.bind(on_press=lambda x: self.attack_boss(150, "DNA Splice Fusion"))

        self.add_widget(btn_up)
        self.add_widget(btn_down)
        self.add_widget(btn_atk)
        self.add_widget(btn_splice)

        Clock.schedule_interval(self.update, 1.0 / 30.0)
        Clock.schedule_interval(self.spawn_orb, 1.8)

    def move_player(self, dx, dy):
        self.player_pos[1] = max(60, min(360, self.player_pos[1] + dy))

    def attack_boss(self, dmg, move_name):
        if self.boss_hp > 0 and self.hp > 0:
            self.boss_hp = max(0, self.boss_hp - dmg)
            self.status_label.text = f"Used {move_name}! | HP: {self.hp} | Eternal Void Boss: {self.boss_hp}"
            if self.boss_hp == 0:
                self.status_label.text = "VICTORY! The Eternal Void has been purified!"

    def spawn_orb(self, dt):
        if self.boss_hp > 0 and self.hp > 0:
            self.orbs.append([self.boss_pos[0], random.randint(80, 350)])

    def update(self, dt):
        self.canvas.before.clear()
        with self.canvas.before:
            # Background
            Color(0.08, 0.05, 0.15, 1)
            Rectangle(pos=(0, 0), size=Window.size)

            # Player (Bharat Guardian)
            Color(0.2, 0.9, 0.4, 1)
            Ellipse(pos=self.player_pos, size=(45, 45))

            # Eternal Void Boss
            Color(0.7, 0.1, 0.9, 1)
            Ellipse(pos=self.boss_pos, size=(80, 80))

            # Shadow Orbs
            Color(1, 0.2, 0.2, 1)
            for orb in self.orbs[:]:
                orb[0] -= 8
                Ellipse(pos=orb, size=(22, 22))
                if abs(orb[0] - self.player_pos[0]) < 35 and abs(orb[1] - self.player_pos[1]) < 35:
                    self.hp = max(0, self.hp - 15)
                    self.orbs.remove(orb)
                    self.status_label.text = f"Hit by Shadow Orb! | HP: {self.hp} | Boss HP: {self.boss_hp}"
                    if self.hp == 0:
                        self.status_label.text = "DEFEATED! Restart app to try again."
                elif orb[0] < 0:
                    self.orbs.remove(orb)

class PokemonShadowGodsApp(App):
    def build(self):
        return ShadowGodsGame()

if __name__ == '__main__':
    PokemonShadowGodsApp().run()
