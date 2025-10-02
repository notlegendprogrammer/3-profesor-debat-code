"""
Quantum State Simulator - Schrödinger's Cat
Enhanced Monte Carlo Wave Function Collapse
Python Version with Tkinter GUI

=== INSTALLATION GUIDE ===

LINUX (Ubuntu/Debian):
    sudo apt-get update
    sudo apt-get install python3-tk

LINUX (Fedora/RedHat):
    sudo dnf install python3-tkinter

LINUX (Arch):
    sudo pacman -S tk

macOS:
    # Tkinter biasanya sudah included dengan Python dari python.org
    # Jika belum, install via Homebrew:
    brew install python-tk

Windows:
    # Tkinter biasanya sudah included dengan Python installer dari python.org
    # Jika belum ada, reinstall Python dan centang "tcl/tk and IDLE"

=== HOW TO RUN ===
    python quantum_simulator.py

atau

    python3 quantum_simulator.py

========================
"""

import tkinter as tk
from tkinter import ttk
import random
import math
import time
from threading import Thread

class QuantumSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("⚛️ Quantum State Simulator")
        self.root.geometry("1400x1000")
        self.root.configure(bg="#0a0a0a")

        # Quantum state variables
        self.current_state = None
        self.total_observations = 0
        self.alive_results = 0
        self.dead_results = 0
        self.wave_time = 0
        self.is_collapsed = False
        self.start_time = time.time()
        self.use_decay = False
        self.mc_running = False

        self.setup_ui()
        self.animate_wave()

    def setup_ui(self):
        # Main container
        main_frame = tk.Frame(self.root, bg="#0a0a0a")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Title
        title = tk.Label(
            main_frame,
            text="⚛️ QUANTUM STATE SIMULATOR",
            font=("Courier", 32, "bold"),
            fg="#00ff41",
            bg="#0a0a0a"
        )
        title.pack(pady=(0, 5))

        subtitle = tk.Label(
            main_frame,
            text="Schrödinger's Cat - Enhanced Monte Carlo Wave Function Collapse",
            font=("Courier", 14),
            fg="#888888",
            bg="#0a0a0a"
        )
        subtitle.pack(pady=(0, 20))

        # Display area
        display_frame = tk.Frame(main_frame, bg="#0a0a0a")
        display_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Left: Cat box
        cat_frame = tk.Frame(display_frame, bg="#1a1a1a", highlightbackground="#00ff41", highlightthickness=2)
        cat_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        self.quantum_state_label = tk.Label(
            cat_frame,
            text="SUPERPOSITION STATE",
            font=("Courier", 12, "bold"),
            fg="#00ff41",
            bg="#2a2a2a",
            pady=10
        )
        self.quantum_state_label.pack(fill=tk.X, padx=10, pady=10)

        self.cat_display = tk.Label(
            cat_frame,
            text="🐱",
            font=("Arial", 100),
            fg="#00ff41",
            bg="#1a1a1a"
        )
        self.cat_display.pack(pady=20)

        self.state_text = tk.Label(
            cat_frame,
            text="State: Unknown",
            font=("Courier", 11),
            fg="#00ff41",
            bg="#1a1a1a"
        )
        self.state_text.pack(pady=5)

        self.decay_label = tk.Label(
            cat_frame,
            text="Decay: 0.0%",
            font=("Courier", 9),
            fg="#ff8800",
            bg="#1a1a1a"
        )
        self.decay_label.pack(pady=5)

        # Right: Probability display
        prob_frame = tk.Frame(display_frame, bg="#1a1a1a", highlightbackground="#00ff41", highlightthickness=2)
        prob_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        prob_title = tk.Label(
            prob_frame,
            text="📊 Probability Distribution",
            font=("Courier", 12, "bold"),
            fg="#00ff41",
            bg="#1a1a1a"
        )
        prob_title.pack(pady=10)

        # Alive probability
        alive_container = tk.Frame(prob_frame, bg="#1a1a1a")
        alive_container.pack(fill=tk.X, padx=20, pady=10)

        alive_label_frame = tk.Frame(alive_container, bg="#1a1a1a")
        alive_label_frame.pack(fill=tk.X)

        tk.Label(alive_label_frame, text="😺 Alive", font=("Courier", 10),
                fg="#00ff41", bg="#1a1a1a").pack(side=tk.LEFT)
        self.alive_prob_label = tk.Label(alive_label_frame, text="50.00%",
                                        font=("Courier", 10), fg="#00ff41", bg="#1a1a1a")
        self.alive_prob_label.pack(side=tk.RIGHT)

        self.alive_progress = ttk.Progressbar(
            alive_container,
            length=300,
            mode='determinate',
            maximum=100,
            value=50
        )
        self.alive_progress.pack(fill=tk.X, pady=5)

        # Dead probability
        dead_container = tk.Frame(prob_frame, bg="#1a1a1a")
        dead_container.pack(fill=tk.X, padx=20, pady=10)

        dead_label_frame = tk.Frame(dead_container, bg="#1a1a1a")
        dead_label_frame.pack(fill=tk.X)

        tk.Label(dead_label_frame, text="💀 Dead", font=("Courier", 10),
                fg="#ff0041", bg="#1a1a1a").pack(side=tk.LEFT)
        self.dead_prob_label = tk.Label(dead_label_frame, text="50.00%",
                                       font=("Courier", 10), fg="#ff0041", bg="#1a1a1a")
        self.dead_prob_label.pack(side=tk.RIGHT)

        self.dead_progress = ttk.Progressbar(
            dead_container,
            length=300,
            mode='determinate',
            maximum=100,
            value=50
        )
        self.dead_progress.pack(fill=tk.X, pady=5)

        # Wave visualization
        self.wave_canvas = tk.Canvas(
            main_frame,
            height=150,
            bg="#1a1a1a",
            highlightbackground="#00ff41",
            highlightthickness=2
        )
        self.wave_canvas.pack(fill=tk.X, pady=20)

        # Control buttons
        button_frame = tk.Frame(main_frame, bg="#0a0a0a")
        button_frame.pack(pady=10)

        btn_style = {
            "font": ("Courier", 11, "bold"),
            "bg": "#0a0a0a",
            "fg": "#00ff41",
            "activebackground": "#00ff41",
            "activeforeground": "#0a0a0a",
            "relief": tk.SOLID,
            "borderwidth": 2,
            "cursor": "hand2",
            "padx": 20,
            "pady": 10
        }

        self.observe_btn = tk.Button(
            button_frame,
            text="👁️ OBSERVE",
            command=self.observe_state,
            **btn_style
        )
        self.observe_btn.pack(side=tk.LEFT, padx=5)

        self.reset_btn = tk.Button(
            button_frame,
            text="🔄 RESET",
            command=self.reset_state,
            **btn_style
        )
        self.reset_btn.pack(side=tk.LEFT, padx=5)

        self.monte_carlo_btn = tk.Button(
            button_frame,
            text="🎲 MONTE CARLO (1000x)",
            command=self.run_monte_carlo,
            **btn_style
        )
        self.monte_carlo_btn.pack(side=tk.LEFT, padx=5)

        # Decay toggle
        self.decay_var = tk.BooleanVar(value=False)
        self.decay_check = tk.Checkbutton(
            button_frame,
            text="⏱️ Decay Mode",
            variable=self.decay_var,
            command=self.toggle_decay,
            font=("Courier", 10),
            fg="#ff8800",
            bg="#0a0a0a",
            selectcolor="#1a1a1a",
            activebackground="#0a0a0a",
            activeforeground="#ff8800"
        )
        self.decay_check.pack(side=tk.LEFT, padx=5)

        # Statistics
        stats_frame = tk.Frame(main_frame, bg="#0a0a0a")
        stats_frame.pack(fill=tk.X, pady=10)

        stat_style = {
            "bg": "#1a1a1a",
            "highlightbackground": "#00ff41",
            "highlightthickness": 1
        }

        for i, (label, var_name) in enumerate([
            ("Total Observations", "total_obs"),
            ("Alive Results", "alive_count"),
            ("Dead Results", "dead_count"),
            ("Alive Probability", "avg_prob")
        ]):
            stat_box = tk.Frame(stats_frame, **stat_style)
            stat_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

            value_label = tk.Label(
                stat_box,
                text="0" if i < 3 else "50.0%",
                font=("Courier", 20, "bold"),
                fg="#00ff41",
                bg="#1a1a1a"
            )
            value_label.pack(pady=(10, 0))
            setattr(self, f"{var_name}_label", value_label)

            desc_label = tk.Label(
                stat_box,
                text=label,
                font=("Courier", 8),
                fg="#888888",
                bg="#1a1a1a"
            )
            desc_label.pack(pady=(0, 10))

        # Terminal
        terminal_frame = tk.Frame(main_frame, bg="#000000",
                                 highlightbackground="#00ff41", highlightthickness=2)
        terminal_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        terminal_scroll = tk.Scrollbar(terminal_frame)
        terminal_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.terminal = tk.Text(
            terminal_frame,
            height=8,
            bg="#000000",
            fg="#00ff41",
            font=("Courier", 9),
            yscrollcommand=terminal_scroll.set,
            state=tk.DISABLED
        )
        self.terminal.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        terminal_scroll.config(command=self.terminal.yview)

        self.add_log("Quantum State Simulator initialized...")
        self.add_log("Wave function in superposition state")
        self.add_log("Ready for observation")

        # Credits
        credit = tk.Label(
            main_frame,
            text="💻 Enhanced Monte Carlo | Wave Function Collapse | Quantum Decay Simulation",
            font=("Courier", 8),
            fg="#666666",
            bg="#0a0a0a"
        )
        credit.pack(pady=5)

    def toggle_decay(self):
        self.use_decay = self.decay_var.get()
        if self.use_decay:
            self.add_log("⏱️ Decay mode ENABLED - Death probability increases over time")
            self.start_time = time.time()
        else:
            self.add_log("⏱️ Decay mode DISABLED - Standard 50/50 probability")
        self.update_decay_display()

    def get_decay_factor(self):
        if not self.use_decay:
            return 0.0
        elapsed = time.time() - self.start_time
        # Decay increases over 60 seconds, max +30% death probability
        decay = min(elapsed / 60.0, 1.0) * 0.3
        return decay

    def update_decay_display(self):
        if not self.is_collapsed:
            decay = self.get_decay_factor()
            self.decay_label.config(text=f"Decay: {decay*100:.1f}%")
            self.root.after(100, self.update_decay_display)

    def add_log(self, message):
        self.terminal.config(state=tk.NORMAL)
        timestamp = time.strftime("%H:%M:%S")
        self.terminal.insert(tk.END, f"[{timestamp}] {message}\n")
        self.terminal.see(tk.END)
        self.terminal.config(state=tk.DISABLED)

    def animate_wave(self):
        self.wave_canvas.delete("all")
        width = self.wave_canvas.winfo_width() or 800
        height = self.wave_canvas.winfo_height() or 150

        center_y = height / 2
        amplitude = 5 if self.is_collapsed else 30
        frequency = 0.02

        # Main wave
        points = []
        for x in range(width):
            y = center_y + math.sin(x * frequency + self.wave_time) * amplitude
            points.append((x, y))

        if len(points) > 1:
            self.wave_canvas.create_line(points, fill="#00ff41", width=2, smooth=True)

        # Interference wave (only in superposition)
        if not self.is_collapsed:
            points2 = []
            for x in range(width):
                y = center_y + math.sin(x * frequency * 1.5 - self.wave_time) * amplitude * 0.7
                points2.append((x, y))

            if len(points2) > 1:
                self.wave_canvas.create_line(points2, fill="#ff0041", width=2, smooth=True)

        self.wave_time += 0.05
        self.root.after(50, self.animate_wave)

    def update_stats(self):
        self.total_obs_label.config(text=str(self.total_observations))
        self.alive_count_label.config(text=str(self.alive_results))
        self.dead_count_label.config(text=str(self.dead_results))

        if self.total_observations > 0:
            prob = (self.alive_results / self.total_observations * 100)
            self.avg_prob_label.config(text=f"{prob:.1f}%")

            # Update probability bars based on actual results
            self.alive_prob_label.config(text=f"{prob:.2f}%")
            self.dead_prob_label.config(text=f"{100-prob:.2f}%")
            self.alive_progress.config(value=prob)
            self.dead_progress.config(value=100-prob)

    def observe_state(self):
        if self.current_state is not None:
            self.add_log("State already collapsed. Reset to observe again.")
            return

        self.is_collapsed = True

        # Calculate death probability with decay
        decay_factor = self.get_decay_factor()
        death_probability = 0.5 + decay_factor

        is_alive = random.random() >= death_probability

        self.current_state = is_alive
        self.total_observations += 1

        if is_alive:
            self.alive_results += 1
            self.cat_display.config(text="😺", fg="#00ff41")
            self.quantum_state_label.config(text="COLLAPSED: ALIVE")
            self.state_text.config(text="State: Alive")
            self.add_log(f"Wave function collapsed! Cat is ALIVE 😺 (p_death={death_probability:.2%})")
        else:
            self.dead_results += 1
            self.cat_display.config(text="💀", fg="#ff0041")
            self.quantum_state_label.config(text="COLLAPSED: DEAD")
            self.state_text.config(text="State: Dead")
            self.add_log(f"Wave function collapsed! Cat is DEAD 💀 (p_death={death_probability:.2%})")

        self.update_stats()

    def reset_state(self):
        self.current_state = None
        self.is_collapsed = False
        self.start_time = time.time()

        self.cat_display.config(text="🐱", fg="#00ff41")
        self.quantum_state_label.config(text="SUPERPOSITION STATE")
        self.state_text.config(text="State: Unknown")
        self.decay_label.config(text="Decay: 0.0%")

        self.add_log("System reset. Wave function restored to superposition.")
        self.update_decay_display()

    def run_monte_carlo(self):
        if self.mc_running:
            self.add_log("Monte Carlo simulation already running!")
            return

        self.add_log("🎲 Starting Monte Carlo simulation (1000 iterations)...")
        self.monte_carlo_btn.config(state=tk.DISABLED)
        self.mc_running = True

        def simulate():
            sim_alive = 0
            sim_dead = 0

            # Get current decay factor for this simulation
            decay_factor = self.get_decay_factor()
            death_probability = 0.5 + decay_factor

            for batch in range(10):
                for _ in range(100):
                    # Use same probability calculation as observe_state
                    if random.random() >= death_probability:
                        sim_alive += 1
                        self.alive_results += 1
                    else:
                        sim_dead += 1
                        self.dead_results += 1

                    self.total_observations += 1

                completed = (batch + 1) * 100
                current_prob = (sim_alive / completed * 100)

                # Update ALL statistics in real-time
                self.root.after(0, self.update_stats)
                self.root.after(0, lambda p=current_prob: self.update_probability_bars(p))

                time.sleep(0.1)

            # Final results
            final_prob = (sim_alive / 1000 * 100)
            deviation = abs(50 - final_prob)

            theoretical = (1 - death_probability) * 100

            self.root.after(0, lambda: self.add_log(
                f"✅ Simulation complete: {sim_alive} alive, {sim_dead} dead"
            ))
            self.root.after(0, lambda: self.add_log(
                f"📊 Observed: {final_prob:.2f}% alive | Theoretical: {theoretical:.2f}% alive"
            ))
            self.root.after(0, lambda: self.add_log(
                f"🎯 Deviation from theoretical: {abs(final_prob - theoretical):.2f}%"
            ))

            if decay_factor > 0:
                self.root.after(0, lambda: self.add_log(
                    f"⏱️ Decay factor applied: +{decay_factor*100:.1f}% death probability"
                ))

            self.root.after(0, lambda: self.monte_carlo_btn.config(state=tk.NORMAL))
            self.mc_running = False

        # Run in separate thread
        Thread(target=simulate, daemon=True).start()

    def update_probability_bars(self, alive_prob):
        dead_prob = 100 - alive_prob

        self.alive_prob_label.config(text=f"{alive_prob:.2f}%")
        self.dead_prob_label.config(text=f"{dead_prob:.2f}%")
        self.alive_progress.config(value=alive_prob)
        self.dead_progress.config(value=dead_prob)

def main():
    root = tk.Tk()
    app = QuantumSimulator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
