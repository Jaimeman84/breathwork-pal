# src/app.py
import streamlit as st
import plotly.graph_objects as go
from breathing_patterns.circle_pattern import CirclePattern
from breathing_patterns.wave_pattern import WavePattern
from breathing_patterns.square_pattern import SquarePattern
import time
import numpy as np

class BreathingApp:
    def __init__(self):
        self.init_session_state()
        
    def init_session_state(self):
        """Initialize session state variables"""
        if 'is_playing' not in st.session_state:
            st.session_state.is_playing = False
        if 'start_time' not in st.session_state:
            st.session_state.start_time = None
        if 'elapsed_time' not in st.session_state:
            st.session_state.elapsed_time = 0.0
            
    def get_current_position(self, x, y, progress):
        """Calculate current position on the pattern"""
        total_points = len(x)
        current_idx = int((progress % 1.0) * total_points)
        return x[current_idx], y[current_idx]
    
    def create_visualization(self, pattern, x, y, current_x, current_y):
        """Create visualization with start/end points and current position"""
        fig = go.Figure()
        
        # Add pattern line
        fig.add_trace(go.Scatter(
            x=x, y=y,
            mode="lines",
            line=dict(color="rgba(0,146,255,0.4)", width=3),
            name="Pattern"
        ))
        
        # Add start point (green star)
        start_point, end_point = pattern.get_start_end_points()
        fig.add_trace(go.Scatter(
            x=[start_point[0]],
            y=[start_point[1]],
            mode="markers",
            marker=dict(
                size=20,
                color="green",
                symbol="star",
                line=dict(color="white", width=2)
            ),
            name="Start"
        ))
        
        # Add end point (red star)
        fig.add_trace(go.Scatter(
            x=[end_point[0]],
            y=[end_point[1]],
            mode="markers",
            marker=dict(
                size=20,
                color="red",
                symbol="star",
                line=dict(color="white", width=2)
            ),
            name="End"
        ))
        
        # Add moving dot
        fig.add_trace(go.Scatter(
            x=[current_x],
            y=[current_y],
            mode="markers",
            marker=dict(size=15, color="rgb(0,146,255)"),
            name="Current Position"
        ))
        
        # Update layout
        fig.update_layout(
            showlegend=True,
            legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01,
                bgcolor="rgba(255, 255, 255, 0.8)"
            ),
            plot_bgcolor="white",
            width=600,
            height=600,
            margin=dict(l=0, r=0, t=0, b=0),
            xaxis=dict(
                showgrid=False,
                zeroline=False,
                showticklabels=False,
                range=[-1.5, 1.5],
                scaleanchor="y",
                scaleratio=1
            ),
            yaxis=dict(
                showgrid=False,
                zeroline=False,
                showticklabels=False,
                range=[-1.5, 1.5]
            )
        )
        
        return fig
    
    def run(self):
        st.set_page_config(page_title="Breathwork App", layout="wide")
        
        # App title with emoji and styling
        st.title("🌬️ Mindful Breathing")

        # Sidebar controls
        with st.sidebar:
            st.header("Settings")
            pattern_type = st.selectbox(
                "Select Breathing Pattern",
                ["Circle Breathing", "Wave Breathing", "Square Breathing"]
            )
            
            duration = st.slider("Duration (seconds)", 30, 300, 60, step=30)
            speed = st.slider("Animation Speed", 0.5, 2.0, 1.0, step=0.1)
            
            st.markdown("---")
            st.markdown("""
            **Pattern Guide:**
            - Circle: Hold breath
            - Wave: Inhale (up) / Exhale (down)
            - Square: Inhale, Hold, Exhale, Hold
            """)
        
        # Main content
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Create pattern based on selection
            if pattern_type == "Circle Breathing":
                pattern = CirclePattern(duration)
            elif pattern_type == "Wave Breathing":
                pattern = WavePattern(duration)
            else:
                pattern = SquarePattern(duration)
            
            # Control buttons in a row with better styling
            controls_col1, controls_col2, _ = st.columns([1, 1, 2])
            
            with controls_col1:
                start_stop = st.button(
                    "⏸ Pause" if st.session_state.is_playing else "▶ Start",
                    use_container_width=True,
                    type="primary"
                )
                if start_stop:
                    if not st.session_state.is_playing:
                        st.session_state.start_time = time.time()
                    st.session_state.is_playing = not st.session_state.is_playing
            
            with controls_col2:
                if st.button("↺ Reset", use_container_width=True):
                    st.session_state.is_playing = False
                    st.session_state.elapsed_time = 0.0
                    st.session_state.start_time = None
            
            # Generate coordinates for the pattern
            x, y = pattern.generate_coordinates()
            
            # Update progress if playing
            if st.session_state.is_playing and st.session_state.start_time is not None:
                st.session_state.elapsed_time = (
                    (time.time() - st.session_state.start_time) * speed
                )
            
            # Calculate current position
            progress = (st.session_state.elapsed_time / duration) % 1.0
            current_x, current_y = self.get_current_position(x, y, progress)
            
            # Create and display visualization
            fig = self.create_visualization(pattern, x, y, current_x, current_y)
            st.plotly_chart(fig, use_container_width=True)
            
            # Rerun to update animation
            if st.session_state.is_playing:
                time.sleep(0.05)  # Small delay for smooth animation
                st.experimental_rerun()
        
        with col2:
            st.markdown(f"### {pattern.get_pattern_name()}")
            
            # Progress indicator
            if st.session_state.is_playing:
                remaining_time = duration - (st.session_state.elapsed_time % duration)
                progress_pct = ((duration - remaining_time) / duration) * 100
                
                st.progress(progress_pct / 100)
                st.markdown(f"**Time Remaining:** {int(remaining_time)} seconds")
                
                # Display current phase based on pattern type
                if isinstance(pattern, SquarePattern):
                    phases = ["Inhale", "Hold", "Exhale", "Hold"]
                    current_phase = phases[int(progress * 4) % 4]
                elif isinstance(pattern, WavePattern):
                    current_phase = "Inhale" if current_y > 0 else "Exhale"
                else:  # Circle pattern
                    current_phase = "Hold breath"
                    
                st.markdown(f"""
                <div style='padding: 10px; background-color: #f0f2f6; border-radius: 5px;'>
                    <h3 style='margin: 0; color: #0E1117;'>Current Phase: {current_phase}</h3>
                </div>
                """, unsafe_allow_html=True)
            
            # Instructions
            st.markdown("""
            ### How to Use
            1. Select your preferred breathing pattern from the sidebar
            2. Adjust the duration and speed if needed
            3. Click 'Start' to begin
            4. Follow the moving blue dot with your breath:
                - Start at the green star ⭐
                - End at the red star ⭐
            5. Use 'Pause' to pause anytime
            6. Use 'Reset' to start over
            
            Remember to breathe smoothly and naturally. If you feel any discomfort, 
            pause the exercise and return to normal breathing.
            """)

if __name__ == "__main__":
    app = BreathingApp()
    app.run()