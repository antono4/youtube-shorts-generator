"""
YouTube Shorts Video Generator
A web application to create vertical short videos for YouTube Shorts
"""

import streamlit as st
import tempfile
import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="YouTube Shorts Video Generator",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Inter:wght@400;500&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #0F0F1A 0%, #1A1A2E 100%);
    }
    
    h1, h2, h3 {
        font-family: 'Poppins', sans-serif;
        color: #FFFFFF;
    }
    
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(90deg, #FF0050, #FFD700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        padding: 1rem 0;
    }
    
    .subtitle {
        font-family: 'Inter', sans-serif;
        color: #AAAAAA;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #FF0050, #FF3366);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 12px;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 20px rgba(255, 0, 80, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(255, 0, 80, 0.5);
    }
    
    .sidebar .stSelectbox label, .sidebar .stSlider label, .sidebar .stTextArea label {
        font-family: 'Inter', sans-serif;
        color: #FFFFFF;
    }
    
    .preview-container {
        background: #16213E;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    }
    
    .video-placeholder {
        aspect-ratio: 9/16;
        background: linear-gradient(180deg, #1A1A2E 0%, #16213E 100%);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #666;
        font-family: 'Inter', sans-serif;
    }
    
    .stCard {
        background: #16213E;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }
    
    .success-box {
        background: linear-gradient(135deg, #00C853, #00E676);
        padding: 1rem;
        border-radius: 12px;
        color: white;
        font-family: 'Inter', sans-serif;
        text-align: center;
    }
    
    .gradient-box {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        margin: 10px 0;
    }
    
    .gradient-swatch {
        width: 50px;
        height: 50px;
        border-radius: 8px;
        cursor: pointer;
        border: 2px solid transparent;
        transition: all 0.2s;
    }
    
    .gradient-swatch:hover {
        transform: scale(1.1);
        border-color: #FF0050;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #16213E;
        border-radius: 8px 8px 0px 0px;
        padding: 10px 20px;
        color: #AAAAAA;
    }
    
    .stTabs .css-1q8j8a6:hover {
        background-color: #1E2A4A;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #FF0050 !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Predefined gradients
GRADIENTS = {
    "Sunset": ["#FF6B6B", "#4ECDC4"],
    "Ocean": ["#667EEA", "#764BA2"],
    "Forest": ["#11998E", "#38EF7D"],
    "Fire": ["#F093FB", "#F5576C"],
    "Ice": ["#00C9FF", "#92FE9D"],
    "Midnight": ["#0F2027", "#2C5364"],
    "Aurora": ["#00B4DB", "#0083B0"],
    "Candy": ["#FFB6C1", "#E6E6FA"],
    "Gold": ["#F7971E", "#FFD200"],
    "Purple": ["#8E2DE2", "#4A00E0"],
}

# Animation options
ANIMATIONS = {
    "None": "none",
    "Fade In": "fade",
    "Typewriter": "typewriter",
    "Bounce": "bounce",
    "Slide Up": "slide_up",
    "Scale": "scale",
}

# Initialize session state
if 'generated_video' not in st.session_state:
    st.session_state.generated_video = None
if 'preview_text' not in st.session_state:
    st.session_state.preview_text = ""
if 'preview_bg_color' not in st.session_state:
    st.session_state.preview_bg_color = "#FF0050"
if 'preview_gradient' not in st.session_state:
    st.session_state.preview_gradient = None


def create_gradient_image(width, height, colors, direction="vertical"):
    """Create a gradient image"""
    image = Image.new("RGB", (width, height))
    pixels = image.load()
    
    for y in range(height):
        for x in range(width):
            if direction == "vertical":
                ratio = y / height
            else:
                ratio = x / width
            
            r = int(colors[0][0] * (1 - ratio) + colors[1][0] * ratio)
            g = int(colors[0][1] * (1 - ratio) + colors[1][1] * ratio)
            b = int(colors[0][2] * (1 - ratio) + colors[1][2] * ratio)
            pixels[x, y] = (r, g, b)
    
    return image


def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def create_preview_frame(bg_type, bg_value, text, font_size, text_color, position, animation, duration_frames):
    """Create a single preview frame"""
    width, height = 360, 640
    current_frame = min(duration_frames, 30)  # Show at 1 second mark for preview
    
    if bg_type == "solid":
        bg_color = hex_to_rgb(bg_value)
        image = Image.new("RGB", (width, height), bg_color)
    elif bg_type == "gradient":
        colors = [hex_to_rgb(c) for c in GRADIENTS[bg_value]]
        image = create_gradient_image(width, height, colors)
    else:  # image
        if bg_value and os.path.exists(bg_value):
            img = Image.open(bg_value).convert("RGB")
            img = img.resize((width, height), Image.Resampling.LANCZOS)
            image = img
        else:
            image = Image.new("RGB", (width, height), (30, 30, 50))
    
    # Calculate text animation
    text_opacity = 1.0
    text_offset_y = 0
    
    if animation == "fade":
        text_opacity = min(1.0, current_frame / 15)
    elif animation == "slide_up":
        text_offset_y = max(0, int((15 - current_frame) * 5)) if current_frame < 15 else 0
    elif animation == "bounce":
        if current_frame < 10:
            text_offset_y = int(-20 * (1 - current_frame / 10))
        elif current_frame < 20:
            text_offset_y = int(-5 * (1 - abs(10 - current_frame) / 10))
        else:
            text_offset_y = 0
    elif animation == "scale":
        text_opacity = min(1.0, current_frame / 10)
    
    # Add text overlay
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    # Word wrap text
    words = text.split()
    lines = []
    current_line = []
    
    for word in words:
        test_line = ' '.join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if bbox[2] - bbox[0] <= width - 40:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]
    if current_line:
        lines.append(' '.join(current_line))
    
    # Calculate position
    line_height = font_size + 10
    total_text_height = len(lines) * line_height
    
    if position == "top":
        y_start = 50 + text_offset_y
    elif position == "center":
        y_start = (height - total_text_height) // 2 + text_offset_y
    else:  # bottom
        y_start = height - total_text_height - 50 + text_offset_y
    
    # Apply opacity effect
    if text_opacity < 1.0:
        overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        alpha = int(255 * text_opacity)
        for i, line in enumerate(lines):
            bbox = draw.textbbox((0, 0), line, font=font)
            text_width = bbox[2] - bbox[0]
            x = (width - text_width) // 2
            overlay_draw.text((x, y_start + i * line_height), line, font=font, fill=(255, 255, 255, alpha))
        image = Image.alpha_composite(image.convert("RGBA"), overlay)
    else:
        for i, line in enumerate(lines):
            bbox = draw.textbbox((0, 0), line, font=font)
            text_width = bbox[2] - bbox[0]
            x = (width - text_width) // 2
            draw.text((x, y_start + i * line_height), line, font=font, fill=text_color)
    
    return image


def generate_video(bg_type, bg_value, text, font_size, text_color, position, animation, duration, audio_path):
    """Generate the final video"""
    import subprocess
    
    # Video settings
    fps = 30
    total_frames = fps * duration
    width, height = 1080, 1920
    
    with tempfile.TemporaryDirectory() as tmpdir:
        frames_dir = os.path.join(tmpdir, "frames")
        os.makedirs(frames_dir, exist_ok=True)
        
        # Generate frames
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(total_frames):
            if bg_type == "solid":
                bg_color = hex_to_rgb(bg_value)
                frame = Image.new("RGB", (width, height), bg_color)
            elif bg_type == "gradient":
                colors = [hex_to_rgb(c) for c in GRADIENTS[bg_value]]
                frame = create_gradient_image(width, height, colors)
            else:  # image
                if bg_value and os.path.exists(bg_value):
                    img = Image.open(bg_value).convert("RGB")
                    img = img.resize((width, height), Image.Resampling.LANCZOS)
                    frame = img
                else:
                    frame = Image.new("RGB", (width, height), (30, 30, 50))
            
            # Text animation calculations
            if animation == "fade":
                if i < 15:
                    opacity = i / 15
                elif i > total_frames - 15:
                    opacity = (total_frames - i) / 15
                else:
                    opacity = 1.0
            elif animation == "slide_up":
                if i < 15:
                    offset_y = int(-200 * (1 - i / 15))
                elif i > total_frames - 20:
                    offset_y = int(-200 * ((total_frames - i) / 20))
                else:
                    offset_y = 0
            else:
                offset_y = 0
                opacity = 1.0
            
            # Draw text
            draw = ImageDraw.Draw(frame)
            try:
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size * 3)
            except:
                font = ImageFont.load_default()
            
            words = text.split()
            lines = []
            current_line = []
            
            for word in words:
                test_line = ' '.join(current_line + [word])
                bbox = draw.textbbox((0, 0), test_line, font=font)
                if bbox[2] - bbox[0] <= width - 100:
                    current_line.append(word)
                else:
                    if current_line:
                        lines.append(' '.join(current_line))
                    current_line = [word]
            if current_line:
                lines.append(' '.join(current_line))
            
            line_height = font_size * 3 + 30
            total_text_height = len(lines) * line_height
            
            if position == "top":
                y_start = 150 + offset_y
            elif position == "center":
                y_start = (height - total_text_height) // 2 + offset_y
            else:
                y_start = height - total_text_height - 150 + offset_y
            
            for j, line in enumerate(lines):
                bbox = draw.textbbox((0, 0), line, font=font)
                text_width = bbox[2] - bbox[0]
                x = (width - text_width) // 2
                
                # Apply opacity
                rgb_color = hex_to_rgb(text_color)
                if opacity < 1.0:
                    r, g, b = rgb_color
                    rgb_color = (int(r * opacity), int(g * opacity), int(b * opacity))
                
                draw.text((x, y_start + j * line_height), line, font=font, fill=rgb_color)
            
            # Save frame
            frame.save(os.path.join(frames_dir, f"frame_{i:05d}.png"))
            
            # Update progress
            if i % 10 == 0:
                progress = int((i / total_frames) * 80)
                progress_bar.progress(progress)
                status_text.text(f"Generating frames... {int((i/total_frames)*100)}%")
        
        progress_bar.progress(90)
        status_text.text("Creating video file...")
        
        # Create video with ffmpeg
        output_path = os.path.join(tmpdir, "output.mp4")
        
        if audio_path and os.path.exists(audio_path):
            # With audio
            cmd = [
                "ffmpeg", "-y", "-framerate", str(fps),
                "-i", os.path.join(frames_dir, "frame_%05d.png"),
                "-i", audio_path,
                "-c:v", "libx264", "-preset", "fast", "-crf", "23",
                "-c:a", "aac", "-b:a", "192k",
                "-shortest",
                "-vf", f"scale={width}:{height}",
                output_path
            ]
        else:
            # Without audio
            cmd = [
                "ffmpeg", "-y", "-framerate", str(fps),
                "-i", os.path.join(frames_dir, "frame_%05d.png"),
                "-c:v", "libx264", "-preset", "fast", "-crf", "23",
                "-vf", f"scale={width}:{height}",
                output_path
            ]
        
        try:
            subprocess.run(cmd, check=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            st.error(f"Error creating video: {e.stderr.decode() if e.stderr else str(e)}")
            return None
        
        progress_bar.progress(100)
        status_text.text("Video created successfully!")
        
        # Copy to workspace for download
        final_path = os.path.join("/workspace/project", "youtube_shorts_output.mp4")
        import shutil
        shutil.copy(output_path, final_path)
        
        return final_path


def main():
    st.markdown('<h1 class="main-header">🎬 YouTube Shorts Video Generator</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Create stunning vertical videos for YouTube Shorts in minutes</p>', unsafe_allow_html=True)
    
    # Sidebar configuration
    with st.sidebar:
        st.markdown("### ⚙️ Configuration")
        
        # Background type
        bg_type = st.radio("Background Type", ["Solid Color", "Gradient", "Image"], index=0)
        
        bg_value = None
        
        if bg_type == "Solid Color":
            bg_value = st.color_picker("Background Color", "#FF0050")
        elif bg_type == "Gradient":
            st.markdown("#### Select Gradient")
            selected_gradient = st.selectbox("Choose a gradient", list(GRADIENTS.keys()))
            bg_value = selected_gradient
            
            # Preview gradients
            cols = st.columns(5)
            for i, (name, colors) in enumerate(GRADIENTS.items()):
                with cols[i % 5]:
                    st.markdown(f"""
                    <div style="background: linear-gradient(180deg, {colors[0]}, {colors[1]}); 
                                width: 100%; height: 40px; border-radius: 8px; margin: 2px;"></div>
                    """, unsafe_allow_html=True)
        else:
            uploaded_bg = st.file_uploader("Upload Background Image", type=["png", "jpg", "jpeg", "webp"])
            if uploaded_bg:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
                    tmp.write(uploaded_bg.getvalue())
                    bg_value = tmp.name
        
        st.divider()
        
        # Text overlay
        st.markdown("### ✏️ Text Overlay")
        text = st.text_area("Overlay Text", value="Your Text Here!", height=100, placeholder="Enter your text...")
        text_color = st.color_picker("Text Color", "#FFFFFF")
        font_size = st.slider("Font Size", 24, 120, 48, help="Adjust text size")
        position = st.selectbox("Text Position", ["top", "center", "bottom"], index=1)
        animation = st.selectbox("Text Animation", list(ANIMATIONS.keys()), index=1)
        
        st.divider()
        
        # Audio
        st.markdown("### 🎵 Background Music")
        use_audio = st.checkbox("Add Background Music")
        audio_path = None
        
        if use_audio:
            audio_file = st.file_uploader("Upload Audio", type=["mp3", "wav", "ogg"])
            if audio_file:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
                    tmp.write(audio_file.getvalue())
                    audio_path = tmp.name
        
        st.divider()
        
        # Video settings
        st.markdown("### 🎥 Video Settings")
        duration = st.select_slider("Duration", options=[15, 30, 60], value=15)
        
        st.markdown(f"**Resolution:** 1080 × 1920 (9:16)")
        st.markdown(f"**Format:** MP4 (H.264)")
        st.markdown(f"**Frame Rate:** 30 FPS")
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📺 Preview")
        with st.container():
            st.markdown('<div class="preview-container">', unsafe_allow_html=True)
            
            # Create preview
            preview_bg_type = "solid" if bg_type == "Solid Color" else ("gradient" if bg_type == "Gradient" else "image")
            preview_bg_value = bg_value
            
            if text:
                preview_frame = create_preview_frame(
                    preview_bg_type, preview_bg_value, text, 
                    font_size // 2, text_color, position, animation, 30
                )
                st.image(preview_frame, use_container_width=True)
            else:
                st.markdown("""
                <div style="aspect-ratio: 9/16; background: linear-gradient(180deg, #1A1A2E, #16213E); 
                            border-radius: 12px; display: flex; align-items: center; 
                            justify-content: center; color: #666; min-height: 400px;">
                    <p>Enter text to see preview</p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 📝 Details")
        with st.container():
            st.markdown("""
            <div style="background: #16213E; padding: 20px; border-radius: 12px; margin: 10px 0;">
                <h4 style="color: #FF0050; margin-bottom: 15px;">Video Summary</h4>
                <p><strong>Background:</strong> {}</p>
                <p><strong>Text:</strong> {}</p>
                <p><strong>Animation:</strong> {}</p>
                <p><strong>Duration:</strong> {} seconds</p>
                <p><strong>Audio:</strong> {}</p>
            </div>
            """.format(
                bg_type,
                text[:50] + "..." if len(text) > 50 else text or "None",
                animation,
                duration,
                "Included" if audio_path else "None"
            ), unsafe_allow_html=True)
            
            # Tips
            st.markdown("""
            <div style="background: linear-gradient(135deg, #16213E, #1E2A4A); padding: 20px; 
                        border-radius: 12px; border-left: 4px solid #FF0050;">
                <h4 style="color: #FFD700; margin-bottom: 10px;">💡 Pro Tips</h4>
                <ul style="color: #CCCCCC; font-size: 14px;">
                    <li>Keep text short and impactful for better engagement</li>
                    <li>Use high contrast between text and background</li>
                    <li>Vertical videos perform best with minimal text</li>
                    <li>Add background music to increase watch time</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
    
    # Generate button
    st.divider()
    
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    
    with col_btn2:
        if st.button("🎬 Generate Video", use_container_width=True):
            if not text:
                st.warning("Please enter some text for the overlay!")
            else:
                with st.spinner("Creating your video..."):
                    video_path = generate_video(
                        preview_bg_type, bg_value, text, font_size, text_color,
                        position, animation, duration, audio_path
                    )
                    
                    if video_path:
                        st.session_state.generated_video = video_path
                        st.success("✅ Video generated successfully!")
    
    # Download section
    if st.session_state.generated_video:
        st.divider()
        st.markdown("### ⬇️ Download")
        
        col_dl1, col_dl2 = st.columns([1, 1])
        
        with col_dl1:
            with open(st.session_state.generated_video, "rb") as f:
                st.download_button(
                    label="📥 Download Video",
                    data=f,
                    file_name="youtube_shorts_video.mp4",
                    mime="video/mp4",
                    use_container_width=True
                )
        
        with col_dl2:
            if st.button("🔄 Generate New", use_container_width=True):
                st.session_state.generated_video = None
                st.rerun()
    
    # Footer
    st.divider()
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 20px;">
        <p>Built with ❤️ using Streamlit | Optimized for YouTube Shorts (9:16)</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()