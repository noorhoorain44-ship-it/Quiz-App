#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ██████╗ ██╗   ██╗██╗███████╗███████╗ █████╗ ██████╗ ██████╗               ║
║  ██╔═══██╗██║   ██║██║╚══███╔╝╚══███╔╝██╔══██╗██╔══██╗██╔══██╗              ║
║  ██║   ██║██║   ██║██║  ███╔╝   ███╔╝ ███████║██████╔╝██████╔╝              ║
║  ██║▄▄ ██║██║   ██║██║ ███╔╝   ███╔╝  ██╔══██║██╔═══╝ ██╔═══╝               ║
║  ╚██████╔╝╚██████╔╝██║███████╗███████╗██║  ██║██║     ██║                    ║
║   ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝                    ║
║                                                                              ║
║              🚀 FUTURISTIC QUIZ APPLICATION v2.0 🚀                          ║
║                                                                              ║
║   Developed by: Noor Hoorain                                                 ║
║   GitHub: https://github.com/noorhoorain44-ship-it                           ║
║   License: MIT                                                               ║
║   Platform: Cross-Platform (Windows, Linux, macOS)                           ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import json
import random
import time
import datetime
import platform
import getpass
import hashlib
import csv
from pathlib import Path

# ═══════════════════════════════════════════════════════════════════════════════
# COLOR & STYLE CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

class Colors:
    """ANSI color codes for terminal styling"""
    # Standard Colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    # Bright Colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

    # Styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    STRIKETHROUGH = '\033[9m'

    # Background Colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

    # Reset
    RESET = '\033[0m'

    # Gradient-like combinations
    HEADER = BOLD + CYAN
    SUCCESS = BOLD + GREEN
    ERROR = BOLD + RED
    WARNING = BOLD + YELLOW
    INFO = BOLD + BLUE
    HIGHLIGHT = BOLD + MAGENTA
    NEON = BOLD + BRIGHT_CYAN

# ═══════════════════════════════════════════════════════════════════════════════
# PLATFORM DETECTION & COMPATIBILITY
# ═══════════════════════════════════════════════════════════════════════════════

class PlatformManager:
    """Handles platform-specific operations"""

    @staticmethod
    def get_platform():
        return platform.system().lower()

    @staticmethod
    def is_windows():
        return PlatformManager.get_platform() == 'windows'

    @staticmethod
    def is_linux():
        return PlatformManager.get_platform() == 'linux'

    @staticmethod
    def is_macos():
        return PlatformManager.get_platform() == 'darwin'

    @staticmethod
    def is_kali():
        if not PlatformManager.is_linux():
            return False
        try:
            with open('/etc/os-release', 'r') as f:
                return 'kali' in f.read().lower()
        except:
            return False

    @staticmethod
    def clear_screen():
        if PlatformManager.is_windows():
            os.system('cls')
        else:
            os.system('clear')

    @staticmethod
    def get_data_dir():
        """Get platform-appropriate data directory"""
        home = Path.home()
        if PlatformManager.is_windows():
            return home / 'AppData' / 'Local' / 'QuizApp'
        elif PlatformManager.is_macos():
            return home / 'Library' / 'Application Support' / 'QuizApp'
        else:
            return home / '.config' / 'quizapp'

    @staticmethod
    def setup_directories():
        """Create necessary directories"""
        data_dir = PlatformManager.get_data_dir()
        dirs = [
            data_dir,
            data_dir / 'users',
            data_dir / 'quizzes',
            data_dir / 'results',
            data_dir / 'exports'
        ]
        for d in dirs:
            d.mkdir(parents=True, exist_ok=True)
        return data_dir

# ═══════════════════════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def print_banner():
    """Display the application banner"""
    banner = f"""
{Colors.NEON}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.RESET}                                                                              {Colors.NEON}║
║{Colors.BRIGHT_CYAN}   ██████╗ ██╗   ██╗██╗███████╗███████╗ █████╗ ██████╗ ██████╗               {Colors.NEON}║
║{Colors.BRIGHT_CYAN}  ██╔═══██╗██║   ██║██║╚══███╔╝╚══███╔╝██╔══██╗██╔══██╗██╔══██╗              {Colors.NEON}║
║{Colors.BRIGHT_CYAN}  ██║   ██║██║   ██║██║  ███╔╝   ███╔╝ ███████║██████╔╝██████╔╝              {Colors.NEON}║
║{Colors.BRIGHT_CYAN}  ██║▄▄ ██║██║   ██║██║ ███╔╝   ███╔╝  ██╔══██║██╔═══╝ ██╔═══╝               {Colors.NEON}║
║{Colors.BRIGHT_CYAN}  ╚██████╔╝╚██████╔╝██║███████╗███████╗██║  ██║██║     ██║                    {Colors.NEON}║
║{Colors.BRIGHT_CYAN}   ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝                    {Colors.NEON}║
║{Colors.RESET}                                                                              {Colors.NEON}║
║{Colors.BRIGHT_GREEN}              🚀 FUTURISTIC QUIZ APPLICATION v2.0 🚀                          {Colors.NEON}║
║{Colors.RESET}                                                                              {Colors.NEON}║
║{Colors.BRIGHT_YELLOW}   Developed by: Noor Hoorain                                                 {Colors.NEON}║
║{Colors.BRIGHT_YELLOW}   GitHub: https://github.com/noorhoorain44-ship-it                           {Colors.NEON}║
║{Colors.BRIGHT_YELLOW}   Platform: {platform.system()} {platform.release()}                                    {Colors.NEON}║
║{Colors.RESET}                                                                              {Colors.NEON}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
    """
    print(banner)

def typewriter_effect(text, delay=0.02):
    """Print text with typewriter effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def loading_animation(text="Loading", duration=1.5):
    """Show loading animation"""
    chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        print(f"\r{Colors.CYAN}{chars[i % len(chars)]} {text}...{Colors.RESET}", end='', flush=True)
        time.sleep(0.1)
        i += 1
    print(f"\r{Colors.GREEN}✓ {text} Complete!{Colors.RESET}      ")

def print_separator(char='═', length=80, color=Colors.CYAN):
    """Print a decorative separator line"""
    print(f"{color}{char * length}{Colors.RESET}")

def print_box(text, width=60, color=Colors.CYAN):
    """Print text in a box"""
    padding = (width - len(text) - 2) // 2
    print(f"{color}╔{'═' * (width-2)}╗{Colors.RESET}")
    print(f"{color}║{' ' * padding}{Colors.BOLD}{text}{Colors.RESET}{' ' * (width - len(text) - 2 - padding)}{color}║{Colors.RESET}")
    print(f"{color}╚{'═' * (width-2)}╝{Colors.RESET}")

def get_input(prompt, color=Colors.BRIGHT_CYAN):
    """Get user input with styling"""
    return input(f"{color}➤ {prompt}{Colors.RESET}")

def confirm(prompt):
    """Ask for confirmation"""
    response = get_input(f"{prompt} (y/n): ").lower().strip()
    return response in ['y', 'yes', '1', 'true']

def hash_password(password):
    """Hash password for secure storage"""
    return hashlib.sha256(password.encode()).hexdigest()

# ═══════════════════════════════════════════════════════════════════════════════
# DEFAULT QUIZ DATABASE
# ═══════════════════════════════════════════════════════════════════════════════

DEFAULT_QUIZZES = {
    "python_basics": {
        "title": "🐍 Python Basics",
        "description": "Test your fundamental Python knowledge",
        "category": "Programming",
        "difficulty": "Beginner",
        "time_limit": 300,
        "questions": [
            {
                "question": "What is the output of: print(type([]))",
                "options": ["<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'set'>"],
                "correct": 0,
                "explanation": "[] creates an empty list in Python."
            },
            {
                "question": "Which of these is NOT a valid Python data type?",
                "options": ["int", "str", "array", "float"],
                "correct": 2,
                "explanation": "Python has 'list' not 'array' as a built-in type (though arrays exist in the array module)."
            },
            {
                "question": "What does the 'len()' function do?",
                "options": ["Returns the length of an object", "Converts to lowercase", "Creates a list", "None of these"],
                "correct": 0,
                "explanation": "len() returns the number of items in an object."
            },
            {
                "question": "How do you create a function in Python?",
                "options": ["function myFunc():", "def myFunc():", "create myFunc():", "func myFunc():"],
                "correct": 1,
                "explanation": "Functions are defined using the 'def' keyword in Python."
            },
            {
                "question": "What is the correct file extension for Python files?",
                "options": [".pt", ".pyt", ".py", ".python"],
                "correct": 2,
                "explanation": "Python files use the .py extension."
            }
        ]
    },
    "cybersecurity": {
        "title": "🔒 Cybersecurity Fundamentals",
        "description": "Essential cybersecurity concepts and practices",
        "category": "Security",
        "difficulty": "Intermediate",
        "time_limit": 420,
        "questions": [
            {
                "question": "What does SQL stand for?",
                "options": ["Structured Query Language", "Simple Query Language", "Standard Query Language", "System Query Language"],
                "correct": 0,
                "explanation": "SQL stands for Structured Query Language."
            },
            {
                "question": "Which attack involves injecting malicious scripts into web pages?",
                "options": ["SQL Injection", "XSS (Cross-Site Scripting)", "CSRF", "DDoS"],
                "correct": 1,
                "explanation": "XSS involves injecting client-side scripts into web pages."
            },
            {
                "question": "What is the purpose of a VPN?",
                "options": ["Increase internet speed", "Encrypt internet connection", "Block ads", "Store passwords"],
                "correct": 1,
                "explanation": "VPN encrypts your internet connection for privacy and security."
            },
            {
                "question": "What does HTTPS stand for?",
                "options": ["Hyper Text Transfer Protocol Secure", "High Transfer Text Protocol", "Hyper Text Transport Protocol", "None"],
                "correct": 0,
                "explanation": "HTTPS is the secure version of HTTP using SSL/TLS encryption."
            },
            {
                "question": "Which is a strong password practice?",
                "options": ["Using your birthday", "Using the same password everywhere", "Using a mix of characters, numbers, symbols", "Using 'password123'"],
                "correct": 2,
                "explanation": "Strong passwords use a mix of uppercase, lowercase, numbers, and symbols."
            }
        ]
    },
    "linux_mastery": {
        "title": "🐧 Linux Mastery",
        "description": "Test your Linux command-line skills",
        "category": "Operating Systems",
        "difficulty": "Advanced",
        "time_limit": 360,
        "questions": [
            {
                "question": "Which command is used to change file permissions?",
                "options": ["chown", "chmod", "chgrp", "perm"],
                "correct": 1,
                "explanation": "chmod is used to change file permissions in Linux."
            },
            {
                "question": "What does 'sudo' stand for?",
                "options": ["Super User Do", "System User Do", "Switch User Do", "Superuser Operation"],
                "correct": 0,
                "explanation": "sudo stands for 'Super User Do' - execute commands as superuser."
            },
            {
                "question": "Which command shows disk usage?",
                "options": ["df", "du", "disk", "usage"],
                "correct": 1,
                "explanation": "du (disk usage) shows directory space usage."
            },
            {
                "question": "What is the purpose of the 'grep' command?",
                "options": ["Copy files", "Search text using patterns", "List directories", "Create files"],
                "correct": 1,
                "explanation": "grep searches for patterns within text files."
            },
            {
                "question": "Which signal number is used to force kill a process?",
                "options": ["1 (SIGHUP)", "9 (SIGKILL)", "15 (SIGTERM)", "2 (SIGINT)"],
                "correct": 1,
                "explanation": "SIGKILL (9) forcefully terminates a process without cleanup."
            }
        ]
    },
    "web_development": {
        "title": "🌐 Web Development",
        "description": "HTML, CSS, and JavaScript fundamentals",
        "category": "Web",
        "difficulty": "Beginner",
        "time_limit": 300,
        "questions": [
            {
                "question": "What does HTML stand for?",
                "options": ["Hyper Text Markup Language", "High Tech Modern Language", "Hyper Transfer Markup Language", "None"],
                "correct": 0,
                "explanation": "HTML = HyperText Markup Language."
            },
            {
                "question": "Which CSS property changes text color?",
                "options": ["text-color", "font-color", "color", "foreground"],
                "correct": 2,
                "explanation": "The 'color' property sets text color in CSS."
            },
            {
                "question": "What is the correct way to declare a JavaScript variable?",
                "options": ["var name;", "variable name;", "v name;", "declare name;"],
                "correct": 0,
                "explanation": "Variables are declared using var, let, or const in JavaScript."
            },
            {
                "question": "Which HTML tag is used for the largest heading?",
                "options": ["<heading>", "<h6>", "<head>", "<h1>"],
                "correct": 3,
                "explanation": "<h1> is the largest heading tag in HTML."
            },
            {
                "question": "What does DOM stand for?",
                "options": ["Document Object Model", "Data Object Model", "Digital Object Model", "None"],
                "correct": 0,
                "explanation": "DOM = Document Object Model, representing the page structure."
            }
        ]
    },
    "data_structures": {
        "title": "📊 Data Structures & Algorithms",
        "description": "Core computer science concepts",
        "category": "Computer Science",
        "difficulty": "Advanced",
        "time_limit": 480,
        "questions": [
            {
                "question": "What is the time complexity of binary search?",
                "options": ["O(n)", "O(log n)", "O(n²)", "O(1)"],
                "correct": 1,
                "explanation": "Binary search has O(log n) time complexity."
            },
            {
                "question": "Which data structure uses LIFO?",
                "options": ["Queue", "Stack", "Linked List", "Tree"],
                "correct": 1,
                "explanation": "Stack follows Last In First Out (LIFO) principle."
            },
            {
                "question": "What is the worst-case time complexity of QuickSort?",
                "options": ["O(n log n)", "O(n²)", "O(n)", "O(log n)"],
                "correct": 1,
                "explanation": "QuickSort's worst case is O(n²) when pivot selection is poor."
            },
            {
                "question": "Which traversal visits root before children?",
                "options": ["In-order", "Post-order", "Pre-order", "Level-order"],
                "correct": 2,
                "explanation": "Pre-order traversal visits root, then left, then right."
            },
            {
                "question": "What data structure is used in BFS?",
                "options": ["Stack", "Queue", "Heap", "Tree"],
                "correct": 1,
                "explanation": "BFS (Breadth-First Search) uses a Queue data structure."
            }
        ]
    }
}

# ═══════════════════════════════════════════════════════════════════════════════
# DATA MANAGER
# ═══════════════════════════════════════════════════════════════════════════════

class DataManager:
    """Manages all data persistence operations"""

    def __init__(self):
        self.data_dir = PlatformManager.setup_directories()
        self.users_file = self.data_dir / 'users' / 'users.json'
        self.results_file = self.data_dir / 'results' / 'results.json'
        self.quizzes_file = self.data_dir / 'quizzes' / 'custom_quizzes.json'
        self._ensure_defaults()

    def _ensure_defaults(self):
        """Ensure default data files exist"""
        if not self.users_file.exists():
            self._save_json(self.users_file, {})
        if not self.results_file.exists():
            self._save_json(self.results_file, [])
        if not self.quizzes_file.exists():
            self._save_json(self.quizzes_file, {})

    def _load_json(self, filepath):
        """Load JSON data from file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _save_json(self, filepath, data):
        """Save data to JSON file"""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    # User Management
    def register_user(self, username, password):
        """Register a new user"""
        users = self._load_json(self.users_file)
        if username in users:
            return False, "Username already exists!"
        users[username] = {
            "password": hash_password(password),
            "created_at": datetime.datetime.now().isoformat(),
            "total_quizzes": 0,
            "total_score": 0,
            "best_score": 0,
            "streak": 0,
            "last_active": datetime.datetime.now().isoformat()
        }
        self._save_json(self.users_file, users)
        return True, "Registration successful!"

    def authenticate_user(self, username, password):
        """Authenticate user credentials"""
        users = self._load_json(self.users_file)
        if username not in users:
            return False, "User not found!"
        if users[username]["password"] != hash_password(password):
            return False, "Incorrect password!"
        users[username]["last_active"] = datetime.datetime.now().isoformat()
        self._save_json(self.users_file, users)
        return True, "Login successful!"

    def get_user_stats(self, username):
        """Get user statistics"""
        users = self._load_json(self.users_file)
        return users.get(username, {})

    def update_user_stats(self, username, score, max_score):
        """Update user statistics after quiz"""
        users = self._load_json(self.users_file)
        if username not in users:
            return
        users[username]["total_quizzes"] += 1
        users[username]["total_score"] += score
        percentage = (score / max_score) * 100
        if percentage > users[username].get("best_score", 0):
            users[username]["best_score"] = percentage
        users[username]["streak"] += 1
        self._save_json(self.users_file, users)

    # Quiz Management
    def get_all_quizzes(self):
        """Get all available quizzes (default + custom)"""
        custom = self._load_json(self.quizzes_file)
        all_quizzes = {**DEFAULT_QUIZZES, **custom}
        return all_quizzes

    def get_quiz(self, quiz_id):
        """Get specific quiz by ID"""
        all_quizzes = self.get_all_quizzes()
        return all_quizzes.get(quiz_id)

    def save_custom_quiz(self, quiz_id, quiz_data):
        """Save a custom quiz"""
        custom = self._load_json(self.quizzes_file)
        custom[quiz_id] = quiz_data
        self._save_json(self.quizzes_file, custom)

    def delete_custom_quiz(self, quiz_id):
        """Delete a custom quiz"""
        custom = self._load_json(self.quizzes_file)
        if quiz_id in custom:
            del custom[quiz_id]
            self._save_json(self.quizzes_file, custom)
            return True
        return False

    # Results Management
    def save_result(self, result):
        """Save quiz result"""
        results = self._load_json(self.results_file)
        results.append(result)
        self._save_json(self.results_file, results)

    def get_user_results(self, username):
        """Get all results for a user"""
        results = self._load_json(self.results_file)
        return [r for r in results if r.get("username") == username]

    def get_leaderboard(self, limit=10):
        """Get global leaderboard"""
        results = self._load_json(self.results_file)
        if not results:
            return []

        # Calculate best scores per user
        user_best = {}
        for r in results:
            user = r["username"]
            score_pct = (r["score"] / r["max_score"]) * 100
            if user not in user_best or score_pct > user_best[user]["percentage"]:
                user_best[user] = {
                    "username": user,
                    "percentage": score_pct,
                    "quiz": r["quiz_title"],
                    "date": r["date"]
                }

        leaderboard = sorted(user_best.values(), key=lambda x: x["percentage"], reverse=True)
        return leaderboard[:limit]

    def export_results_csv(self, username=None):
        """Export results to CSV"""
        results = self._load_json(self.results_file)
        if username:
            results = [r for r in results if r.get("username") == username]

        if not results:
            return None

        export_path = self.data_dir / 'exports' / f'results_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'

        with open(export_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["username", "quiz_title", "score", "max_score", "percentage", "time_taken", "date"])
            writer.writeheader()
            for r in results:
                writer.writerow(r)

        return str(export_path)

# ═══════════════════════════════════════════════════════════════════════════════
# QUIZ ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

class QuizEngine:
    """Core quiz logic and execution"""

    def __init__(self, data_manager):
        self.dm = data_manager
        self.current_user = None

    def login(self):
        """User login flow"""
        print(f"\n{Colors.HEADER}╔══════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.HEADER}║         🔐 USER LOGIN               ║{Colors.RESET}")
        print(f"{Colors.HEADER}╚══════════════════════════════════════╝{Colors.RESET}\n")

        username = get_input("Enter username: ")
        password = getpass.getpass(f"{Colors.BRIGHT_CYAN}➤ Enter password: {Colors.RESET}")

        success, message = self.dm.authenticate_user(username, password)
        if success:
            self.current_user = username
            print(f"\n{Colors.SUCCESS}✅ {message}{Colors.RESET}")
            loading_animation("Loading dashboard")
            return True
        else:
            print(f"\n{Colors.ERROR}❌ {message}{Colors.RESET}")
            return False

    def register(self):
        """User registration flow"""
        print(f"\n{Colors.HEADER}╔══════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.HEADER}║        📝 USER REGISTRATION         ║{Colors.RESET}")
        print(f"{Colors.HEADER}╚══════════════════════════════════════╝{Colors.RESET}\n")

        username = get_input("Choose username: ")
        if len(username) < 3:
            print(f"{Colors.ERROR}❌ Username must be at least 3 characters!{Colors.RESET}")
            return False

        password = getpass.getpass(f"{Colors.BRIGHT_CYAN}➤ Choose password: {Colors.RESET}")
        if len(password) < 4:
            print(f"{Colors.ERROR}❌ Password must be at least 4 characters!{Colors.RESET}")
            return False

        confirm_pass = getpass.getpass(f"{Colors.BRIGHT_CYAN}➤ Confirm password: {Colors.RESET}")
        if password != confirm_pass:
            print(f"{Colors.ERROR}❌ Passwords don't match!{Colors.RESET}")
            return False

        success, message = self.dm.register_user(username, password)
        if success:
            print(f"\n{Colors.SUCCESS}✅ {message}{Colors.RESET}")
            print(f"{Colors.INFO}ℹ️  You can now login with your credentials.{Colors.RESET}")
            return True
        else:
            print(f"\n{Colors.ERROR}❌ {message}{Colors.RESET}")
            return False

    def display_quiz_menu(self):
        """Display available quizzes"""
        quizzes = self.dm.get_all_quizzes()

        print(f"\n{Colors.HEADER}╔══════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.HEADER}║       📚 AVAILABLE QUIZZES          ║{Colors.RESET}")
        print(f"{Colors.HEADER}╚══════════════════════════════════════╝{Colors.RESET}\n")

        quiz_list = list(quizzes.items())
        for idx, (quiz_id, quiz) in enumerate(quiz_list, 1):
            diff_color = Colors.GREEN if quiz["difficulty"] == "Beginner" else (Colors.YELLOW if quiz["difficulty"] == "Intermediate" else Colors.RED)
            print(f"{Colors.BRIGHT_CYAN}[{idx}]{Colors.RESET} {Colors.BOLD}{quiz['title']}{Colors.RESET}")
            print(f"    {Colors.DIM}Description:{Colors.RESET} {quiz['description']}")
            print(f"    {Colors.DIM}Category:{Colors.RESET} {quiz['category']} | {Colors.DIM}Difficulty:{Colors.RESET} {diff_color}{quiz['difficulty']}{Colors.RESET}")
            print(f"    {Colors.DIM}Questions:{Colors.RESET} {len(quiz['questions'])} | {Colors.DIM}Time Limit:{Colors.RESET} {quiz['time_limit']//60}m {quiz['time_limit']%60}s")
            print()

        return quiz_list

    def run_quiz(self, quiz_id, quiz_data):
        """Execute a quiz session"""
        questions = quiz_data["questions"].copy()
        random.shuffle(questions)

        print(f"\n{Colors.HEADER}╔══════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.HEADER}║  🎯 STARTING: {quiz_data['title'][:25]:25}║{Colors.RESET}")
        print(f"{Colors.HEADER}╚══════════════════════════════════════╝{Colors.RESET}\n")

        print(f"{Colors.INFO}📋 Rules:{Colors.RESET}")
        print(f"   • {len(questions)} questions")
        print(f"   • Time limit: {quiz_data['time_limit']//60} minutes")
        print(f"   • +1 point per correct answer")
        print(f"   • No negative marking")
        print()

        if not confirm("Ready to start?"):
            print(f"{Colors.WARNING}⚠️  Quiz cancelled.{Colors.RESET}")
            return

        score = 0
        max_score = len(questions)
        start_time = time.time()
        answers_record = []

        for idx, q in enumerate(questions, 1):
            PlatformManager.clear_screen()
            print_banner()

            elapsed = time.time() - start_time
            remaining = quiz_data["time_limit"] - elapsed

            if remaining <= 0:
                print(f"\n{Colors.ERROR}⏰ TIME'S UP!{Colors.RESET}")
                break

            # Progress bar
            progress = int((idx / len(questions)) * 30)
            bar = f"{Colors.GREEN}{'█' * progress}{Colors.DIM}{'░' * (30 - progress)}{Colors.RESET}"
            print(f"\n{Colors.BRIGHT_CYAN}Question {idx}/{len(questions)} {bar} {Colors.YELLOW}⏱️  {int(remaining//60)}:{int(remaining%60):02d}{Colors.RESET}\n")

            print(f"{Colors.BOLD}{q['question']}{Colors.RESET}\n")

            for opt_idx, option in enumerate(q["options"]):
                labels = ['A', 'B', 'C', 'D']
                print(f"   {Colors.BRIGHT_YAN}[{labels[opt_idx]}]{Colors.RESET} {option}")

            print()

            # Get answer with validation
            valid_answers = ['a', 'b', 'c', 'd', '1', '2', '3', '4']
            while True:
                answer = get_input("Your answer (A/B/C/D or 1/2/3/4): ").lower().strip()
                if answer in valid_answers:
                    break
                print(f"{Colors.ERROR}❌ Invalid input! Use A/B/C/D or 1/2/3/4{Colors.RESET}")

            # Convert to index
            answer_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, '1': 0, '2': 1, '3': 2, '4': 3}
            user_answer = answer_map[answer]
            is_correct = user_answer == q["correct"]

            if is_correct:
                score += 1
                print(f"\n{Colors.SUCCESS}✅ CORRECT!{Colors.RESET}")
            else:
                correct_label = ['A', 'B', 'C', 'D'][q["correct"]]
                print(f"\n{Colors.ERROR}❌ WRONG! Correct answer: {Colors.BRIGHT_GREEN}{correct_label}{Colors.RESET}")

            print(f"{Colors.DIM}💡 {q['explanation']}{Colors.RESET}")
            answers_record.append({
                "question": q["question"],
                "user_answer": user_answer,
                "correct_answer": q["correct"],
                "is_correct": is_correct
            })

            if idx < len(questions):
                input(f"\n{Colors.DIM}Press Enter for next question...{Colors.RESET}")

        total_time = time.time() - start_time

        # Show results
        PlatformManager.clear_screen()
        print_banner()

        percentage = (score / max_score) * 100

        print(f"\n{Colors.HEADER}╔══════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.HEADER}║           🏆 QUIZ RESULTS           ║{Colors.RESET}")
        print(f"{Colors.HEADER}╚══════════════════════════════════════╝{Colors.RESET}\n")

        # Score display with color coding
        if percentage >= 80:
            grade_color = Colors.BRIGHT_GREEN
            grade = "EXCELLENT! 🌟"
        elif percentage >= 60:
            grade_color = Colors.BRIGHT_YELLOW
            grade = "GOOD JOB! 👍"
        elif percentage >= 40:
            grade_color = Colors.BRIGHT_MAGENTA
            grade = "KEEP PRACTICING! 📚"
        else:
            grade_color = Colors.BRIGHT_RED
            grade = "NEED MORE PRACTICE! 💪"

        print(f"{Colors.BOLD}Quiz:{Colors.RESET} {quiz_data['title']}")
        print(f"{Colors.BOLD}Score:{Colors.RESET} {grade_color}{score}/{max_score} ({percentage:.1f}%){Colors.RESET}")
        print(f"{Colors.BOLD}Grade:{Colors.RESET} {grade_color}{grade}{Colors.RESET}")
        print(f"{Colors.BOLD}Time:{Colors.RESET} {int(total_time//60)}m {int(total_time%60)}s")
        print()

        # Answer review
        print(f"{Colors.HEADER}📊 Answer Review:{Colors.RESET}")
        for i, record in enumerate(answers_record, 1):
            status = f"{Colors.GREEN}✓{Colors.RESET}" if record["is_correct"] else f"{Colors.RED}✗{Colors.RESET}"
            print(f"   Q{i}: {status}")

        # Save result
        result = {
            "username": self.current_user,
            "quiz_id": quiz_id,
            "quiz_title": quiz_data["title"],
            "score": score,
            "max_score": max_score,
            "percentage": percentage,
            "time_taken": int(total_time),
            "date": datetime.datetime.now().isoformat()
        }
        self.dm.save_result(result)
        self.dm.update_user_stats(self.current_user, score, max_score)

        print(f"\n{Colors.SUCCESS}✅ Result saved successfully!{Colors.RESET}")
        input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")

    def create_custom_quiz(self):
        """Create a custom quiz"""
        print(f"\n{Colors.HEADER}╔══════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.HEADER}║      ✨ CREATE CUSTOM QUIZ          ║{Colors.RESET}")
        print(f"{Colors.HEADER}╚══════════════════════════════════════╝{Colors.RESET}\n")

        quiz_id = get_input("Quiz ID (no spaces, lowercase): ").lower().replace(" ", "_")
        if not quiz_id:
            print(f"{Colors.ERROR}❌ Quiz ID cannot be empty!{Colors.RESET}")
            return

        title = get_input("Quiz Title: ")
        description = get_input("Description: ")
        category = get_input("Category: ")

        print(f"\n{Colors.INFO}Difficulty:{Colors.RESET}")
        print("  [1] Beginner")
        print("  [2] Intermediate")
        print("  [3] Advanced")
        diff_choice = get_input("Choose (1-3): ")
        difficulty = {"1": "Beginner", "2": "Intermediate", "3": "Advanced"}.get(diff_choice, "Beginner")

        time_limit = int(get_input("Time limit (seconds, e.g., 300 for 5 min): ") or "300")

        questions = []
        print(f"\n{Colors.INFO}Add questions (minimum 1, type 'done' when finished):{Colors.RESET}\n")

        q_num = 1
        while True:
            print(f"{Colors.BRIGHT_CYAN}--- Question {q_num} ---{Colors.RESET}")
            question_text = get_input("Question: ")
            if question_text.lower() == 'done' and q_num > 1:
                break
            if not question_text:
                print(f"{Colors.ERROR}❌ Question cannot be empty!{Colors.RESET}")
                continue

            options = []
            for opt in ['A', 'B', 'C', 'D']:
                opt_text = get_input(f"Option {opt}: ")
                options.append(opt_text)

            correct = int(get_input("Correct answer (1-4): ")) - 1
            explanation = get_input("Explanation: ")

            questions.append({
                "question": question_text,
                "options": options,
                "correct": correct,
                "explanation": explanation
            })
            q_num += 1
            print()

        quiz_data = {
            "title": title,
            "description": description,
            "category": category,
            "difficulty": difficulty,
            "time_limit": time_limit,
            "questions": questions,
            "created_by": self.current_user,
            "created_at": datetime.datetime.now().isoformat()
        }

        self.dm.save_custom_quiz(quiz_id, quiz_data)
        print(f"\n{Colors.SUCCESS}✅ Custom quiz '{title}' created successfully!{Colors.RESET}")
        input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")

    def view_profile(self):
        """View user profile and statistics"""
        stats = self.dm.get_user_stats(self.current_user)
        results = self.dm.get_user_results(self.current_user)

        print(f"\n{Colors.HEADER}╔══════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.HEADER}║         👤 USER PROFILE             ║{Colors.RESET}")
        print(f"{Colors.HEADER}╚══════════════════════════════════════╝{Colors.RESET}\n")

        print(f"{Colors.BOLD}Username:{Colors.RESET} {Colors.BRIGHT_CYAN}{self.current_user}{Colors.RESET}")
        print(f"{Colors.BOLD}Member Since:{Colors.RESET} {stats.get('created_at', 'N/A')[:10]}")
        print(f"{Colors.BOLD}Total Quizzes Taken:{Colors.RESET} {stats.get('total_quizzes', 0)}")
        print(f"{Colors.BOLD}Best Score:{Colors.RESET} {Colors.BRIGHT_GREEN}{stats.get('best_score', 0):.1f}%{Colors.RESET}")
        print(f"{Colors.BOLD}Current Streak:{Colors.RESET} {stats.get('streak', 0)} quizzes")
        print()

        if results:
            print(f"{Colors.HEADER}📜 Recent Activity:{Colors.RESET}")
            for r in reversed(results[-5:]):
                date = r['date'][:10]
                pct = (r['score'] / r['max_score']) * 100
                color = Colors.GREEN if pct >= 60 else Colors.RED
                print(f"   {date} | {r['quiz_title'][:25]:25} | {color}{r['score']}/{r['max_score']} ({pct:.0f}%){Colors.RESET}")

        input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")

    def view_leaderboard(self):
        """Display global leaderboard"""
        leaderboard = self.dm.get_leaderboard()

        print(f"\n{Colors.HEADER}╔══════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.HEADER}║      🏆 GLOBAL LEADERBOARD          ║{Colors.RESET}")
        print(f"{Colors.HEADER}╚══════════════════════════════════════╝{Colors.RESET}\n")

        if not leaderboard:
            print(f"{Colors.WARNING}⚠️  No scores yet. Be the first!{Colors.RESET}")
        else:
            medals = ["🥇", "🥈", "🥉"]
            for i, entry in enumerate(leaderboard, 1):
                medal = medals[i-1] if i <= 3 else f"{i}."
                highlight = Colors.BRIGHT_YELLOW if entry["username"] == self.current_user else Colors.RESET
                print(f"{medal} {highlight}{entry['username'][:15]:15}{Colors.RESET} | {Colors.BRIGHT_GREEN}{entry['percentage']:.1f}%{Colors.RESET} | {entry['quiz'][:20]}")

        input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")

    def export_results(self):
        """Export results to CSV"""
        print(f"\n{Colors.HEADER}📤 EXPORT RESULTS{Colors.RESET}\n")
        print("[1] Export my results only")
        print("[2] Export all results (admin)")
        choice = get_input("Choose option: ")

        username = self.current_user if choice == "1" else None
        path = self.dm.export_results_csv(username)

        if path:
            print(f"\n{Colors.SUCCESS}✅ Results exported to:{Colors.RESET}")
            print(f"   {Colors.BRIGHT_CYAN}{path}{Colors.RESET}")
        else:
            print(f"\n{Colors.WARNING}⚠️  No results to export!{Colors.RESET}")

        input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN APPLICATION - SWITCH CASE MENU SYSTEM
# ═══════════════════════════════════════════════════════════════════════════════

class QuizApp:
    """Main Quiz Application with Switch-Case Menu System"""

    def __init__(self):
        self.dm = DataManager()
        self.engine = QuizEngine(self.dm)
        self.running = True

    def auth_menu(self):
        """Authentication Menu - Switch Case Pattern"""
        while not self.engine.current_user:
            PlatformManager.clear_screen()
            print_banner()

            print(f"\n{Colors.HEADER}╔══════════════════════════════════════╗{Colors.RESET}")
            print(f"{Colors.HEADER}║         🔐 AUTHENTICATION           ║{Colors.RESET}")
            print(f"{Colors.HEADER}╚══════════════════════════════════════╝{Colors.RESET}\n")

            print(f"{Colors.BRIGHT_CYAN}[1]{Colors.RESET} 📝 Login")
            print(f"{Colors.BRIGHT_CYAN}[2]{Colors.RESET} 🆕 Register")
            print(f"{Colors.BRIGHT_CYAN}[3]{Colors.RESET} 👤 Guest Mode (Limited)")
            print(f"{Colors.BRIGHT_CYAN}[0]{Colors.RESET} ❌ Exit")
            print()

            choice = get_input("Select option: ")

            # ═══════ SWITCH CASE FOR AUTH MENU ═══════
            match choice:
                case "1" | "login" | "l":
                    if self.engine.login():
                        return True
                    input(f"\n{Colors.DIM}Press Enter to try again...{Colors.RESET}")

                case "2" | "register" | "r":
                    if self.engine.register():
                        input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
                    else:
                        input(f"\n{Colors.DIM}Press Enter to try again...{Colors.RESET}")

                case "3" | "guest" | "g":
                    self.engine.current_user = "guest"
                    print(f"\n{Colors.WARNING}⚠️  Guest mode - Progress won't be saved!{Colors.RESET}")
                    input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
                    return True

                case "0" | "exit" | "q" | "quit":
                    self.shutdown()
                    return False

                case _:
                    print(f"\n{Colors.ERROR}❌ Invalid option! Please try again.{Colors.RESET}")
                    input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")

        return True

    def main_menu(self):
        """Main Application Menu - Switch Case Pattern"""
        while self.running:
            PlatformManager.clear_screen()
            print_banner()

            # Welcome message
            user_color = Colors.BRIGHT_GREEN if self.engine.current_user != "guest" else Colors.BRIGHT_YELLOW
            print(f"\n{Colors.DIM}Welcome back,{Colors.RESET} {user_color}{self.engine.current_user}{Colors.RESET} 👋")
            print()

            print(f"{Colors.HEADER}╔══════════════════════════════════════╗{Colors.RESET}")
            print(f"{Colors.HEADER}║          📋 MAIN MENU               ║{Colors.RESET}")
            print(f"{Colors.HEADER}╚══════════════════════════════════════╝{Colors.RESET}\n")

            print(f"{Colors.BRIGHT_CYAN}[1]{Colors.RESET} 🎮 Start Quiz")
            print(f"{Colors.BRIGHT_CYAN}[2]{Colors.RESET} ✨ Create Custom Quiz")
            print(f"{Colors.BRIGHT_CYAN}[3]{Colors.RESET} 👤 View Profile")
            print(f"{Colors.BRIGHT_CYAN}[4]{Colors.RESET} 🏆 Leaderboard")
            print(f"{Colors.BRIGHT_CYAN}[5]{Colors.RESET} 📤 Export Results")
            print(f"{Colors.BRIGHT_CYAN}[6]{Colors.RESET} ℹ️  About")
            print(f"{Colors.BRIGHT_CYAN}[7]{Colors.RESET} 🔄 Logout")
            print(f"{Colors.BRIGHT_CYAN}[0]{Colors.RESET} ❌ Exit")
            print()

            choice = get_input("Select option: ")

            # ═══════ SWITCH CASE FOR MAIN MENU ═══════
            match choice:
                case "1" | "start" | "play" | "quiz":
                    self.start_quiz_flow()

                case "2" | "create" | "custom":
                    if self.engine.current_user == "guest":
                        print(f"\n{Colors.ERROR}❌ Please login to create quizzes!{Colors.RESET}")
                        input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
                    else:
                        self.engine.create_custom_quiz()

                case "3" | "profile" | "stats":
                    if self.engine.current_user == "guest":
                        print(f"\n{Colors.ERROR}❌ Please login to view profile!{Colors.RESET}")
                        input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
                    else:
                        self.engine.view_profile()

                case "4" | "leaderboard" | "rank":
                    self.engine.view_leaderboard()

                case "5" | "export" | "save":
                    if self.engine.current_user == "guest":
                        print(f"\n{Colors.ERROR}❌ Please login to export results!{Colors.RESET}")
                        input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")
                    else:
                        self.engine.export_results()

                case "6" | "about" | "info":
                    self.show_about()

                case "7" | "logout" | "switch":
                    print(f"\n{Colors.WARNING}👋 Logging out...{Colors.RESET}")
                    self.engine.current_user = None
                    loading_animation("Cleaning up")
                    return

                case "0" | "exit" | "quit" | "q":
                    self.shutdown()

                case _:
                    print(f"\n{Colors.ERROR}❌ Invalid option! Please try again.{Colors.RESET}")
                    input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")

    def start_quiz_flow(self):
        """Quiz selection and execution flow"""
        quiz_list = self.engine.display_quiz_menu()

        print(f"{Colors.BRIGHT_CYAN}[0]{Colors.RESET} 🔙 Back to Main Menu")
        print()

        choice = get_input("Select quiz: ")

        # ═══════ SWITCH CASE FOR QUIZ SELECTION ═══════
        match choice:
            case "0" | "back" | "b":
                return

            case _ if choice.isdigit() and 1 <= int(choice) <= len(quiz_list):
                idx = int(choice) - 1
                quiz_id, quiz_data = quiz_list[idx]
                self.engine.run_quiz(quiz_id, quiz_data)

            case _:
                print(f"\n{Colors.ERROR}❌ Invalid selection!{Colors.RESET}")
                input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")

    def show_about(self):
        """Display application information"""
        print(f"\n{Colors.HEADER}╔══════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.HEADER}║         ℹ️  ABOUT QUIZAPP           ║{Colors.RESET}")
        print(f"{Colors.HEADER}╚══════════════════════════════════════╝{Colors.RESET}\n")

        print(f"{Colors.BOLD}QuizApp v2.0{Colors.RESET}")
        print(f"A futuristic, cross-platform quiz application built with Python.")
        print()
        print(f"{Colors.BOLD}Developer:{Colors.RESET} {Colors.BRIGHT_CYAN}Noor Hoorain{Colors.RESET}")
        print(f"{Colors.BOLD}GitHub:{Colors.RESET} {Colors.BRIGHT_BLUE}https://github.com/noorhoorain44-ship-it{Colors.RESET}")
        print(f"{Colors.BOLD}License:{Colors.RESET} MIT License")
        print()
        print(f"{Colors.BOLD}Features:{Colors.RESET}")
        print("  • Multiple quiz categories")
        print("  • Custom quiz creation")
        print("  • User authentication & profiles")
        print("  • Global leaderboard")
        print("  • Timed quizzes")
        print("  • Progress tracking")
        print("  • CSV export")
        print("  • Cross-platform support")
        print()
        print(f"{Colors.BOLD}Platform:{Colors.RESET} {platform.system()} {platform.release()}")
        print(f"{Colors.BOLD}Python:{Colors.RESET} {platform.python_version()}")
        print()
        print(f"{Colors.DIM}Made with ❤️  by Noor Hoorain{Colors.RESET}")

        input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")

    def shutdown(self):
        """Graceful application shutdown"""
        print(f"\n{Colors.WARNING}👋 Thank you for using QuizApp!{Colors.RESET}")
        print(f"{Colors.DIM}Developed by Noor Hoorain{Colors.RESET}")
        loading_animation("Shutting down", 1.0)
        self.running = False

    def run(self):
        """Main application entry point"""
        try:
            while self.running:
                if not self.engine.current_user:
                    if not self.auth_menu():
                        break
                else:
                    self.main_menu()
        except KeyboardInterrupt:
            print(f"\n\n{Colors.WARNING}⚠️  Interrupted by user{Colors.RESET}")
            self.shutdown()
        except Exception as e:
            print(f"\n{Colors.ERROR}❌ An error occurred: {e}{Colors.RESET}")
        finally:
            print(f"\n{Colors.BRIGHT_CYAN}Goodbye! 👋{Colors.RESET}")
            sys.exit(0)

# ═══════════════════════════════════════════════════════════════════════════════
# APPLICATION ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    app = QuizApp()
    app.run()
