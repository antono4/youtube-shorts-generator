# 🎬 YouTube Shorts Video Generator

A modern, client-side web application for creating vertical videos optimized for YouTube Shorts. Built with pure HTML, CSS, and JavaScript - no server required!

![YouTube Shorts Generator](https://img.shields.io/badge/YouTube-Shorts-FF0050?style=for-the-badge&logo=youtube)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript)

## ✨ Features

### 🎨 Background Options
- **Solid Colors**: Choose any color with a color picker
- **Gradients**: 10 beautiful pre-made gradients (Sunset, Ocean, Forest, Fire, Ice, Midnight, Aurora, Candy, Gold, Purple)
- **Images**: Upload your own background images

### ✏️ Text Overlay
- Multi-line text support
- Customizable font size (24px - 120px)
- Color picker for text
- Position options: Top, Center, Bottom
- 5 animation effects:
  - None
  - Fade In
  - Typewriter
  - Bounce
  - Slide Up

### 🎵 Audio
- Upload background music (MP3, WAV, OGG)
- Adds engagement to your content

### 📹 Video Output
- Resolution: 1080 × 1920 (Full HD)
- Aspect Ratio: 9:16 (Vertical)
- Format: WebM (VP9 codec)
- Frame Rate: 30 FPS
- Duration: 15, 30, or 60 seconds

## 🚀 Quick Start

### Option 1: Open Directly
Simply open `index.html` in any modern web browser.

### Option 2: Use with Local Server
```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx serve .

# Using PHP
php -S localhost:8000
```

Then visit `http://localhost:8000` in your browser.

## 📖 How to Use

1. **Select Background Type**
   - Choose between Solid Color, Gradient, or Image
   - Customize the selected option

2. **Add Text Overlay**
   - Enter your text in the textarea
   - Choose text color, size, and position
   - Select an animation effect

3. **Add Audio (Optional)**
   - Toggle the audio upload section
   - Select an MP3 or WAV file

4. **Generate Video**
   - Click the "Generate Video" button
   - Wait for the video to be created
   - Download your video

## 🎯 Use Cases

- Create quick tutorial clips
- Make quote/statement videos
- Produce motivational content
- Generate promotional material
- Create before/after comparisons
- Make text-based stories

## 💡 Tips for Better Videos

1. **Keep it Short**: YouTube Shorts perform best under 30 seconds
2. **High Contrast**: Ensure text is readable against the background
3. **Bold Text**: Use larger font sizes for mobile viewing
4. **Add Music**: Background music increases engagement
5. **Brand Colors**: Use consistent colors for brand recognition

## 🛠️ Technical Details

### Browser Compatibility
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

### Technologies Used
- **HTML5 Canvas**: For rendering frames
- **CSS3**: Modern UI with Flexbox and Grid
- **JavaScript ES6+**: Pure JavaScript, no frameworks
- **MediaRecorder API**: For video encoding
- **Web Audio API**: For audio processing

### File Structure
```
├── index.html      # Main application
├── SPEC.md         # Technical specification
├── README.md       # Documentation
└── requirements.txt # (Optional) Python dependencies
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- YouTube Shorts for inspiring this project
- Google Fonts for Poppins and Inter fonts
- All contributors and users of this tool

---

Made with ❤️ for content creators everywhere