# html-font-preview-generator
Python script for generating an HTML preview file for all the fonts installed on the system

## Requirements

- **python3** — download from https://www.python.org/downloads or use your OS package manager
```bash
# MacOS
brew install python3

# debian Linux
sudo apt install python3

# Windows (with chocolatey)
choco install python --pre 
```
- **matplotlib**

```bash
pip3 install matplotlib
```

## Usage

Run the script

```bash
python3 html_fontlist_generator.py
```

After the script is executed a file named `fontlist.html` will be created in the same folder as the script. Open the file with your browser by double-clicking it.
