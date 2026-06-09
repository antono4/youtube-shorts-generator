# YouTube Shorts Video Generator - Specification

## 1. Project Overview

**Project Name**: YouTube Shorts Video Generator  
**Project Type**: Web Application (Python/Streamlit)  
**Core Functionality**: A web-based tool that allows users to create vertical short videos (9:16 aspect ratio) optimized for YouTube Shorts with customizable backgrounds, text overlays, and background music.  
**Target Users**: Content creators, social media managers, and anyone wanting to create quick vertical videos for YouTube Shorts.

## 2. UI/UX Specification

### Layout Structure

- **Single Page Application**: All functionality on one page using Streamlit
- **Sidebar**: Configuration options and settings
- **Main Area**: Video preview and generation controls

### Visual Design

**Color Palette**:
- Primary: `#FF0050` (YouTube Red)
- Secondary: `#1A1A2E` (Dark Navy)
- Accent: `#FFD700` (Gold)
- Background: `#0F0F1A` (Deep Dark)
- Text: `#FFFFFF` (White)
- Surface: `#16213E` (Card Background)

**Typography**:
- Font Family: 'Poppins' for headings, 'Inter' for body
- Heading Size: 24px bold
- Body Size: 14px regular
- Caption Size: 12px

**Spacing System**:
- Base unit: 8px
- Padding: 16px, 24px, 32px
- Border radius: 12px for cards, 8px for buttons

**Visual Effects**:
- Gradient overlays on video preview
- Subtle shadow on cards: `0 4px 20px rgba(0,0,0,0.3)`
- Smooth transitions on hover states

### Components

1. **Header**: App title with YouTube-style branding
2. **Sidebar Panel**:
   - Background type selector (solid color, gradient, image)
   - Text input for overlay text
   - Font size slider
   - Text position selector (top, center, bottom)
   - Background music upload/selector
   - Video duration selector (15s, 30s, 60s)
3. **Main Preview Area**:
   - Live video preview (9:16 aspect ratio)
   - Frame-by-frame animation
4. **Action Buttons**:
   - "Generate Video" button
   - "Download" button
   - "Reset" button

## 3. Functionality Specification

### Core Features

1. **Background Options**:
   - Solid color selection with color picker
   - Gradient backgrounds (predefined)
   - Image upload as background

2. **Text Overlay**:
   - Multi-line text support
   - Font size adjustment (16-72px)
   - Text position: top, center, bottom
   - Text animation (fade-in, typewriter, bounce)
   - Color picker for text

3. **Background Music**:
   - Upload audio file (MP3, WAV)
   - Built-in sound effects library
   - Volume control

4. **Video Generation**:
   - Output format: MP4 (H.264)
   - Resolution: 1080x1920 (Full HD vertical)
   - Frame rate: 30 FPS
   - Automatic text animation timing

5. **Export Options**:
   - Download as MP4
   - Copy shareable filename

### User Interactions

1. User selects background type
2. User uploads or selects background content
3. User enters overlay text
4. User customizes text style (size, position, color, animation)
5. User optionally adds background music
6. User previews the result in real-time
7. User clicks "Generate Video"
8. Video is rendered and made available for download

### Data Handling

- All processing happens client-side (browser)
- Temporary files stored in `/tmp` directory
- Files cleaned up after download
- No persistent user data storage

### Edge Cases

- Large file uploads (>50MB): Show warning
- Unsupported formats: Display error message
- Empty text input: Allow video without text
- Network issues: Graceful error handling

## 4. Technical Stack

- **Framework**: Streamlit (Python)
- **Video Processing**: OpenCV, MoviePy
- **Audio Processing**: Pydub
- **Styling**: Custom CSS with Streamlit theming

## 5. Acceptance Criteria

- [ ] Application launches without errors
- [ ] User can select/create background
- [ ] User can add and style text overlay
- [ ] User can add background music
- [ ] Preview shows live animation
- [ ] Video generates successfully in 9:16 format
- [ ] Download works correctly
- [ ] All UI elements are responsive
- [ ] Application handles edge cases gracefully