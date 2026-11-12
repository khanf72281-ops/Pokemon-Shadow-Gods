from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.clock import Clock
from kivy.core.window import Window
import random

class BattleArena(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.player_hp = 100
        self.boss_hp = 250
        self.player_y = 200
        self.boss_y = 220
        self.boss_dir = 1
        self.projectiles = []
        self.dna_charged = True
        self.game_over = False

        with self.canvas:
            # Background (Dark Shadow Arena)
            Color(0.08, 0.06, 0.14, 1)
            self.bg = Rectangle(pos=self.pos, size=Window.size)

            # Player (Shadow Trainer / Guardian)
            Color(0.2, 0.7, 1.0, 1)
            self.player_rect = Rectangle(pos=(100, self.player_y), size=(60, 80))

            # Eternal Void Boss
            Color(0.85, 0.15, 0.35, 1)
            self.boss_rect = Rectangle(pos=(Window.width - 200, self.boss_y), size=(110, 130))

        self.bind(size=self._update_bg, pos=self._update_bg)
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def _update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size
        self.boss_rect.pos = (self.width - 200, self.boss_y)

    def move_player(self, dy):
        if self.game_over:
            return
        self.player_y = max(100, min(self.height - 140, self.player_y + dy))
        self.player_rect.pos = (100, self.player_y)

    def shoot_soul_blast(self):
        if self.game_over:
            return
        with self.canvas:
            Color(0.3, 0.9, 1.0, 1)
            proj = Ellipse(pos=(170, self.player_y + 30), size=(28, 28))
        self.projectiles.append({'shape': proj, 'damage': 15, 'speed': 12})

    def use_dna_splice(self):
        if self.game_over or not self.dna_charged:
            return
        self.dna_charged = False
        with self.canvas:
            Color(1.0, 0.85, 0.1, 1)
            proj = Ellipse(pos=(170, self.player_y + 20), size=(55, 55))
        self.projectiles.append({'shape': proj, 'damage': 55, 'speed': 15})
        Clock.schedule_once(self._recharge_dna, 5.0)

    def _recharge_dna(self, dt):
        self.dna_charged = True

    def update(self, dt):
        if self.game_over:
            return

        # Move Boss
        self.boss_y += self.boss_dir * 3
        if self.boss_y > self.height - 180 or self.boss_y < 100:
            self.boss_dir *= -1
        self.boss_rect.pos = (self.width - 200, self.boss_y)

        # Update Projectiles
        for p in self.projectiles[:]:
            x, y = p['shape'].pos
            x += p['speed']
            p['shape'].pos = (x, y)

            # Check Boss Hit
            bx, by = self.boss_rect.pos
            bw, bh = self.boss_rect.size
            if bx < x < bx + bw and by < y < by + bh:
                self.boss_hp = max(0, self.boss_hp - p['damage'])
                self.canvas.remove(p['shape'])
                self.projectiles.remove(p)
                if self.boss_hp == 0:
                    self.game_over = True
                    App.get_running_app().show_end("VICTORY! ETERNAL VOID DEFEATED!")
            elif x > self.width:
                self.canvas.remove(p['shape'])
                self.projectiles.remove(p)

        App.get_running_app().update_hud(self.player_hp, self.boss_hp, self.dna_charged)


class ShadowGodsApp(App):
    def build(self):
        self.root = FloatLayout()
        self.arena = BattleArena()
        self.root.add_widget(self.arena)

        # HUD Label
        self.hud = Label(
            text="PLAYER HP: 100  |  ETERNAL VOID HP: 250",
            size_hint=(1, 0.1),
            pos_hint={'x': 0, 'top': 1},
            bold=True,
            font_size='18sp'
        )
        self.root.add_widget(self.hud)

        # Touch Controls (Left: Movement, Right: Attacks)
        btn_up = Button(text="UP", size_hint=(0.14, 0.14), pos_hint={'x': 0.03, 'y': 0.22})
        btn_up.bind(on_press=lambda x: self.arena.move_player(45))

        btn_down = Button(text="DOWN", size_hint=(0.14, 0.14), pos_hint={'x': 0.03, 'y': 0.05})
        btn_down.bind(on_press=lambda x: self.arena.move_player(-45))

        btn_blast = Button(
            text="SOUL BLAST",
            background_color=(0.1, 0.6, 1, 1),
            size_hint=(0.18, 0.14),
            pos_hint={'right': 0.97, 'y': 0.22}
        )
        btn_blast.bind(on_press=lambda x: self.arena.shoot_soul_blast())

        self.btn_dna = Button(
            text="DNA SPLICE",
            background_color=(1, 0.75, 0, 1),
            size_hint=(0.18, 0.14),
            pos_hint={'right': 0.97, 'y': 0.05}
        )
        self.btn_dna.bind(on_press=lambda x: self.arena.use_dna_splice())

        self.root.add_widget(btn_up)
        self.root.add_widget(btn_down)
        self.root.add_widget(btn_blast)
        self.root.add_widget(self.btn_dna)
        return self.root

    def update_hud(self, p_hp, b_hp, dna_ready):
        if not self.arena.game_over:
            status = "READY" if dna_ready else "CHARGING..."
            self.hud.text = f"PLAYER HP: {p_hp}  |  ETERNAL VOID HP: {b_hp}  |  DNA: {status}"

    def show_end(self, message):
        self.hud.text = message

if __name__ == '__main__':
    ShadowGodsApp().run()
