# 🎬 YouTube Shorts Video Generator - AI Powered

> **Created by Antono**


A modern, client-side web application for creating vertical videos optimized for YouTube Shorts with **AI-powered image generation**. Built with pure HTML, CSS, and JavaScript - no server required!

![YouTube Shorts Generator](https://img.shields.io/badge/YouTube-Shorts-FF0050?style=for-the-badge&logo=youtube)
![AI Powered](https://img.shields.io/badge/AI-Powered-7B2FFF?style=for-the-badge)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript)

## ✨ Features

### 🤖 AI Generate Mode (NEW!)
- **Text-to-Image AI**: Generate stunning backgrounds from text prompts
- **8 Style Presets**: Cinematic, Anime, Realistic, Abstract, Neon, Minimal, Fantasy, None
- **Quick Prompts**: Pre-made prompt suggestions for instant creativity
- **API Integration**: Works with Replicate API (Stable Diffusion) or Hugging Face
- **Vertical Output**: Optimized 9:16 aspect ratio for Shorts

### 🎨 Background Options (Manual Mode)
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

## 🤖 AI Generation (No API Key Required!)

This app uses **Pollinations.ai** for free, unlimited AI image generation - no API key needed!

### How to Use AI
1. Click the **"🤖 AI Generate"** tab
2. Enter a prompt describing the background you want
3. Select a style preset (Cinematic, Anime, Realistic, etc.)
4. Click **"Generate with AI"**
5. Wait 10-20 seconds for the image to be created
6. Add text overlay and generate your video!

### Example Prompts

| Category | Prompt | Style |
|----------|--------|-------|
| 🌅 Nature | Sunset over ocean waves, golden hour | Cinematic |
| 🌃 Urban | Cyberpunk city at night, neon lights, rain | Neon |
| 🌲 Fantasy | Magical forest with glowing mushrooms and fireflies | Fantasy |
| 🌌 Space | Space nebula with stars and galaxies | Cinematic |
| 🏔️ Landscape | Mountain peak above clouds, sunrise | Realistic |
| 🎨 Abstract | Abstract geometric shapes, vibrant colors | Abstract |

## 🎯 Style Presets

| Style | Description |
|-------|-------------|
| **Cinematic** | Film-like quality with dramatic lighting |
| **Anime** | Japanese animation style, vibrant colors |
| **Realistic** | Photorealistic, hyper-detailed images |
| **Abstract** | Modern art, geometric shapes |
| **Neon** | Cyberpunk aesthetic, glowing lights |
| **Minimal** | Clean, simple, minimalist design |
| **Fantasy** | Magical, ethereal, otherworldly |
| **None** | No style modification |

## 📖 How to Use

### Manual Mode
1. **Select Background Type**: Choose between Solid Color, Gradient, or Image
2. **Customize Background**: Pick a color, select a gradient, or upload your own image
3. **Add Text Overlay**: Enter your text, choose color, size, and position
4. **Select Animation**: Choose from 5 animation effects
5. **Add Audio (Optional)**: Upload background music
6. **Generate Video**: Click "Generate Video" and download

### AI Mode
1. **Switch to AI Tab**: Click the "🤖 AI Generate" tab
2. **Enter Prompt**: Describe the background you want
3. **Select Style**: Choose a style preset
4. **Generate**: Click "Generate with AI"
5. **Customize**: Add text overlay and effects
6. **Create Video**: Generate your Shorts!

## 🎯 Use Cases

- Create quick tutorial clips
- Make quote/statement videos
- Produce motivational content
- Generate promotional material
- Create AI-generated artistic backgrounds
- Make text-based stories

## 💡 Tips for Better Videos

1. **Keep it Short**: YouTube Shorts perform best under 30 seconds
2. **High Contrast**: Ensure text is readable against the background
3. **Bold Text**: Use larger font sizes for mobile viewing
4. **Add Music**: Background music increases engagement
5. **Use AI for Unique Backgrounds**: Stand out from other creators
6. **Be Specific with Prompts**: More detail = better AI results

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
- **AI APIs**: Replicate & Hugging Face for image generation

### File Structure
```
├── index.html      # Main application
├── SPEC.md         # Technical specification
├── README.md       # Documentation
├── DEPLOY.md       # Deployment guide
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
- Stable Diffusion by Stability AI
- Replicate for easy AI model hosting
- Hugging Face for free inference API
- Google Fonts for Poppins and Inter fonts
- All contributors and users of this tool

---

Made with ❤️ for content creators everywhere | ✨ AI Powered