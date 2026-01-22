# scripture-to-slides

A command-line tool that fetches scripture and generates presentation-ready PDF slides for group scripture reading in youth groups, Bible studies, and church services.

Currently supports ESV (English Standard Version) via the ESV.org API.

## Features

- **16:9 Widescreen Slides** - Perfect for modern displays and projectors
- **Beautiful Typography** - Large, readable text with clean layout
- **Poetry Formatting** - Preserves line breaks and indentation for Psalms and poetic passages
- **Section Headings** - Bold, centered headings for context
- **Smart Pagination** - Automatically splits long passages across multiple slides
- **Multiple Passages** - Combine multiple references into one presentation
- **Flexible Output** - Generate combined or separate PDFs
- **Highly Configurable** - Customize fonts, sizes, and output settings

## Quick Start (macOS - No Installation Required)

**For non-technical users:** Download the standalone executable from the [Releases page](https://github.com/cmshinkle/scripture-to-slides/releases). No Python installation needed!

1. Download `scripture-to-slides` from the latest release

2. Get your free ESV API key from https://api.esv.org

3. On first run, the tool will create a config file at `~/.scripture-slides/config.yaml`

4. Edit the config file and add your API key

5. Run the executable:
   ```bash
   # Make it executable (first time only)
   chmod +x scripture-to-slides

   # Run it
   ./scripture-to-slides "John 3:16"

   # Or move it to your PATH for global access
   sudo mv scripture-to-slides /usr/local/bin/
   scripture-to-slides "John 3:16"
   ```

## Installation for Developers

### Prerequisites
- Python 3.8 or higher
- ESV API key (free at https://api.esv.org)

### Install from Source

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   ```

2. Install dependencies:
   ```bash
   pip install requests reportlab pyyaml
   ```

3. Run the tool:
   ```bash
   python -m scripture_slides.cli "John 3:16"
   ```

## Quick Start

1. **First run** - Generate config file:
   ```bash
   python -m scripture_slides.cli "John 3:16"
   ```
   This creates `~/.scripture-slides/config.yaml`

2. **Add your API key** - Edit the config file:
   ```bash
   open ~/.scripture-slides/config.yaml
   ```
   Replace `your-esv-api-key-here` with your actual API key from https://api.esv.org

3. **Generate slides**:
   ```bash
   python -m scripture_slides.cli "John 3:16-21"
   ```
   Your PDF will be saved to `./output/`

## Usage Examples

### Basic Usage

```bash
# Single verse
python -m scripture_slides.cli "John 3:16"

# Verse range
python -m scripture_slides.cli "John 3:16-21"

# Whole chapter
python -m scripture_slides.cli "Psalm 23"

# Multiple passages (combined into one PDF)
python -m scripture_slides.cli "John 3:16-21" "Romans 8:28-30"

# Comma-separated references
python -m scripture_slides.cli "John 3:16, Romans 8:28, Psalm 23"
```

### File Input

Create a text file with one reference per line:

**references.txt:**
```
John 3:16-21
Romans 8:28-30
Psalm 23
Matthew 5:1-12
```

Then generate slides:
```bash
python -m scripture_slides.cli --input-file references.txt
```

### Custom Output

```bash
# Custom filename
python -m scripture_slides.cli "Psalm 23" --output-file sunday-sermon.pdf

# Custom output directory
python -m scripture_slides.cli "John 3:16" --output-dir ~/Documents/Slides

# Separate PDFs for each passage
python -m scripture_slides.cli "John 3:16" "Romans 8:28" --separate

# Auto-open PDF after generation
python -m scripture_slides.cli "Psalm 23" --open
```

### Customization

```bash
# Different font
python -m scripture_slides.cli "John 3:16" --font Times-Roman

# Custom font size (default: 64pt)
python -m scripture_slides.cli "John 3:16" --font-size 72

# No section headings
python -m scripture_slides.cli "Matthew 5:1-12" --no-headings

# Combine multiple options
python -m scripture_slides.cli "Psalm 23" --font-size 80 --output-file large-psalm.pdf --open
```

## Command-Line Options

### Input Options

| Flag | Description |
|------|-------------|
| `references` | Scripture reference(s) as positional arguments |
| `-f, --input-file FILE` | Read references from a text file (one per line) |

### Output Options

| Flag | Description |
|------|-------------|
| `-o, --output-file FILE` | Custom output filename (default: `scripture_YYYY-MM-DD_HHMM.pdf`) |
| `-d, --output-dir DIR` | Output directory (default: `./output/`) |
| `-s, --separate` | Generate separate PDFs for each passage |
| `--open` | Auto-open PDF(s) after generation |

### Content Options

| Flag | Description |
|------|-------------|
| `--no-headings` | Exclude section headings from slides |

### Appearance Options

| Flag | Description |
|------|-------------|
| `--font NAME` | Font family (default: `Helvetica`; also supports `Times-Roman`, `Courier`) |
| `--font-size SIZE` | Body text font size in points (default: `64`) |

### Other Options

| Flag | Description |
|------|-------------|
| `-h, --help` | Show help message and exit |
| `-v, --version` | Show version number and exit |

## Configuration

Settings can be configured in `~/.scripture-slides/config.yaml`:

```yaml
# Bible API settings
api_endpoint: "https://api.esv.org/v3/passage/text/"  # API endpoint URL
api_key: "your-esv-api-key-here"  # ESV API key from https://api.esv.org

# Output settings
output_directory: "./output"
output_type: "pdf"

# PDF appearance
font: "Helvetica"
font_size: 64

# Behavior
auto_open: false
include_section_headings: true
combine_passages: true
```

Command-line flags override config file settings.

## Slide Layout

### Title Slide
- Centered passage reference (e.g., "John 3:16–21")
- Black background, white text
- ESV attribution in footer

### Body Slides
- Large, readable text (64pt default)
- White superscript verse numbers
- Section headings (bold, centered)
- Smart pagination (headings always with at least one verse)
- Poetry formatting preserved (line breaks and indentation)
- Reference and ESV attribution in footer

## Getting an ESV API Key

1. Visit https://api.esv.org
2. Click "Get API Key"
3. Create a free account
4. Copy your API key
5. Add it to `~/.scripture-slides/config.yaml`

The API key is free for personal and church use.

## Troubleshooting

### "Config file created" message
- The tool created a config file for you
- Add your ESV API key to `~/.scripture-slides/config.yaml`
- Run the command again

### "ESV API key is invalid"
- Check that your API key is correct in the config file
- Ensure there are no extra spaces or quotes
- Get a new key at https://api.esv.org if needed

### PDF not opening automatically
- Use the `--open` flag
- Or set `auto_open: true` in your config file
- PDFs are always saved even if they don't auto-open

### Text is too small/large
- Use `--font-size` to adjust (try values between 48-80)
- Or update `font_size` in your config file

## Examples for Common Use Cases

### Youth Group
```bash
python -m scripture_slides.cli "John 3:16-21" "Romans 5:8" --font-size 72 --open
```

### Bible Study Series
```bash
python -m scripture_slides.cli --input-file romans-study.txt --separate --output-dir ~/RomansSeries
```

### Sunday Sermon
```bash
python -m scripture_slides.cli "Matthew 5:1-20" --output-file sermon-beatitudes.pdf --font-size 64 --open
```

### Worship Service Readings
```bash
python -m scripture_slides.cli "Psalm 23" "John 10:11-18" --output-file good-shepherd-readings.pdf
```

## License

MIT License

## Credits

Scripture quotations are from the ESV® Bible (The Holy Bible, English Standard Version®), copyright © 2001 by Crossway, a publishing ministry of Good News Publishers. Used by permission. All rights reserved.
