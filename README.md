# 3-profesor-debat-code

# ⚛️ Quantum State Simulator

**Schrödinger's Cat - Enhanced Monte Carlo Wave Function Collapse**

Simulasi interaktif yang memvisualisasikan konsep superposisi kuantum dan wave function collapse menggunakan eksperimen pemikiran terkenal Schrödinger's Cat.

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## 🎯 Fitur

- **Visualisasi Wave Function**: Gelombang kuantum real-time yang merepresentasikan superposisi
- **Wave Function Collapse**: Observasi menyebabkan collapse ke state definitif
- **Monte Carlo Simulation**: Jalankan 1000 iterasi untuk validasi probabilitas
- **Quantum Decay Mode**: Simulasi peluruhan radioaktif yang meningkatkan probabilitas kematian
- **Real-time Statistics**: Tracking lengkap hasil observasi dan probabilitas
- **Terminal Log**: Output detail setiap event kuantum

## 📸 Screenshot

```
┌─────────────────────────────────────────────────────────┐
│        ⚛️ QUANTUM STATE SIMULATOR                       │
│   Schrödinger's Cat - Monte Carlo Wave Function        │
├──────────────────────┬──────────────────────────────────┤
│                      │  📊 Probability Distribution     │
│   SUPERPOSITION      │                                  │
│         🐱           │  😺 Alive    [████████░░] 50%    │
│                      │  💀 Dead     [████████░░] 50%    │
│   State: Unknown     │                                  │
└──────────────────────┴──────────────────────────────────┘
│        ～～～～Wave Function～～～～                    │
└─────────────────────────────────────────────────────────┘
```

## 🚀 Instalasi

### Prasyarat

Python 3.6 atau lebih tinggi dengan Tkinter.

### Linux

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install python3-tk
```

**Fedora/RedHat:**
```bash
sudo dnf install python3-tkinter
```

**Arch Linux:**
```bash
sudo pacman -S tk
```

### macOS

Tkinter biasanya sudah termasuk dalam Python dari python.org. Jika belum:
```bash
brew install python-tk
```

### Windows

Tkinter biasanya sudah included dengan Python installer. Jika belum ada, reinstall Python dan centang opsi **"tcl/tk and IDLE"**.

## 💻 Cara Menjalankan

```bash
python quantum_simulator.py
```

atau

```bash
python3 quantum_simulator.py
```

## 🎮 Cara Penggunaan

### 1. Observasi State
- Klik tombol **👁️ OBSERVE** untuk mengamati kucing
- Wave function akan collapse ke state **ALIVE** 😺 atau **DEAD** 💀
- Setiap observasi dicatat dalam statistik

### 2. Reset System
- Klik **🔄 RESET** untuk mengembalikan sistem ke superposisi
- State kembali tidak pasti (unknown)
- Wave function terbentuk kembali

### 3. Monte Carlo Simulation
- Klik **🎲 MONTE CARLO (1000x)** untuk menjalankan 1000 simulasi
- Validasi probabilitas teoritis vs hasil observasi
- Melihat konvergensi ke distribusi yang diharapkan

### 4. Decay Mode
- Aktifkan **⏱️ Decay Mode** untuk simulasi peluruhan radioaktif
- Probabilitas kematian meningkat seiring waktu (maksimal +30% dalam 60 detik)
- Mensimulasikan eksperimen asli dengan atom radioaktif

## 🧪 Konsep Fisika Kuantum

### Superposisi
Sebelum observasi, kucing berada dalam **superposisi** - secara simultan hidup DAN mati. State ini direpresentasikan oleh wave function yang berosilasi.

### Wave Function Collapse
Saat dilakukan observasi, wave function **collapse** menjadi satu state definitif:
- **|ψ⟩ = α|alive⟩ + β|dead⟩** → **|alive⟩** atau **|dead⟩**

### Probabilitas
Dalam mode standar:
- P(alive) = 50%
- P(dead) = 50%

Dalam decay mode:
- P(dead) = 50% + decay_factor (max 80%)
- P(alive) = 50% - decay_factor (min 20%)

### Monte Carlo Method
Simulasi Monte Carlo memvalidasi hukum bilangan besar - dengan iterasi cukup banyak, frekuensi relatif konvergen ke probabilitas teoritis.

## 📊 Statistik yang Ditampilkan

- **Total Observations**: Jumlah total observasi
- **Alive Results**: Jumlah hasil alive
- **Dead Results**: Jumlah hasil dead
- **Alive Probability**: Probabilitas empiris based on hasil

## 🎨 Antarmuka

- **Dark theme** dengan aksen neon green (#00ff41)
- **Real-time wave visualization** menggunakan Canvas
- **Progress bars** untuk distribusi probabilitas
- **Terminal output** dengan timestamp
- **Responsive layout** dengan Tkinter

## 🔬 Aplikasi Edukatif

Simulator ini cocok untuk:
- 📚 Pembelajaran konsep mekanika kuantum
- 🎓 Demonstrasi di kelas fisika
- 🧑‍🔬 Eksperimen dengan probabilitas kuantum
- 💡 Memahami paradoks Schrödinger's Cat
- 📈 Visualisasi metode Monte Carlo

## 🛠️ Teknologi

- **Python 3.6+**
- **Tkinter**: GUI framework
- **Threading**: Untuk Monte Carlo simulation non-blocking
- **Math**: Wave function calculations
- **Random**: Quantum measurement simulation

## 📝 Catatan Penting

- Ini adalah **simulasi klasik** dari fenomena kuantum
- Quantum randomness di-simulate dengan pseudo-random number generator
- Wave function adalah representasi visual, bukan perhitungan matematis rigor
- Decay mode mensimulasikan peluruhan eksponensial sederhana

## 🤝 Kontribusi

Kontribusi selalu welcome! Beberapa ide pengembangan:

- [ ] Tambah mode multi-particle entanglement
- [ ] Implementasi Bloch sphere visualization
- [ ] Export data ke CSV untuk analisis statistik
- [ ] Quantum gate simulator
- [ ] Animation untuk measurement process

## 📄 Lisensi

MIT License - bebas digunakan untuk keperluan edukatif dan penelitian.

## 👨‍💻 Author

Dibuat dengan ⚛️ untuk edukasi mekanika kuantum

---

**"Until you observe it, the cat is both alive and dead at the same time."**  
*- Erwin Schrödinger*
