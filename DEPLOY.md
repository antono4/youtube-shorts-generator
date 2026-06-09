# YouTube Shorts Video Generator - Deployment Guide

## Overview

This is a client-side YouTube Shorts Video Generator application built with HTML, CSS, and JavaScript. No server required!

## Features

- 🎨 **Background Options**: Solid colors, gradients, or custom images
- ✏️ **Text Overlay**: Customizable text with 5 animation effects
- 🎵 **Audio**: Background music support
- 📹 **Video Output**: 1080x1920 vertical video (9:16 aspect ratio)
- ⚡ **Client-Side**: All processing happens in your browser

## Quick Start

### Option 1: Open Directly
Simply open `index.html` in any modern web browser (Chrome, Firefox, Safari, Edge).

### Option 2: Local Server
```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx serve .

# Using PHP
php -S localhost:8000
```

Then visit `http://localhost:8000`

## How to Use

1. **Select Background**: Choose between Solid Color, Gradient, or Image
2. **Add Text**: Enter your text and customize font size, color, and position
3. **Add Music** (Optional): Upload an MP3 or WAV file
4. **Generate**: Click "Generate Video" and download when ready

## GitHub Repository Setup

Due to GitHub token permissions, you may need to create the repository manually:

1. Go to https://github.com/new
2. Create a new repository named `youtube-shorts-generator`
3. Run these commands in your terminal:

```bash
git remote add origin https://github.com/YOUR_USERNAME/youtube-shorts-generator.git
git push -u origin main
```

## Browser Compatibility

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## License

MIT License - Feel free to use and modify!