# 🚀 QuizApp v2.0

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-green?style=for-the-badge" alt="Platform">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Version-2.0-orange?style=for-the-badge" alt="Version">
</p>

<p align="center">
  <b>A futuristic, cross-platform quiz application built with Python</b><br>
  <i>Developed by <a href="https://github.com/noorhoorain44-ship-it">Noor Hoorain</a></i>
</p>

---

## ✨ Features

- 🎮 **Interactive Quiz Engine** - Beautiful terminal UI with animations and color coding
- 🔐 **User Authentication** - Secure registration and login system with password hashing
- 📝 **Custom Quiz Creation** - Build your own quizzes with custom questions and time limits
- 🏆 **Global Leaderboard** - Compete with others and track your rankings
- 📊 **User Profiles** - Track your progress, streaks, and best scores
- ⏱️ **Timed Quizzes** - Challenge yourself with time-limited quizzes
- 📤 **CSV Export** - Export your quiz results for external analysis
- 🎨 **Futuristic UI** - Neon-styled interface with progress bars and animations
- 🖥️ **Cross-Platform** - Works on Windows, Linux (including Kali), and macOS
- 🎯 **Switch-Case Menu** - Clean, intuitive menu system using Python 3.10+ match-case

## 📦 Installation

### Windows

1. **Download** the repository or clone it:
   ```bash
   git clone https://github.com/noorhoorain44-ship-it/quizapp.git
   cd quizapp
   ```

2. **Run the installer:**
   ```cmd
   install.bat
   ```

3. **Launch QuizApp:**
   - Double-click the **QuizApp** desktop icon, or
   - Run `QuizApp.bat` from the installation directory

### Linux / Kali Linux / macOS

1. **Download** the repository or clone it:
   ```bash
   git clone https://github.com/noorhoorain44-ship-it/quizapp.git
   cd quizapp
   ```

2. **Make the installer executable and run it:**
   ```bash
   chmod +x install.sh
   ./install.sh
   ```

3. **Launch QuizApp:**
   ```bash
   quizapp
   ```

### Manual Installation (Any Platform)

If you prefer manual installation, simply ensure you have **Python 3.10+** installed and run:

```bash
python quizapp.py
```

## 🖥️ System Requirements

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| Python | 3.8+ | 3.10+ |
| RAM | 512 MB | 1 GB |
| Storage | 50 MB | 100 MB |
| Terminal | Any modern terminal | Terminal with ANSI color support |

## 🎯 Usage

### Main Menu Options

| Option | Feature | Description |
|--------|---------|-------------|
| `1` | 🎮 Start Quiz | Choose from available quizzes and test your knowledge |
| `2` | ✨ Create Custom Quiz | Build your own quiz with custom questions |
| `3` | 👤 View Profile | Check your statistics and quiz history |
| `4` | 🏆 Leaderboard | See global rankings and top performers |
| `5` | 📤 Export Results | Export your results to CSV format |
| `6` | ℹ️ About | View application information |
| `7` | 🔄 Logout | Switch to a different account |
| `0` | ❌ Exit | Close the application |

### Quiz Categories

- 🐍 **Python Basics** - Test your fundamental Python knowledge
- 🔒 **Cybersecurity** - Essential security concepts and practices
- 🐧 **Linux Mastery** - Command-line skills and Linux fundamentals
- 🌐 **Web Development** - HTML, CSS, and JavaScript basics
- 📊 **Data Structures** - Core computer science concepts

## 🗂️ Project Structure

```
quizapp/
├── quizapp.py          # Main application file
├── install.sh          # Linux/macOS installer
├── install.bat         # Windows installer
├── README.md           # This file
├── LICENSE             # MIT License
├── .gitignore          # Git ignore rules
└── requirements.txt    # Python dependencies
```

## 🛠️ Built With

- **Python 3.10+** - Core language with match-case statements
- **Standard Library** - No external dependencies required!
  - `json` - Data persistence
  - `hashlib` - Password hashing
  - `csv` - Result exports
  - `pathlib` - Cross-platform paths
  - `datetime` - Time tracking
  - `platform` - OS detection

## 🐧 Kali Linux Special Features

QuizApp is optimized for Kali Linux and penetration testing environments:

- ✅ Automatic Kali Linux detection
- ✅ Compatible with Kali's default Python installation
- ✅ Stores data in `~/.config/quizapp/` (XDG compliant)
- ✅ Works in both GUI terminal and TTY modes
- ✅ Includes cybersecurity quiz category

## 🎨 Customization

### Adding Custom Quizzes

You can add custom quizzes through the in-app menu (Option 2) or by editing the `DEFAULT_QUIZZES` dictionary in `quizapp.py`.

Example quiz format:
```python
"my_quiz": {
    "title": "My Custom Quiz",
    "description": "A description",
    "category": "Custom",
    "difficulty": "Beginner",
    "time_limit": 300,
    "questions": [
        {
            "question": "What is...?",
            "options": ["A", "B", "C", "D"],
            "correct": 0,
            "explanation": "Because..."
        }
    ]
}
```

## 📊 Data Storage

QuizApp stores all data locally in platform-appropriate directories:

| Platform | Data Directory |
|----------|---------------|
| Windows | `%LOCALAPPDATA%\QuizApp\` |
| Linux/Kali | `~/.config/quizapp/` |
| macOS | `~/Library/Application Support/QuizApp/` |

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Contribution Ideas

- 🌍 Add more quiz categories
- 🌐 Add multi-language support
- 🎨 Add more color themes
- 📱 Add mobile compatibility
- 🔊 Add sound effects
- 🤖 Add AI-powered quiz generation

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by modern CLI applications
- Built with love for the open-source community
- Special thanks to all contributors and users

## 📞 Support

- 🐛 **Bug Reports:** [GitHub Issues](https://github.com/noorhoorain44-ship-it/quizapp/issues)
- 💡 **Feature Requests:** [GitHub Discussions](https://github.com/noorhoorain44-ship-it/quizapp/discussions)
- 📧 **Email:** Contact through GitHub

## 👨‍💻 Developer

<p align="center">
  <b>Noor Hoorain</b><br>
  <a href="https://github.com/noorhoorain44-ship-it">GitHub: @noorhoorain44-ship-it</a><br>
  <i>Building the future, one line of code at a time.</i>
</p>

---

<p align="center">
  ⭐ Star this repository if you find it useful!<br>
  🍴 Fork it to create your own version!<br>
  ❤️ Made with passion by Noor Hoorain
</p>
