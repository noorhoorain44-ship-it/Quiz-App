#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════════════
# QuizApp v2.0 - Installation Script for Linux/macOS
# Developed by: Noor Hoorain
# GitHub: https://github.com/noorhoorain44-ship-it
# ═══════════════════════════════════════════════════════════════════════════════

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'
BOLD='\033[1m'

# Banner
echo ""
echo -e "${CYAN}╔════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║${NC}                                                                ${CYAN}║${NC}"
echo -e "${CYAN}║${NC}   ${BOLD}🚀 QuizApp v2.0 - Installation Script${NC}                       ${CYAN}║${NC}"
echo -e "${CYAN}║${NC}   ${YELLOW}Developed by: Noor Hoorain${NC}                                  ${CYAN}║${NC}"
echo -e "${CYAN}║${NC}   ${BLUE}GitHub: noorhoorain44-ship-it${NC}                               ${CYAN}║${NC}"
echo -e "${CYAN}║${NC}                                                                ${CYAN}║${NC}"
echo -e "${CYAN}╚════════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Detect OS
OS="$(uname -s)"
ARCH="$(uname -m)"

echo -e "${BLUE}📋 System Information:${NC}"
echo -e "   OS: ${YELLOW}$OS${NC}"
echo -e "   Architecture: ${YELLOW}$ARCH${NC}"
echo ""

# Check if running as root (not recommended)
if [ "$EUID" -eq 0 ]; then
    echo -e "${YELLOW}⚠️  Warning: Running as root is not recommended${NC}"
    read -p "Continue anyway? (y/n): " choice
    if [[ ! "$choice" =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Detect distribution
if [ -f /etc/os-release ]; then
    . /etc/os-release
    DISTRO=$NAME
    DISTRO_ID=$ID
else
    DISTRO="Unknown"
    DISTRO_ID="unknown"
fi

echo -e "${BLUE}🖥️  Distribution: ${YELLOW}$DISTRO${NC}"
echo ""

# Check Python installation
echo -e "${BLUE}🔍 Checking Python installation...${NC}"
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    PYTHON_VERSION=$($PYTHON_CMD --version 2>&1)
    echo -e "   ${GREEN}✅ Found: $PYTHON_VERSION${NC}"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
    PYTHON_VERSION=$($PYTHON_CMD --version 2>&1)
    echo -e "   ${GREEN}✅ Found: $PYTHON_VERSION${NC}"
else
    echo -e "   ${RED}❌ Python not found!${NC}"
    echo -e "${YELLOW}📦 Installing Python...${NC}"

    case $DISTRO_ID in
        ubuntu|debian|kali|linuxmint|pop)
            sudo apt-get update
            sudo apt-get install -y python3 python3-pip
            PYTHON_CMD="python3"
            ;;
        fedora|rhel|centos|rocky|almalinux)
            sudo dnf install -y python3 python3-pip
            PYTHON_CMD="python3"
            ;;
        arch|manjaro|endeavouros)
            sudo pacman -S --noconfirm python python-pip
            PYTHON_CMD="python"
            ;;
        opensuse*)
            sudo zypper install -y python3 python3-pip
            PYTHON_CMD="python3"
            ;;
        alpine)
            sudo apk add python3 py3-pip
            PYTHON_CMD="python3"
            ;;
        macos|darwin)
            if command -v brew &> /dev/null; then
                brew install python
            else
                echo -e "${RED}❌ Please install Homebrew first: https://brew.sh${NC}"
                exit 1
            fi
            PYTHON_CMD="python3"
            ;;
        *)
            echo -e "${RED}❌ Unsupported distribution. Please install Python manually.${NC}"
            exit 1
            ;;
    esac
fi

# Verify Python version
PYTHON_VERSION_NUM=$($PYTHON_CMD -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
REQUIRED_VERSION="3.10"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION_NUM" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo -e "   ${YELLOW}⚠️  Python $PYTHON_VERSION_NUM detected. Python 3.10+ recommended for match-case support.${NC}"
    echo -e "   ${YELLOW}   The app will work but some features may be limited.${NC}"
else
    echo -e "   ${GREEN}✅ Python version is compatible!${NC}"
fi

echo ""

# Create installation directory
INSTALL_DIR="$HOME/.local/share/quizapp"
BIN_DIR="$HOME/.local/bin"

echo -e "${BLUE}📁 Creating installation directories...${NC}"
mkdir -p "$INSTALL_DIR"
mkdir -p "$BIN_DIR"
echo -e "   ${GREEN}✅ Directories created${NC}"
echo ""

# Copy application files
echo -e "${BLUE}📦 Installing QuizApp files...${NC}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cp "$SCRIPT_DIR/quizapp.py" "$INSTALL_DIR/"
chmod +x "$INSTALL_DIR/quizapp.py"

# Create launcher script
cat > "$BIN_DIR/quizapp" << 'EOF'
#!/bin/bash
python3 "$HOME/.local/share/quizapp/quizapp.py" "$@"
EOF
chmod +x "$BIN_DIR/quizapp"

echo -e "   ${GREEN}✅ Files installed${NC}"
echo ""

# Add to PATH if not already there
echo -e "${BLUE}🔧 Configuring PATH...${NC}"
if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
    SHELL_RC=""
    if [ -n "$ZSH_VERSION" ]; then
        SHELL_RC="$HOME/.zshrc"
    elif [ -n "$BASH_VERSION" ]; then
        SHELL_RC="$HOME/.bashrc"
    else
        SHELL_RC="$HOME/.profile"
    fi

    echo "export PATH="$BIN_DIR:\$PATH"" >> "$SHELL_RC"
    echo -e "   ${GREEN}✅ Added $BIN_DIR to PATH in $SHELL_RC${NC}"
    echo -e "   ${YELLOW}⚠️  Please run: source $SHELL_RC${NC}"
else
    echo -e "   ${GREEN}✅ Already in PATH${NC}"
fi
echo ""

# Create desktop entry (Linux only)
if [ "$OS" = "Linux" ]; then
    DESKTOP_DIR="$HOME/.local/share/applications"
    mkdir -p "$DESKTOP_DIR"

    cat > "$DESKTOP_DIR/quizapp.desktop" << EOF
[Desktop Entry]
Name=QuizApp
Comment=Futuristic Quiz Application by Noor Hoorain
Exec=gnome-terminal -- bash -c "quizapp; read -p 'Press Enter to close...'"
Type=Application
Terminal=true
Icon=utilities-terminal
Categories=Education;
Keywords=quiz;education;learning;
EOF
    chmod +x "$DESKTOP_DIR/quizapp.desktop"
    echo -e "   ${GREEN}✅ Desktop entry created${NC}"
fi

echo ""

# Verify installation
echo -e "${BLUE}🔍 Verifying installation...${NC}"
if [ -f "$INSTALL_DIR/quizapp.py" ]; then
    echo -e "   ${GREEN}✅ QuizApp installed successfully!${NC}"
else
    echo -e "   ${RED}❌ Installation failed!${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}╔════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║${NC}                    ${BOLD}✅ INSTALLATION COMPLETE${NC}                    ${GREEN}║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${CYAN}🚀 To start QuizApp, run:${NC}"
echo -e "   ${YELLOW}quizapp${NC}           (after reloading shell or opening new terminal)"
echo -e "   ${YELLOW}python3 $INSTALL_DIR/quizapp.py${NC}  (direct path)"
echo ""
echo -e "${CYAN}📁 Installation location:${NC} ${YELLOW}$INSTALL_DIR${NC}"
echo -e "${CYAN}📊 Data directory:${NC} ${YELLOW}$HOME/.config/quizapp${NC}"
echo ""
echo -e "${BLUE}💡 Tip: Run 'quizapp --help' for usage information${NC}"
echo -e "${BLUE}🐛 Issues? Report at: https://github.com/noorhoorain44-ship-it/quizapp/issues${NC}"
echo ""
echo -e "${YELLOW}Made with ❤️  by Noor Hoorain${NC}"
