# How to Create a Release

This guide walks through creating a new release of scripture-to-slides on GitHub.

## Before You Release

1. **Make sure all changes are committed and pushed**
   ```bash
   git status  # Should show "nothing to commit, working tree clean"
   git push origin main
   ```

2. **Test that everything works**
   ```bash
   source venv/bin/activate
   pytest  # All tests should pass
   scripture-to-slides "John 3:16" --output-file test.pdf
   ```

3. **Update version number** (optional but recommended)
   - Edit `pyproject.toml` and update the version number
   - Example: `version = "0.1.0"` → `version = "0.2.0"`
   - Commit and push:
     ```bash
     git add pyproject.toml
     git commit -m "Bump version to 0.2.0"
     git push origin main
     ```

## Creating a Release on GitHub

### Step 1: Create and Push a Git Tag

Tags mark specific points in your repository's history. Each release needs a tag.

```bash
# Create a tag (use semantic versioning: v0.1.0, v0.2.0, v1.0.0, etc.)
git tag v0.1.0

# Push the tag to GitHub
git push origin v0.1.0
```

**Tag naming convention:**
- `v0.1.0` - First release
- `v0.2.0` - Minor feature additions
- `v1.0.0` - Major milestone
- `v0.1.1` - Bug fix release

### Step 2: Create the Release on GitHub

1. **Go to your repository on GitHub**
   - https://github.com/cmshinkle/scripture-to-slides

2. **Click "Releases"** (on the right sidebar)

3. **Click "Draft a new release"**

4. **Fill in the release form:**

   - **Choose a tag:** Select the tag you just pushed (e.g., `v0.1.0`)

   - **Release title:** Give it a descriptive name
     - Example: `v0.1.0 - Initial Release`
     - Example: `v0.2.0 - NET Bible Support`

   - **Description:** Write release notes describing what's new
     ```markdown
     ## What's New

     - Added support for custom fonts
     - Fixed pagination issue with long passages
     - Improved poetry formatting for Psalms

     ## Installation

     Download `scripture-to-slides` below and follow the instructions in README.md

     ## Requirements

     - macOS 10.15 or later
     - ESV API key (free at https://api.esv.org)
     ```

5. **Click "Publish release"**

### Step 3: Wait for the Build

Once you publish the release:

1. **GitHub Action automatically starts** (takes 5-10 minutes)
   - Go to the "Actions" tab to watch progress
   - Look for "Build macOS Release" workflow

2. **When complete, the executable appears** on your release page
   - Refresh the release page
   - You'll see `scripture-to-slides` listed under "Assets"

3. **Anyone can now download it!**

## Quick Release Checklist

- [ ] All changes committed and pushed
- [ ] Tests passing (`pytest`)
- [ ] Version number updated in `pyproject.toml`
- [ ] Git tag created and pushed (`git tag v0.1.0 && git push origin v0.1.0`)
- [ ] Release created on GitHub with descriptive notes
- [ ] GitHub Action completed successfully
- [ ] Executable appears in release assets

## Troubleshooting

### "Tag already exists"
If you need to redo a release:
```bash
# Delete local tag
git tag -d v0.1.0

# Delete remote tag
git push origin :refs/tags/v0.1.0

# Create the tag again
git tag v0.1.0
git push origin v0.1.0
```

### GitHub Action Failed
1. Go to Actions tab
2. Click on the failed workflow
3. Read the error message
4. Common issues:
   - Missing dependencies in `requirements.txt`
   - Syntax errors in code
   - PyInstaller compatibility issues

### Executable Won't Run on macOS
Users might see "can't be opened because it is from an unidentified developer"

**Solution for users:**
```bash
# Right-click the file → "Open" (instead of double-click)
# Or remove quarantine:
xattr -d com.apple.quarantine scripture-to-slides
chmod +x scripture-to-slides
```

## Example Release Notes Template

```markdown
# scripture-to-slides v0.1.0

Initial release of scripture-to-slides - a CLI tool to generate presentation-ready PDF slides from scripture passages.

## Features

- ESV Bible support via ESV.org API
- 16:9 widescreen slides with beautiful typography
- Poetry formatting for Psalms
- Smart pagination with section headings
- Configurable fonts and sizes
- Multiple output options

## Installation

**Download:** `scripture-to-slides` (macOS)

**Setup:**
1. Download the executable
2. Get free ESV API key: https://api.esv.org
3. Run: `chmod +x scripture-to-slides`
4. First run creates config at `~/.scripture-slides/config.yaml`
5. Add your API key to the config file

**Usage:**
```bash
./scripture-to-slides "John 3:16"
./scripture-to-slides "Psalm 23" --font-size 72 --open
```

## Requirements

- macOS 10.15 or later
- ESV API key (free)

## Known Issues

None

## What's Next

See [BACKLOG.md](BACKLOG.md) for planned features.
```

## Semantic Versioning Guide

**MAJOR.MINOR.PATCH** (e.g., 1.2.3)

- **MAJOR** (1.0.0): Breaking changes - Changes that require users to update their workflow
- **MINOR** (0.2.0): New features - Backwards-compatible functionality additions
- **PATCH** (0.1.1): Bug fixes - Backwards-compatible bug fixes

**Examples:**
- `v0.1.0` → `v0.1.1`: Fixed a bug
- `v0.1.0` → `v0.2.0`: Added NET Bible support
- `v0.9.0` → `v1.0.0`: First stable release
- `v1.2.0` → `v2.0.0`: Changed CLI flags (breaking change)

## Deleting a Release

If you need to delete a release:

1. Go to the Releases page
2. Click on the release
3. Click "Delete" (top right)
4. Delete the tag:
   ```bash
   git push origin :refs/tags/v0.1.0
   git tag -d v0.1.0
   ```

## Resources

- [GitHub Releases Documentation](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
- [Semantic Versioning](https://semver.org/)
- [Writing Good Release Notes](https://github.com/phauer/blog-related/blob/master/release-notes/release-notes.md)
